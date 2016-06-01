"""
Created on May 16, 2016

@author: Jafar Taghiyar (jtaghiyar@bccrc.ca)
"""

from django.contrib import admin

from .models import Sample, AdditionalSampleInformation
from .models import Library, SublibraryInformation, LibrarySampleDetail
from .models import LibraryConstructionInformation
from .models import LibraryQuantificationAndStorage
from .models import Sequencing, SequencingDetail

## Sample information
class AdditionalSampleInformationInline(admin.StackedInline):
    model = AdditionalSampleInformation

class SampleAdmin(admin.ModelAdmin):
    inlines = [AdditionalSampleInformationInline]
    list_display = ['sample_id', 'sample_type']
    list_filter = ['sample_type']
    search_fields = ['sample_id']


## Library information
class SublibraryInformationInline(admin.TabularInline):
    model = SublibraryInformation
    extra = 3

class LibrarySampleDetailInline(admin.StackedInline):
    model = LibrarySampleDetail

class LibraryConstructionInformationInline(admin.StackedInline):
    model = LibraryConstructionInformation

class LibraryQuantificationAndStorageInline(admin.StackedInline):
    model = LibraryQuantificationAndStorage

class LibraryAdmin(admin.ModelAdmin):
    ## to avoid showing the field "num_libraries"
    fieldsets = [
      (
        '',
        {'fields': [
          "sample",
          "pool_id",
          "jira_ticket",
          "description",
        ]
        }
      ),
    ]
    inlines = [
      SublibraryInformationInline,
      LibrarySampleDetailInline,
      LibraryConstructionInformationInline,
      LibraryQuantificationAndStorageInline
      ]
    list_display = ['sample', 'pool_id', 'jira_ticket']
    list_filter = ['jira_ticket']
    search_fields = ['pool_id']


## Sequencing information
class SequencingDetailInline(admin.StackedInline):
    model = SequencingDetail

class SequencingAdmin(admin.ModelAdmin):
    inlines = [SequencingDetailInline]


admin.site.register(Sample, SampleAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Sequencing, SequencingAdmin)

# extra admin only information
admin.site.register(AdditionalSampleInformation)

