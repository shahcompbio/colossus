(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-605b28fc"],{"1a33":function(e,t,a){"use strict";a.r(t);var o=function(){var e=this,t=e.$createElement,a=e._self._c||t;return e.headerLoaded?a("div",[a("md-table",{attrs:{"md-width":"100%","md-height":"100%",value:e.listValues,"md-sort":"id","md-sort-order":"asc","md-fixed-header":""},scopedSlots:e._u([{key:"md-table-row",fn:function(t){var o=t.item;return a("md-table-row",{on:{click:function(t){return e.$router.replace({name:"detail",params:{app:e.$route.params.app,type:e.$route.params.type,pk:o.id}})}}},e._l(e.headers,function(t){return a("md-table-cell",{attrs:{"md-label":t,"md-sort-by":t,"md-numeric":""}},[e._v(e._s(o[t]))])}),1)}}],null,!1,1020292118)},[a("md-table-toolbar",[a("div",{staticClass:"md-toolbar-section-start"},[a("h1",{staticClass:"md-title"},[e._v(e._s(e.$route.params.type))])]),a("md-field",{staticClass:"md-toolbar-section-end",attrs:{"md-clearable":""}},[a("md-input",{attrs:{placeholder:"Search by name..."},model:{value:e.search,callback:function(t){e.search=t},expression:"search"}})],1)],1)],1),e.isEditable?e._e():a("md-button",{staticClass:"md-icon-button",on:{click:e.toggleEditForm}},[a("md-icon",[e._v("add")])],1),a("editForm",{attrs:{showForm:e.showForm,toggleEditForm:e.toggleEditForm,formData:this.$store.state.model.form_fields}})],1):e._e()},n=[],s=(a("386d"),a("bd86")),l=(a("ac6a"),a("456d"),a("bbc9")),i=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("md-radio",{model:{value:e.radio,callback:function(t){e.radio=t},expression:"radio"}},[e._v("No Value")]),a("md-radio",{model:{value:e.radio,callback:function(t){e.radio=t},expression:"radio"}},[e._v("No Value")]),a("md-radio",{model:{value:e.radio,callback:function(t){e.radio=t},expression:"radio"}},[e._v("No Value")])],1)},r=[],c={name:"customFilter",components:{},data:function(){return{radio:""}}},d=c,u=a("2877"),m=Object(u["a"])(d,i,r,!1,null,null,null),f=m.exports,p=a("2a68"),v={name:"TableSearch",components:{editForm:l["a"],customFilter:f},created:function(){var e=this;console.log("CREATED"),console.log(this.$store.state.form),this.$store.dispatch("loadData",{app:this.$route.params.app,type:"list",model:this.$route.params.type,token:this.$session.get("token")}).then(function(t){console.log("DONE"),e.dataset=t,"undefined"!==typeof t[0]&&(e.headers=Object.keys(t[0])),e.headerLoaded=!0,console.log("HELLO")},function(e){console.log("ERROR")})},beforeCreate:function(){console.log("CONE")},mounted:function(){console.log("MOUTNED")},data:function(){var e;return e={headerLoaded:!1,dataset:[],headers:[],search:null,showForm:!1},Object(s["a"])(e,"headers",["i"]),Object(s["a"])(e,"searched",[]),e},methods:{toggleEditForm:function(){console.log("fefe"),console.log(this.showForm),this.showForm=!this.showForm,console.log(this.showForm)},toggleLoading:function(){this.$store.commit("LOADING")},searchOnTable:function(){}},computed:{listValues:function(){return this.search?Object(p["c"])(this.search,this.dataset):this.dataset},isEditable:function(){return this.$store.getters.isEditable}}},b=v,h=(a("ba98"),Object(u["a"])(b,o,n,!1,null,"6aefa033",null));t["default"]=h.exports},"25a1":function(e,t,a){"use strict";var o=a("61ce"),n=a.n(o);n.a},3846:function(e,t,a){a("9e1e")&&"g"!=/./g.flags&&a("86cc").f(RegExp.prototype,"flags",{configurable:!0,get:a("0bfb")})},"386d":function(e,t,a){"use strict";var o=a("cb7c"),n=a("83a1"),s=a("5f1b");a("214f")("search",1,function(e,t,a,l){return[function(a){var o=e(this),n=void 0==a?void 0:a[t];return void 0!==n?n.call(a,o):new RegExp(a)[t](String(o))},function(e){var t=l(a,e,this);if(t.done)return t.value;var i=o(e),r=String(this),c=i.lastIndex;n(c,0)||(i.lastIndex=0);var d=s(i,r);return n(i.lastIndex,c)||(i.lastIndex=c),null===d?-1:d.index}]})},"389c":function(e,t,a){"use strict";var o=a("6527"),n=a.n(o);n.a},"454f":function(e,t,a){a("46a7");var o=a("584a").Object;e.exports=function(e,t,a){return o.defineProperty(e,t,a)}},"46a7":function(e,t,a){var o=a("63b6");o(o.S+o.F*!a("8e60"),"Object",{defineProperty:a("d9f6").f})},"61ce":function(e,t,a){},6527:function(e,t,a){},"6b54":function(e,t,a){"use strict";a("3846");var o=a("cb7c"),n=a("0bfb"),s=a("9e1e"),l="toString",i=/./[l],r=function(e){a("2aba")(RegExp.prototype,l,e,!0)};a("79e5")(function(){return"/a/b"!=i.call({source:"a",flags:"b"})})?r(function(){var e=o(this);return"/".concat(e.source,"/","flags"in e?e.flags:!s&&e instanceof RegExp?n.call(e):void 0)}):i.name!=l&&r(function(){return i.call(this)})},"83a1":function(e,t){e.exports=Object.is||function(e,t){return e===t?0!==e||1/e===1/t:e!=e&&t!=t}},"85f2":function(e,t,a){e.exports=a("454f")},ba98:function(e,t,a){"use strict";var o=a("d5e7"),n=a.n(o);n.a},bbc9:function(e,t,a){"use strict";var o,n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("md-dialog",{attrs:{"md-active":e.showForm},on:{"update:mdActive":function(t){e.showForm=t},"update:md-active":function(t){e.showForm=t}}},[a("form",{on:{submit:function(t){return t.preventDefault(),e.getFormValues(t)}}},[a("md-card",[a("md-card-header",[a("div",{staticClass:"md-title"},[e._v("create "+e._s(e.$route.params.type))])]),a("md-card-content",[a("md-subheader",[e._v("Relations")]),a("md-list",[e._l(e.formData.relations,function(t,o){return a("md-list-item",{attrs:{"md-expand":""}},[a("span",{staticClass:"md-list-item-text"},[e._v(e._s(o)+e._s(t.many))]),a("md-list",{attrs:{slot:"md-expand"},slot:"md-expand"},[a("relationManyEdit",{attrs:{relationInfo:t,selected:t.selected,many:t.many}})],1)],1)}),a("md-divider"),a("md-subheader",[e._v("Properties ")]),a("md-list-item",{attrs:{"md-expand":""}},[a("span",{staticClass:"md-list-item-text"},[e._v(e._s(e.$route.params.type)+" ")]),a("md-list",{attrs:{slot:"md-expand"},slot:"md-expand"},e._l(e.formData.fields,function(t,o){return a("md-list-item",["Date"!==t.type?a("md-field",[a("label",[e._v(e._s(o))]),"String"===t.type?a("md-input",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"value.value"}}):"Integer"===t.type?a("md-input",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"value.value"}}):"Date"===t.type?a("md-datepicker",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"value.value"}},[a("label",[e._v("Select date")])]):"Select"===t.type?a("md-select",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"value.value"}},e._l(t.choices,function(t){return a("md-option",{attrs:{value:t[0]}},[e._v(e._s(t[1]))])}),1):e._e()],1):"children"!==o&&"Date"===t.type?a("md-datepicker",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"value.value"}},[a("label",[e._v(e._s(o))])]):e._e()],1)}),1)],1),e._l(e.formData.children,function(t,o){return a("md-list-item",{attrs:{"md-expand":""}},[a("span",{staticClass:"md-list-item-text"},[e._v(e._s(o)+" ")]),a("md-list",{attrs:{slot:"md-expand"},slot:"md-expand"},e._l(t,function(t,o){return a("md-list-item",["Date"!==t.type?a("md-field",[a("label",[e._v(e._s(o))]),"String"===t.type?a("md-input",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"v.value"}}):"Integer"===t.type?a("md-input",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"v.value"}}):"Date"===t.type?a("md-datepicker",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"v.value"}},[a("label",[e._v("Select date")])]):"Select"===t.type?a("md-select",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"v.value"}},e._l(t.choices,function(t){return a("md-option",{attrs:{value:t[0]}},[e._v(e._s(t[1]))])}),1):e._e()],1):"Date"===t.type?a("md-datepicker",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"v.value"}},[a("label",[e._v(e._s(o))])]):e._e()],1)}),1)],1)})],2)],1),a("md-card-actions",[a("md-button",{attrs:{type:"submit"}},[e._v("Create")]),a("md-button",{on:{click:e.toggleEditForm}},[e._v("Cancer")])],1)],1)],1)])},s=[],l=a("bd86"),i=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("md-table-toolbar",[a("md-field",{staticClass:"md-toolbar-section-end",attrs:{"md-clearable":""}},[a("md-input",{attrs:{placeholder:"Search by name..."},on:{input:e.searchOnTable},model:{value:e.search,callback:function(t){e.search=t},expression:"search"}})],1)],1),a("md-table",{attrs:{id:"choiceTable"},scopedSlots:e._u([{key:"md-table-row",fn:function(t){var o=t.item;return a("md-table-row",{staticClass:"rowitem"},[a("md-table-cell",{attrs:{"md-label":"ID","md-sort-by":"name"}},[a("md-checkbox",{on:{click:function(e){e.stopPropagation()},change:function(t){return t.stopPropagation(),e.selectItem(o)}},model:{value:o.selected,callback:function(t){e.$set(o,"selected",t)},expression:"item.selected"}}),e._v(e._s(o.name)+e._s(o.selected))],1)],1)}}]),model:{value:e.items,callback:function(t){e.items=t},expression:"items"}})],1)},r=[],c=(a("ac6a"),a("386d"),a("7f7f"),a("6762"),a("2fdb"),a("6b54"),function(e){return e.toString().toLowerCase()}),d=function(e,t){return t?e.filter(function(e){return c(e.name).includes(c(t))}):e},u={name:"relationManyEdit",props:["relationInfo","selected","many"],data:function(){return{items:[],search:null,searched:[],single:null,boolean:!1}},methods:{onSelect:function(e){console.log("ONSELECT"),this.selected=e},searchOnTable:function(){this.searched=d(this.items,this.search)},selectItem:function(e){console.log(e.id),console.log(this.items),console.log(this.selected),console.log(e.selected)}},mounted:function(){var e=this;console.log("BEGINNING"),console.log(this.selected),this.$store.dispatch("loadRelationList",{token:this.$session.get("token"),name:this.relationInfo.name,model:this.relationInfo.model}).then(function(t){e.items=t,e.many||(e.single=t,e.selected=[e.selected]),e.items.forEach(function(t){e.selected.includes(t.id)&&(console.log(t.name),t.selected=!0)})},function(e){}),console.log(this.items)}},m=u,f=(a("25a1"),a("2877")),p=Object(f["a"])(m,i,r,!1,null,"08ec2f2c",null),v=p.exports,b=(o={name:"editForm",props:["showForm","toggleEditForm","formData"]},Object(l["a"])(o,"name","FormValidation"),Object(l["a"])(o,"components",{relationManyEdit:v}),Object(l["a"])(o,"methods",{getFormValues:function(e){console.log("GETFORMVALUE"),console.log(this.$store.getters.formFields)}}),Object(l["a"])(o,"computed",{getForm:function(){return this.$store.getters.formFields}}),o),h=b,g=(a("389c"),Object(f["a"])(h,n,s,!1,null,"55f79148",null));t["a"]=g.exports},bd86:function(e,t,a){"use strict";a.d(t,"a",function(){return s});var o=a("85f2"),n=a.n(o);function s(e,t,a){return t in e?n()(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}},d5e7:function(e,t,a){}}]);
//# sourceMappingURL=chunk-605b28fc.05b1cfc3.js.map