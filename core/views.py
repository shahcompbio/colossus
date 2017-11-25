"""
Created on May 16, 2016

@author: Jafar Taghiyar (jtaghiyar@bccrc.ca)

Updated by Spencer Vatrt-Watts (github.com/Spenca)
"""

import os
import collections
import subprocess


#============================
# Django imports
#----------------------------
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required #, permission_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.db import transaction

import pandas as pd
from django.conf import settings
from django.utils import timezone
from itertools import chain


#============================
# App imports
#----------------------------
from .helpers import Render
from .models import (
    Sample,
    DlpLibrary,
    DlpSequencing,
    PbalLibrary,
    PbalSequencing,
    TenxLibrary,
    TenxSequencing,
    DlpLane,
    PbalLane,
    TenxLane,
    SublibraryInformation,
    ChipRegion,
    ChipRegionMetadata,
    MetadataField,
    Plate,
)
from sisyphus.models import *
from .forms import (
    SampleForm, 
    AdditionalSampleInfoInlineFormset,
    DlpLibraryForm,
    PbalLibraryForm,
    TenxLibraryForm,
    DlpLibrarySampleDetailInlineFormset,
    DlpLibraryConstructionInfoInlineFormset,
    DlpLibraryQuantificationAndStorageInlineFormset,
    PbalLibrarySampleDetailInlineFormset,
    PbalLibraryConstructionInfoInlineFormset,
    PbalLibraryQuantificationAndStorageInlineFormset,
    TenxLibrarySampleDetailInlineFormset,
    TenxLibraryConstructionInfoInlineFormset,
    TenxLibraryQuantificationAndStorageInlineFormset,
    SublibraryForm,
    DlpSequencingForm,
    DlpSequencingDetailInlineFormset,
    PbalSequencingForm,
    PbalSequencingDetailInlineFormset,
    TenxSequencingForm,
    TenxSequencingDetailInlineFormset,
    DlpLaneForm,
    PbalLaneForm,
    TenxLaneForm,
    GSCFormDeliveryInfo,
    GSCFormSubmitterInfo,
    ProjectForm,
    PlateForm,
)
from .utils import (
    create_sublibrary_models,
    generate_samplesheet,
    generate_gsc_form,
)


#============================
# 3rd-party app imports
#----------------------------
from taggit.models import Tag


#============================
# Helpers
#----------------------------
def get_libraries(self):
    return list(chain(DlpLibrary.objects.filter(projects__name=self.name), PbalLibrary.objects.filter(projects__name=self.name), TenxLibrary.objects.filter(projects__name=self.name)))

# add a method to get the list of libraries for each project name
Tag.get_libraries = get_libraries


#============================
# Index page
#----------------------------
class IndexView(TemplateView):
    
    """
    Home page.
    """

    template_name = "core/index.html"
    
    def get_context_data(self):
        context = {
            'sample_size': Sample.objects.count(),
            'dlp_library_size': DlpLibrary.objects.count(),
            'dlp_sequencing_size': DlpSequencing.objects.count(),
            'pbal_library_size': PbalLibrary.objects.count(),
            'pbal_sequencing_size': PbalSequencing.objects.count(),
            'tenx_library_size': TenxLibrary.objects.count(),
            'tenx_sequencing_size': TenxSequencing.objects.count(),
            'analysisinformation_size':AnalysisInformation.objects.count(),
            'analysisrun_size':AnalysisRun.objects.count(),
        }
        return context


#============================
# Sample views
#----------------------------
class SampleList(TemplateView):
    
    """
    List of samples.
    """

    template_name = "core/sample_list.html"

    def get_context_data(self):
        context = {
            'samples': Sample.objects.all().order_by('sample_id'),
        }
        return context


class SampleDetail(TemplateView):
    
    """
    Sample detail page.
    """

    template_name = "core/sample_detail.html"

    def get_context_data(self, pk):
        context = {
            'sample': get_object_or_404(Sample, pk=pk),
            'library_list': ['dlp', 'pbal', 'tenx'],
            'pk': pk,
        }   
        return context
        

@method_decorator(login_required, name='dispatch')
class SampleCreate(TemplateView):

    """
    Sample create page.
    """

    template_name="core/sample_create.html"

    def get_context_and_render(self, request, form, formset, pk=None):
        context = {
            'pk': pk,
            'form': form,
            'formset': formset,
        }
        return render(request, self.template_name, context)

    def get(self, request):
        form = SampleForm()
        formset = AdditionalSampleInfoInlineFormset()
        return self.get_context_and_render(request, form, formset)

    def post(self, request):
        form = SampleForm(request.POST)
        formset = AdditionalSampleInfoInlineFormset(request.POST)
        if form.is_valid() and formset.is_valid():
            instance = form.save(commit=False)
            formset.instance = instance
            instance.save()
            formset.save()
            msg = "Successfully created the Sample."
            messages.success(request, msg)
            return HttpResponseRedirect(instance.get_absolute_url())

        msg = "Failed to create the sample. Please fix the errors below."
        messages.error(request, msg)
        return self.get_context_and_render(request, form, formset)


class SampleUpdate(SampleCreate):
    
    """
    Sample update page.
    """

    template_name = "core/sample_update.html"

    def get(self, request, pk):
        sample = get_object_or_404(Sample, pk=pk)
        form=SampleForm(instance=sample)
        formset=AdditionalSampleInfoInlineFormset(instance=sample)
        return self.get_context_and_render(request, form, formset, pk=pk)

    def post(self, request, pk):
        sample = get_object_or_404(Sample, pk=pk)
        form = SampleForm(request.POST, instance=sample)
        formset = AdditionalSampleInfoInlineFormset(request.POST, instance=sample)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            msg = "Successfully updated the Sample."
            messages.success(request, msg)
            return HttpResponseRedirect(sample.get_absolute_url())

        msg = "Failed to update the sample. Please fix the errors below."
        messages.error(request, msg)
        return self.get_context_and_render(request, form, formset, pk=pk)


@method_decorator(login_required, name='dispatch')
class SampleDelete(TemplateView):
    
    """
    Sample delete page.
    """

    template_name = "core/sample_delete.html"

    def get_context_data(self, pk): 
        context = {
            'sample': get_object_or_404(Sample, pk=pk),
            'pk': pk,
        }
        return context

    def post(self, request, pk):
        get_object_or_404(Sample, pk=pk).delete()
        msg = "Successfully deleted the Sample."
        messages.success(request, msg)
        return HttpResponseRedirect(reverse('core:sample_list'))


#============================
# Library views
#----------------------------
class LibraryList(TemplateView):
    
    """
    Library list base class.
    """

    class Meta:
        abstract = True

    template_name = "core/library_list.html"

    def get_context_data(self):
        context = {
            'libraries': self.library_class.objects.all().order_by(self.order), 
            'library_type': self.library_type,
        }
        return context


class DlpLibraryList(LibraryList):

    """
    List of DLP libraries.
    """

    order = 'pool_id'
    library_class = DlpLibrary
    library_type = 'dlp'


class PbalLibraryList(LibraryList):

    """
    List of PBAL libraries.
    """

    order = 'sample_id'
    library_class = PbalLibrary
    library_type = 'pbal'


class TenxLibraryList(LibraryList):

    """
    List of 10x libraries.
    """

    order = 'sample_id'
    library_class = TenxLibrary
    library_type = 'tenx'


class LibraryDetail(TemplateView):

    """
    Library detail base class.
    """

    class Meta:
        abstract = True

    template_name = "core/library_detail.html"

    def get_context_and_render(self, request, library, library_type, analyses=None, sublibinfo_fields=None, chip_metadata=None, metadata_fields=None):
        context = {
            'library': library, 
            'library_type': library_type,
            'analyses': analyses,
            'sublibinfo_fields': sublibinfo_fields,
            'chip_metadata': chip_metadata,
            'metadata_fields': metadata_fields,
        }
        return render(request, self.template_name, context)

    def get(self, request, pk):
        library = get_object_or_404(self.library_class, pk=pk)
        library_type = self.library_type
        return self.get_context_and_render(request, library, library_type)


class DlpLibraryDetail(LibraryDetail):

    """
    DLP library detail page.
    """

    def get(self, request, pk):
        library = get_object_or_404(DlpLibrary, pk=pk)
        library_type = 'dlp'
        analyses = AnalysisInformation.objects.filter(sequencings__in=library.dlpsequencing_set.all()).distinct()
        sublibinfo = SublibraryInformation()
        fields = MetadataField.objects.distinct().filter(chipregionmetadata__chip_region__library=library).values_list('field', flat=True).distinct()
        metadata_dict = collections.OrderedDict()
        
        for chip_region in library.chipregion_set.all().order_by('region_code'):
            metadata_set = chip_region.chipregionmetadata_set.all()
            d1 = {}

            for metadata in metadata_set:
                d1[metadata.metadata_field.field] = metadata.metadata_value
            row = []

            for field in fields:
                # Check that columns named in "fields" exist, else populate with "" if no entry in row for that particular metadata column
                # then adding it to a metadata dictionary with other rows
                if field not in d1.keys():
                    d1[field] = ""
                row.append(d1[field])
            metadata_dict[chip_region.region_code] = row

        return self.get_context_and_render(request, library, library_type, analyses, sublibinfo.get_fields(), metadata_dict, fields)


class PbalLibraryDetail(LibraryDetail):

    """
    PBAL library detail page.
    """

    library_class = PbalLibrary
    library_type = 'pbal'
    # sisyphus integration not implemented yet for pbal
    # analyses = AnalysisInformation.objects.filter(sequencings__in=library.pbalsequencing_set.all()).distinct()


class TenxLibraryDetail(LibraryDetail):

    """
    10x library detail page.
    """

    library_class = TenxLibrary
    library_type = 'tenx'
    # sisyphus integration not implemented yet for 10x
    # analyses = AnalysisInformation.objects.filter(sequencings__in=library.tenxsequencing_set.all()).distinct()


@method_decorator(login_required, name='dispatch')
class LibraryDelete(TemplateView):
    
    """
    Library delete base class.
    """

    class Meta:
        abstract = True

    template_name = "core/library_delete.html"

    def get_context_data(self, pk): 
        context = {
            'library': get_object_or_404(self.library_class, pk=pk),
            'pk': pk,
            'library_type': self.library_type,
        }
        return context

    def post(self, request, pk):
        get_object_or_404(self.library_class, pk=pk).delete()
        msg = "Successfully deleted the Library."
        messages.success(request, msg)
        return HttpResponseRedirect(reverse(self.library_type + ':library_list'))


class DlpLibraryDelete(LibraryDelete):

    """
    DLP library delete page.
    """

    library_class = DlpLibrary
    library_type = 'dlp'


class PbalLibraryDelete(LibraryDelete):

    """
    PBAL library delete page.
    """

    library_class = PbalLibrary
    library_type = 'pbal'


class TenxLibraryDelete(LibraryDelete):

    """
    10x library delete page.
    """

    library_class = TenxLibrary
    library_type = 'tenx'


@method_decorator(login_required, name='dispatch')
class LibraryCreate(TemplateView):

    """
    Library create base class.
    """

    class Meta:
        abstract = True

    template_name = "core/library_create.html"

    def get_context_data(self, pk=None):
        if pk:
            sample = get_object_or_404(Sample, pk=pk)
        else:
            sample = None
        
        context = {
            'lib_form': self.lib_form_class(),
            'sublib_form': SublibraryForm(),
            'libdetail_formset': self.libdetail_formset_class(),
            'libcons_formset': self.libcons_formset_class(),
            'libqs_formset': self.libqs_formset_class(),
            'projects': [t.name for t in Tag.objects.all()],
            'sample': str(sample),
            'sample_id': pk,
            'related_libs': DlpLibrary.objects.all(),
            'library_type': self.library_type,
        }
        return context

    def get(self, request, pk=None):
        context = self.get_context_data(pk)
        return render(request, self.template_name, context)

    def post(self, request, pk=None):
        context = self.get_context_data(pk)
        return self._post(request, context)

    def _post(self, request, context, library=None):
        # this is becaues of this django feature:
        # https://code.djangoproject.com/ticket/1130
        request.POST['projects'] = ','.join(request.POST.getlist('projects'))

        lib_form = self.lib_form_class(request.POST, instance=library)
        sublib_form = SublibraryForm(request.POST, request.FILES or None)
        context['lib_form'] = lib_form
        context['sublib_form'] = sublib_form

        error_message = ''
        try:
            with transaction.atomic():
                if lib_form.is_valid() and sublib_form.is_valid():
                    # if 'commit=True' when saving lib_form, then it strangely
                    # raises the following error when trying to save the
                    # ManyToMany 'Projects' field:
                    # 'LibraryForm' object has no attribute 'save_m2m'.
                    # see this: https://stackoverflow.com/questions/7083152/is-save-m2m-required-in-the-django-forms-save-method-when-commit-false
                    instance = lib_form.save(commit=False)
                    all_valid, formsets = self._validate_formsets(request, instance)
                    context.update(formsets)
                    if all_valid:
                        instance.save()
                        # save the ManyToMany field.
                        lib_form.save_m2m()
                        # Add information from SmartChipApp files
                        region_metadata = sublib_form.cleaned_data.get('smartchipapp_region_metadata')
                        sublib_results = sublib_form.cleaned_data.get('smartchipapp_results')
                        if region_metadata is not None and sublib_results is not None:
                            instance.sublibraryinformation_set.all().delete()
                            instance.chipregion_set.all().delete()
                            create_sublibrary_models(instance, sublib_results, region_metadata)
                        # save the formsets.
                        [formset.save() for formset in formsets.values()]
                        messages.success(request, "Successfully created the Library.")
                        return HttpResponseRedirect(instance.get_absolute_url())
        except ValueError as e:
            error_message = ' '.join(e.args)

        error_message = "Failed to create the library. " + error_message + ". Please fix the errors below."
        messages.error(request, error_message)
        return render(request, self.template_name, context)

    def _validate_formsets(self, request, instance):
        all_valid = True
        formsets = {
            'libdetail_formset': self.libdetail_formset_class(
                request.POST,
                instance=instance,
            ),
            'libcons_formset': self.libcons_formset_class(
                request.POST,
                instance=instance,
            ),
            'libqs_formset': self.libqs_formset_class(
                request.POST,
                request.FILES or None,
                instance=instance,
            ),
        }
        for k, formset in formsets.items():
            if not formset.is_valid():
                all_valid = False
            formsets[k] = formset
        return all_valid, formsets


class DlpLibraryCreate(LibraryCreate):

    """
    DLP library create page.
    """

    lib_form_class = DlpLibraryForm
    libdetail_formset_class = DlpLibrarySampleDetailInlineFormset
    libcons_formset_class = DlpLibraryConstructionInfoInlineFormset
    libqs_formset_class = DlpLibraryQuantificationAndStorageInlineFormset
    library_type = 'dlp'


class PbalLibraryCreate(LibraryCreate):

    """
    PBAL library create page.
    """

    lib_form_class = PbalLibraryForm
    libdetail_formset_class = PbalLibrarySampleDetailInlineFormset
    libcons_formset_class = PbalLibraryConstructionInfoInlineFormset
    libqs_formset_class = PbalLibraryQuantificationAndStorageInlineFormset
    library_type = 'pbal'


class TenxLibraryCreate(LibraryCreate):

    """
    10x library create page.
    """

    lib_form_class = TenxLibraryForm
    libdetail_formset_class = TenxLibrarySampleDetailInlineFormset
    libcons_formset_class = TenxLibraryConstructionInfoInlineFormset
    libqs_formset_class = TenxLibraryQuantificationAndStorageInlineFormset
    library_type = 'tenx'


class LibraryUpdate(LibraryCreate):

    """
    Library update base class.
    """

    class Meta:
        abstract = True

    template_name = "core/library_update.html"

    def get_context_data(self, pk):
        library = get_object_or_404(self.library_class, pk=pk)
        selected_projects = library.projects.names()
        selected_related_libs = library.relates_to.only()
        
        context = {
            'pk': pk,
            'lib_form': self.lib_form_class(instance=library),
            'sublib_form': SublibraryForm(),
            'libdetail_formset': self.libdetail_formset_class(instance=library),
            'libcons_formset': self.libcons_formset_class(instance=library),
            'libqs_formset': self.libqs_formset_class(instance=library),
            'projects': [t.name for t in Tag.objects.all()],
            'selected_projects': selected_projects,
            'related_libs': DlpLibrary.objects.all(),
            'selected_related_libs': selected_related_libs,
            'library_type': self.library_type,
        }
        return context

    def post(self, request, pk):
        context = self.get_context_data(pk)
        library = get_object_or_404(self.library_class, pk=pk)
        return self._post(request, context, library=library)    


class DlpLibraryUpdate(LibraryUpdate):

    """
    DLP library update page.
    """

    library_class = DlpLibrary
    lib_form_class = DlpLibraryForm
    libdetail_formset_class = DlpLibrarySampleDetailInlineFormset
    libcons_formset_class = DlpLibraryConstructionInfoInlineFormset
    libqs_formset_class = DlpLibraryQuantificationAndStorageInlineFormset
    library_type = 'dlp'


class PbalLibraryUpdate(LibraryUpdate):

    """
    PBAL library update page.
    """

    library_class = PbalLibrary
    lib_form_class = PbalLibraryForm
    libdetail_formset_class = PbalLibrarySampleDetailInlineFormset
    libcons_formset_class = PbalLibraryConstructionInfoInlineFormset
    libqs_formset_class = PbalLibraryQuantificationAndStorageInlineFormset
    library_type = 'pbal'


class TenxLibraryUpdate(LibraryUpdate):

    """
    10x library update page.
    """

    library_class = TenxLibrary
    lib_form_class = TenxLibraryForm
    libdetail_formset_class = TenxLibrarySampleDetailInlineFormset
    libcons_formset_class = TenxLibraryConstructionInfoInlineFormset
    libqs_formset_class = TenxLibraryQuantificationAndStorageInlineFormset
    library_type = 'tenx'


#============================
# Project views
#----------------------------
class ProjectList(TemplateView):
    
    """
    Project detail page.
    """

    template_name = "core/project_list.html"

    def get_context_data(self):
        context = {
            'projects': Tag.objects.all().order_by('name'),
        }
        return context


@method_decorator(login_required, name='dispatch')
class ProjectDelete(TemplateView):

    """
    Project delete page.
    """

    template_name = "core/project_delete.html"

    def get_context_data(self, pk):
        context = {
            'project': get_object_or_404(Tag, pk=pk),
            'pk': pk,
        }
        return context

    def post(self, request, pk):
        get_object_or_404(Tag, pk=pk).delete()
        msg = "Successfully deleted the Project."
        messages.success(request, msg)
        return HttpResponseRedirect(reverse('core:project_list'))


@method_decorator(login_required, name='dispatch')
class ProjectUpdate(TemplateView):
    
    """
    Project update page.
    """

    template_name = "core/project_update.html"

    def get_context_data(self, pk):
        context = {
            'pk': pk,
            'form': ProjectForm(instance=get_object_or_404(Tag, pk=pk)), 
        }
        return context

    def post(self, request, pk):
        form = ProjectForm(request.POST, instance=get_object_or_404(Tag, pk=pk))
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            msg = "Successfully updated the Project."
            messages.success(request, msg)
            return HttpResponseRedirect(reverse('core:project_list'))


#============================
# Sequencing views
#----------------------------
class SequencingList(TemplateView):

    """
    Sequencing list base class.
    """

    class Meta:
        abstract = True

    template_name = "core/sequencing_list.html"

    def get_context_data(self):
        context = {
            'sequencings': self.sequencing_class.objects.all().order_by('library'),
            'library_type': self.library_type,
        }
        return context


class DlpSequencingList(SequencingList):

    """
    List of DLP sequencings.
    """

    sequencing_class = DlpSequencing
    library_type = 'dlp'


class PbalSequencingList(SequencingList):

    """
    List of PBAL sequencings.
    """

    sequencing_class = PbalSequencing
    library_type = 'pbal'


class TenxSequencingList(SequencingList):

    """
    List of 10x sequencings.
    """

    sequencing_class = TenxSequencing
    library_type = 'tenx'


class SequencingDetail(TemplateView):

    """
    Sequencing detail base class.
    """

    class Meta:
        abstract = True

    template_name = "core/sequencing_detail.html"

    def get(self, request, pk):
        key = "gsc_form_metadata_%s" % pk
        download = False
        if key in request.session.keys():
            download = True
        
        context = {
            'sequencing': get_object_or_404(self.sequencing_class, pk=pk),
            'download': download,
            'library_type': self.library_type,
        }
        return render(request, self.template_name, context) 


class DlpSequencingDetail(SequencingDetail):

    """
    DLP sequencing detail page.
    """

    sequencing_class = DlpSequencing
    library_type = 'dlp'


class PbalSequencingDetail(SequencingDetail):

    """
    DLP sequencing detail page.
    """

    sequencing_class = PbalSequencing
    library_type = 'pbal'


class TenxSequencingDetail(SequencingDetail):

    """
    10x sequencing detail page.
    """

    sequencing_class = TenxSequencing
    library_type = 'tenx'
            

@method_decorator(login_required, name='dispatch')
class SequencingCreate(TemplateView):

    """
    Sequencing create base class.
    """

    class Meta:
        abstract = True

    template_name = "core/sequencing_create.html"

    def get_context_and_render(self, request, from_library, form, seqdetail_formset):
        if from_library:
            library = get_object_or_404(self.library_class, pk=from_library)
        else:
            library = None

        context = {
            'form': form,
            'seqdetail_formset': seqdetail_formset,
            'library': str(library),
            'library_id': from_library,
            'related_seqs': self.sequencing_class.objects.all(),
            'library_type': self.library_type,
        }
        return render(request, self.template_name, context)

    def get(self, request, from_library=None):
        form = self.form_class()
        seqdetail_formset = self.seqdetail_formset_class()
        return self.get_context_and_render(request, from_library, form, seqdetail_formset)

    def post(self, request, from_library=None):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m() 
            seqdetail_formset = self.seqdetail_formset_class(
                request.POST,
                instance=instance,
            )
            if seqdetail_formset.is_valid():
                seqdetail_formset.save()

            msg = "Successfully created the Sequencing."
            messages.success(request, msg)
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            msg = "Failed to create the sequencing. Please fix the errors below."
            messages.error(request, msg)
            seqdetail_formset = self.seqdetail_formset_class()
            return self.get_context_and_render(request, from_library, form, seqdetail_formset)


class DlpSequencingCreate(SequencingCreate):

    """
    DLP sequencing create page.
    """

    library_class = DlpLibrary
    sequencing_class = DlpSequencing
    form_class = DlpSequencingForm
    seqdetail_formset_class = DlpSequencingDetailInlineFormset
    library_type = 'dlp'


class PbalSequencingCreate(SequencingCreate):

    """
    PBAL sequencing create page.
    """

    library_class = PbalLibrary
    sequencing_class = PbalSequencing
    form_class = PbalSequencingForm
    seqdetail_formset_class = PbalSequencingDetailInlineFormset
    library_type = 'pbal'


class TenxSequencingCreate(SequencingCreate):

    """
    10x sequencing create page.
    """

    library_class = TenxLibrary
    sequencing_class = TenxSequencing
    form_class = TenxSequencingForm
    seqdetail_formset_class = TenxSequencingDetailInlineFormset
    library_type = 'tenx'


@method_decorator(login_required, name='dispatch')
class SequencingUpdate(TemplateView):

    """
    Sequencing update base class.
    """

    class Meta:
        abstract = True

    template_name = "core/sequencing_update.html"

    def get_context_and_render(self, request, sequencing, form, seqdetail_formset):
        context = {
            'pk': sequencing.pk,
            'form': form,
            'seqdetail_formset': seqdetail_formset,
            'related_seqs': self.sequencing_class.objects.all(),
            'selected_related_seqs': sequencing.relates_to.only(),
            'library_type': self.library_type,
        }
        return render(request, self.template_name, context)

    def get(self, request, pk):
        sequencing = get_object_or_404(self.sequencing_class, pk=pk)
        form = self.form_class(instance=sequencing)
        seqdetail_formset = self.seqdetail_formset_class(instance=sequencing)
        return self.get_context_and_render(request, sequencing, form, seqdetail_formset)

    def post(self, request, pk):
        sequencing = get_object_or_404(self.sequencing_class, pk=pk)
        form = self.form_class(request.POST, instance=sequencing)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()
            seqdetail_formset = self.seqdetail_formset_class(
                request.POST,
                instance=instance,
            )                        
            if seqdetail_formset.is_valid():
                seqdetail_formset.save()

            msg = "Successfully updated the Sequencing."
            messages.success(request, msg)
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            msg = "Failed to update the sequencing. Please fix the errors below."
            messages.error(request, msg)
            seqdetail_formset = self.seqdetail_formset_class(instance=sequencing)
            return self.get_context_and_render(request, sequencing, form, seqdetail_formset)


class DlpSequencingUpdate(SequencingUpdate):

    """
    DLP sequencing update page.
    """

    sequencing_class = DlpSequencing
    form_class = DlpSequencingForm
    seqdetail_formset_class = DlpSequencingDetailInlineFormset
    library_type = 'dlp'


class PbalSequencingUpdate(SequencingUpdate):

    """
    PBAL sequencing update page.
    """

    sequencing_class = PbalSequencing
    form_class = PbalSequencingForm
    seqdetail_formset_class = PbalSequencingDetailInlineFormset
    library_type = 'pbal'


class TenxSequencingUpdate(SequencingUpdate):

    """
    10x sequencing update page.
    """

    sequencing_class = TenxSequencing
    form_class = TenxSequencingForm
    seqdetail_formset_class = TenxSequencingDetailInlineFormset
    library_type = 'tenx'


@method_decorator(login_required, name='dispatch')
class SequencingDelete(TemplateView):

    """
    Sequencing delete base class.
    """

    class Meta:
        abstract = True

    template_name = "core/sequencing_delete.html"

    def get_context_data(self, pk):
        context = {
            'sequencing': get_object_or_404(self.sequencing_class, pk=pk),
            'pk': pk,
            'library_type': self.library_type,
        }
        return context

    def post(self, request, pk):
        get_object_or_404(self.sequencing_class, pk=pk).delete()
        msg = "Successfully deleted the Sequencing."
        messages.success(request, msg)
        return HttpResponseRedirect(reverse(self.library_type + ':sequencing_list'))


class DlpSequencingDelete(SequencingDelete):

    """
    DLP sequencing delete page.
    """

    sequencing_class = DlpSequencing
    library_type = 'dlp'


class PbalSequencingDelete(SequencingDelete):

    """
    PBAL sequencing delete page.
    """

    sequencing_class = PbalSequencing
    library_type = 'pbal'


class TenxSequencingDelete(SequencingDelete):

    """
    10x sequencing delete page.
    """

    sequencing_class = TenxSequencing
    library_type = 'tenx'


def dlp_sequencing_get_samplesheet(request, pk):
    
    """
    Generates downloadable samplesheet.
    """
    
    ofilename, ofilepath = generate_samplesheet(pk)
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % ofilename
    ofile = open(ofilepath, 'r')
    response.write(ofile.read())
    ofile.close()
    os.remove(ofilepath)
    return response


def dlp_sequencing_get_queried_samplesheet(request, pool_id, flowcell):
    
    """
    Makes downloading samplesheets from flowcell possible. 
    """

    try:
        pk = DlpLane.objects.get(flow_cell_id=flowcell, sequencing__library__pool_id=pool_id).pk
        return dlp_sequencing_get_samplesheet(request, pk)
    except DlpSequencing.DoesNotExist:
        msg = "Sorry, no sequencing with flowcell {} and chip id {} found.".format(flowcell, pool_id)
        messages.warning(request, msg)
        return HttpResponseRedirect(reverse('index'))


@method_decorator(login_required, name='dispatch')
class DlpSequencingCreateGSCFormView(TemplateView):

    """
    Sequencing GSC submission form.
    """

    template_name = "core/sequencing_create_gsc_form.html"

    def get_context_data(self, pk):
        context = {
            'pk': pk,
            'delivery_info_form': GSCFormDeliveryInfo(),
            'submitter_info_form': GSCFormSubmitterInfo(),
            'library_type': 'dlp',
        }
        return context

    def get(self, request, pk):
        context = self.get_context_data(pk)
        return render(request, self.template_name, context)

    def post(self, request, pk):
        sequencing = get_object_or_404(DlpSequencing, pk=pk)
        context = self.get_context_data(pk)
        delivery_info_form = GSCFormDeliveryInfo(request.POST)
        submitter_info_form = GSCFormSubmitterInfo(request.POST)
        if delivery_info_form.is_valid() and submitter_info_form.is_valid():
            key = "gsc_form_metadata_%s" % pk
            request.session[key] = request.POST
            msg = "Successfully started downloading the GSC submission form."
            messages.success(request, msg)
            return HttpResponseRedirect(sequencing.get_absolute_url())
        else:
            context['delivery_info_form'] = delivery_info_form
            context['submitter_info_form'] = submitter_info_form
            msg = "please fix the errors below."
            messages.error(request, msg)
        return render(request, self.template_name, context)


def dlp_sequencing_get_gsc_form(request, pk):
    
    """
    Generates downloadable GSC submission form.
    """
    
    key = "gsc_form_metadata_%s" % pk
    metadata = request.session.pop(key)
    ofilename, ofilepath = generate_gsc_form(pk, metadata)
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % ofilename
    ofile = open(ofilepath, 'r')
    response.write(ofile.read())
    ofile.close()
    os.remove(ofilepath)
    return response


#============================
# Lane views
#----------------------------
@method_decorator(login_required, name='dispatch')
class LaneCreate(TemplateView):

    """
    Lane create page.
    """

    template_name = "core/lane_create.html"

    def get_context_and_render(self, request, from_sequencing, form):
        if from_sequencing:
            sequencing = get_object_or_404(self.sequencing_class, pk=from_sequencing)
        else:
            sequencing = None

        context = {
            'form': form,
            'sequencing': str(sequencing),
            'sequencing_id': from_sequencing,
            'library_type': self.library_type,
        }
        return render(request, self.template_name, context)

    def get(self, request, from_sequencing=None):
        form = self.form_class()
        return self.get_context_and_render(request, from_sequencing, form)

    def post(self, request, from_sequencing=None):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            msg = "Successfully created the lane."
            messages.success(request, msg)
            return HttpResponseRedirect(instance.sequencing.get_absolute_url())
        else:
            msg = "Failed to create the lane. Please fix the errors below."
            messages.error(request, msg)
            return self.get_context_and_render(request, from_sequencing, form)


class DlpLaneCreate(LaneCreate):

    """
    DLP lane create page.
    """

    sequencing_class = DlpSequencing
    form_class = DlpLaneForm
    library_type = 'dlp'


class PbalLaneCreate(LaneCreate):

    """
    PBAL lane create page.
    """

    sequencing_class = PbalSequencing
    form_class = PbalLaneForm
    library_type = 'pbal'


class TenxLaneCreate(LaneCreate):

    """
    10x lane create page.
    """

    sequencing_class = TenxSequencing
    form_class = TenxLaneForm
    library_type = 'tenx'


@method_decorator(login_required, name='dispatch')
class LaneUpdate(TemplateView):

    """
    Lane update base class.
    """

    class Meta:
        abstract = True

    template_name = "core/lane_update.html"

    def get_context_and_render(self, request, lane, form, pk):
        context = {
            'sequencing': lane.sequencing,
            'sequencing_id': lane.sequencing_id,
            'form': form,
            'pk': pk,
            'library_type': self.library_type,
        }
        return render(request, self.template_name, context)

    def get(self, request, pk):
        lane = get_object_or_404(self.lane_class, pk=pk)
        form = self.form_class(instance=lane)
        return self.get_context_and_render(request, lane, form, pk)

    def post(self, request, pk):
        lane = get_object_or_404(self.lane_class, pk=pk)
        form = self.form_class(request.POST, instance=lane)
        if form.is_valid():
            instance = form.save()
            msg = "Successfully updated the lane."
            messages.success(request, msg)
            return HttpResponseRedirect(instance.sequencing.get_absolute_url())
        else:
            msg = "Failed to update the lane. Please fix the errors below."
            messages.error(request, msg)
            return self.get_context_and_render(request, lane, form, pk)


class DlpLaneUpdate(LaneUpdate):

    """
    DLP lane update page.
    """

    lane_class = DlpLane
    form_class = DlpLaneForm
    library_type = 'dlp'


class PbalLaneUpdate(LaneUpdate):

    """
    PBAL lane update page.
    """

    lane_class = PbalLane
    form_class = PbalLaneForm
    library_type = 'pbal'


class TenxLaneUpdate(LaneUpdate):

    """
    10x lane update page.
    """

    lane_class = TenxLane
    form_class = TenxLaneForm
    library_type = 'tenx'


@method_decorator(login_required, name='dispatch')
class LaneDelete(TemplateView):

    """
    Lane delete base class.
    """

    class Meta:
        abstract = True

    template_name = "core/lane_delete.html"

    def get_context_and_render(self, request, lane, pk, sequencing):
        context = {
            'lane': lane,
            'pk': pk,
            'sequencing_id': sequencing.id,
            'library_type': self.library_type,
        }
        return render(request, self.template_name, context)

    def get(self, request, pk):
        lane = get_object_or_404(self.lane_class, pk=pk)
        sequencing = lane.sequencing
        return self.get_context_and_render(request, lane, pk, sequencing)

    def post(self, request, pk):
        lane = get_object_or_404(self.lane_class, pk=pk)
        sequencing = lane.sequencing
        lane.delete()
        msg = "Successfully deleted the Lane."
        messages.success(request, msg)
        return HttpResponseRedirect(sequencing.get_absolute_url())


class DlpLaneDelete(LaneDelete):

    """
    DLP lane delete page.
    """

    lane_class = DlpLane
    library_type = 'dlp'


class PbalLaneDelete(LaneDelete):

    """
    PBAL lane delete page.
    """

    lane_class = PbalLane
    library_type = 'pbal'


class TenxLaneDelete(LaneDelete):

    """
    10x lane delete page.
    """

    lane_class = TenxLane
    library_type = 'tenx'


#============================
# Plate views
#----------------------------
@Render("core/plate_create.html")
@login_required()
def plate_create(request, from_library=None):
    
    """
    Plate create page.
    """
    
    if from_library:
        library = get_object_or_404(PbalLibrary, pk=from_library)
    else:
        library = None
    
    if request.method == 'POST':
        form = PlateForm(request.POST)
        if form.is_valid():
            instance = form.save()
            msg = "Successfully created the plate."
            messages.success(request, msg)
            return HttpResponseRedirect(instance.library.get_absolute_url())
        else:
            msg = "Failed to create the plate. Please fix the errors below."
            messages.error(request, msg)
    else:
        form = PlateForm()

    context = {
        'form': form,
        'library': str(library),
        'library_id': from_library,
    }
    return context


@Render("core/plate_update.html")
@login_required()
def plate_update(request, pk):
    
    """
    Plate update page.
    """
    
    plate = get_object_or_404(Plate, pk=pk)
    
    if request.method == 'POST':
        form = PlateForm(request.POST, instance=plate)
        if form.is_valid():
            instance = form.save()
            msg = "Successfully updated the plate."
            messages.success(request, msg)
            return HttpResponseRedirect(instance.library.get_absolute_url())
        else:
            msg = "Failed to update the plate. Please fix the errors below."
            messages.error(request, msg)
    else:
        form = PlateForm(instance=plate)

    context = {
        'form': form,
        'library': plate.library,
        'library_id': plate.library_id,
        'pk': pk,
    }
    return context


@Render("core/plate_delete.html")
@login_required()
def plate_delete(request, pk):
    
    """
    Plate delete page.
    """
    
    plate = get_object_or_404(Plate, pk=pk)
    library = plate.library

    if request.method == 'POST':
        plate.delete()
        msg = "Successfully deleted the Plate."
        messages.success(request, msg)
        return HttpResponseRedirect(library.get_absolute_url())

    context = {
        'plate': plate,
        'pk': pk,
        'library_id': library.id,
    }
    return context


#============================
# Search view
#----------------------------
def search_view(request):
    query_str = request.GET.get('query_str')
    instance = None

    # search for samples
    if Sample.objects.filter(sample_id=query_str):
        instance = Sample.objects.filter(sample_id=query_str)[0]

    # search for dlp libraries
    elif DlpLibrary.objects.filter(pool_id=query_str):
        instance = DlpLibrary.objects.filter(pool_id=query_str)[0]

    # search for jira ticket associated with dlp library
    elif DlpLibrary.objects.filter(jira_ticket=query_str):
        instance = DlpLibrary.objects.filter(jira_ticket=query_str)[0]

    # search for jira ticket associated with tenx library
    elif TenxLibrary.objects.filter(jira_ticket=query_str):
        instance = TenxLibrary.objects.filter(jira_ticket=query_str)[0]

    if instance:
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        msg = "Sorry, no match found."
        messages.warning(request, msg)
        return HttpResponseRedirect(reverse('index'))


#============================
# Summary view
#----------------------------
@Render("core/summary.html")
def dlp_summary_view(request):

    library_per_sample_count = {s.sample_id : s.dlplibrary_set.count() for s in Sample.objects.all()}

    sublibrary_per_sample_count = {s.sample_id : s.sublibraryinformation_set.count() for s in Sample.objects.all()}

    context ={
        'library_per_sample': library_per_sample_count,
        'sublibrary_per_sample': sublibrary_per_sample_count,
        'total_sublibs': SublibraryInformation.objects.count(),
        'total_libs': DlpLibrary.objects.count(),
        'samples':Sample.objects.all().order_by('sample_id'),
    }
    return context


def dlp_get_filtered_sublib_count(sublibs):
    unfiltered_count = sublibs.count()

    # wells to filter out
    blankwells_count = sublibs.filter(spot_well='nan').count()

    # final count
    filtered_count = unfiltered_count - blankwells_count
    return filtered_count


def dlp_get_cell_graph(request):

    data = []
    libs = DlpLibrary.objects.filter(dlpsequencing__isnull=False, sublibraryinformation__isnull=False).distinct()

    for lib in libs:
        lib_info = {}
        lib_info['jira_ticket'] = lib.jira_ticket
        lib_info['pool_id'] = lib.pool_id
        lib_info['count'] = dlp_get_filtered_sublib_count(lib.sublibraryinformation_set)
        lib_info['id'] = lib.pk
        
        for sequencing in lib.dlpsequencing_set.all():
            lib_info['submission_date'] = sequencing.submission_date
            data.append(lib_info)

    df = pd.DataFrame(data)
    # TODO: change time to just only include date
    today = str(timezone.now().strftime('%b-%d-%Y'))
    ofilename = os.path.join("cell_count-" + today + ".csv")
    output_csv_path = os.path.join(settings.MEDIA_ROOT, ofilename)
    df.to_csv(output_csv_path, index=False)


    rscript_path = os.path.join(settings.BASE_DIR, "scripts", "every_cell_count_plot.R")
    cmd = "Rscript {rscript} {input_csv} {media_dir}/output.pdf".format(rscript=rscript_path, input_csv=output_csv_path, media_dir=settings.MEDIA_ROOT)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    r_stdout, r_stderr = p.communicate()
    if p.returncode != 0:
        raise Exception('cmd {} failed\nstdout:\n{}\nstderr:\n{}\n'.format(cmd, r_stdout, r_stderr))

    output_plots_path = os.path.join(settings.MEDIA_ROOT, "output.pdf")

    with open(output_plots_path, 'r') as plots_pdf:

        response = HttpResponse(plots_pdf, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=%s' % ("cell_count-" + today)
    os.remove(output_csv_path)
    os.remove(output_plots_path)

    return response