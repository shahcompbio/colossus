(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-ce450342"],{"25a1":function(e,t,a){"use strict";var n=a("61ce"),s=a.n(n);s.a},3846:function(e,t,a){a("9e1e")&&"g"!=/./g.flags&&a("86cc").f(RegExp.prototype,"flags",{configurable:!0,get:a("0bfb")})},"386d":function(e,t,a){"use strict";var n=a("cb7c"),s=a("83a1"),l=a("5f1b");a("214f")("search",1,function(e,t,a,o){return[function(a){var n=e(this),s=void 0==a?void 0:a[t];return void 0!==s?s.call(a,n):new RegExp(a)[t](String(n))},function(e){var t=o(a,e,this);if(t.done)return t.value;var i=n(e),r=String(this),c=i.lastIndex;s(c,0)||(i.lastIndex=0);var d=l(i,r);return s(i.lastIndex,c)||(i.lastIndex=c),null===d?-1:d.index}]})},"389c":function(e,t,a){"use strict";var n=a("6527"),s=a.n(n);s.a},"3bc3":function(e,t,a){"use strict";var n=a("fb20"),s=a.n(n);s.a},"454f":function(e,t,a){a("46a7");var n=a("584a").Object;e.exports=function(e,t,a){return n.defineProperty(e,t,a)}},"46a7":function(e,t,a){var n=a("63b6");n(n.S+n.F*!a("8e60"),"Object",{defineProperty:a("d9f6").f})},"61ce":function(e,t,a){},6527:function(e,t,a){},"6b54":function(e,t,a){"use strict";a("3846");var n=a("cb7c"),s=a("0bfb"),l=a("9e1e"),o="toString",i=/./[o],r=function(e){a("2aba")(RegExp.prototype,o,e,!0)};a("79e5")(function(){return"/a/b"!=i.call({source:"a",flags:"b"})})?r(function(){var e=n(this);return"/".concat(e.source,"/","flags"in e?e.flags:!l&&e instanceof RegExp?s.call(e):void 0)}):i.name!=o&&r(function(){return i.call(this)})},"83a1":function(e,t){e.exports=Object.is||function(e,t){return e===t?0!==e||1/e===1/t:e!=e&&t!=t}},"85f2":function(e,t,a){e.exports=a("454f")},bbc9:function(e,t,a){"use strict";var n,s=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("md-dialog",{attrs:{"md-active":e.showForm},on:{"update:mdActive":function(t){e.showForm=t},"update:md-active":function(t){e.showForm=t}}},[a("form",{on:{submit:function(t){return t.preventDefault(),e.getFormValues(t)}}},[a("md-card",[a("md-card-header",[a("div",{staticClass:"md-title"},[e._v("create "+e._s(e.$route.params.type))])]),a("md-card-content",[a("md-subheader",[e._v("Relations")]),a("md-list",[e._l(e.formData.relations,function(t,n){return a("md-list-item",{attrs:{"md-expand":""}},[a("span",{staticClass:"md-list-item-text"},[e._v(e._s(n)+e._s(t.many))]),a("md-list",{attrs:{slot:"md-expand"},slot:"md-expand"},[a("relationManyEdit",{attrs:{relationInfo:t,selected:t.selected,many:t.many}})],1)],1)}),a("md-divider"),a("md-subheader",[e._v("Properties ")]),a("md-list-item",{attrs:{"md-expand":""}},[a("span",{staticClass:"md-list-item-text"},[e._v(e._s(e.$route.params.type)+" ")]),a("md-list",{attrs:{slot:"md-expand"},slot:"md-expand"},e._l(e.formData.fields,function(t,n){return a("md-list-item",["Date"!==t.type?a("md-field",[a("label",[e._v(e._s(n))]),"String"===t.type?a("md-input",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"value.value"}}):"Integer"===t.type?a("md-input",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"value.value"}}):"Date"===t.type?a("md-datepicker",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"value.value"}},[a("label",[e._v("Select date")])]):"Select"===t.type?a("md-select",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"value.value"}},e._l(t.choices,function(t){return a("md-option",{attrs:{value:t[0]}},[e._v(e._s(t[1]))])}),1):e._e()],1):"children"!==n&&"Date"===t.type?a("md-datepicker",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"value.value"}},[a("label",[e._v(e._s(n))])]):e._e()],1)}),1)],1),e._l(e.formData.children,function(t,n){return a("md-list-item",{attrs:{"md-expand":""}},[a("span",{staticClass:"md-list-item-text"},[e._v(e._s(n)+" ")]),a("md-list",{attrs:{slot:"md-expand"},slot:"md-expand"},e._l(t,function(t,n){return a("md-list-item",["Date"!==t.type?a("md-field",[a("label",[e._v(e._s(n))]),"String"===t.type?a("md-input",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"v.value"}}):"Integer"===t.type?a("md-input",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"v.value"}}):"Date"===t.type?a("md-datepicker",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"v.value"}},[a("label",[e._v("Select date")])]):"Select"===t.type?a("md-select",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"v.value"}},e._l(t.choices,function(t){return a("md-option",{attrs:{value:t[0]}},[e._v(e._s(t[1]))])}),1):e._e()],1):"Date"===t.type?a("md-datepicker",{model:{value:t.value,callback:function(a){e.$set(t,"value",a)},expression:"v.value"}},[a("label",[e._v(e._s(n))])]):e._e()],1)}),1)],1)})],2)],1),a("md-card-actions",[a("md-button",{attrs:{type:"submit"}},[e._v("Create")]),a("md-button",{on:{click:e.toggleEditForm}},[e._v("Cancer")])],1)],1)],1)])},l=[],o=a("bd86"),i=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("md-table-toolbar",[a("md-field",{staticClass:"md-toolbar-section-end",attrs:{"md-clearable":""}},[a("md-input",{attrs:{placeholder:"Search by name..."},on:{input:e.searchOnTable},model:{value:e.search,callback:function(t){e.search=t},expression:"search"}})],1)],1),a("md-table",{attrs:{id:"choiceTable"},scopedSlots:e._u([{key:"md-table-row",fn:function(t){var n=t.item;return a("md-table-row",{staticClass:"rowitem"},[a("md-table-cell",{attrs:{"md-label":"ID","md-sort-by":"name"}},[a("md-checkbox",{on:{click:function(e){e.stopPropagation()},change:function(t){return t.stopPropagation(),e.selectItem(n)}},model:{value:n.selected,callback:function(t){e.$set(n,"selected",t)},expression:"item.selected"}}),e._v(e._s(n.name)+e._s(n.selected))],1)],1)}}]),model:{value:e.items,callback:function(t){e.items=t},expression:"items"}})],1)},r=[],c=(a("ac6a"),a("386d"),a("7f7f"),a("6762"),a("2fdb"),a("6b54"),function(e){return e.toString().toLowerCase()}),d=function(e,t){return t?e.filter(function(e){return c(e.name).includes(c(t))}):e},u={name:"relationManyEdit",props:["relationInfo","selected","many"],data:function(){return{items:[],search:null,searched:[],single:null,boolean:!1}},methods:{onSelect:function(e){console.log("ONSELECT"),this.selected=e},searchOnTable:function(){this.searched=d(this.items,this.search)},selectItem:function(e){console.log(e.id),console.log(this.items),console.log(this.selected),console.log(e.selected)}},mounted:function(){var e=this;console.log("BEGINNING"),console.log(this.selected),this.$store.dispatch("loadRelationList",{token:this.$session.get("token"),name:this.relationInfo.name,model:this.relationInfo.model}).then(function(t){e.items=t,e.many||(e.single=t,e.selected=[e.selected]),e.items.forEach(function(t){e.selected.includes(t.id)&&(console.log(t.name),t.selected=!0)})},function(e){}),console.log(this.items)}},m=u,f=(a("25a1"),a("2877")),v=Object(f["a"])(m,i,r,!1,null,"08ec2f2c",null),p=v.exports,b=(n={name:"editForm",props:["showForm","toggleEditForm","formData"]},Object(o["a"])(n,"name","FormValidation"),Object(o["a"])(n,"components",{relationManyEdit:p}),Object(o["a"])(n,"methods",{getFormValues:function(e){console.log("GETFORMVALUE"),console.log(this.$store.getters.formFields)}}),Object(o["a"])(n,"computed",{getForm:function(){return this.$store.getters.formFields}}),n),h=b,_=(a("389c"),Object(f["a"])(h,s,l,!1,null,"55f79148",null));t["a"]=_.exports},bd86:function(e,t,a){"use strict";a.d(t,"a",function(){return l});var n=a("85f2"),s=a.n(n);function l(e,t,a){return t in e?s()(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}},c84b:function(e,t,a){"use strict";a.r(t);var n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return null!==e.cardValues?a("div",{staticClass:"detail-wrap"},[a("md-dialog-alert",{attrs:{"md-active":e.deleteAlert,"md-title":"DELETELTELDELDLELTEL!","md-content":"DELETE DELETE DELETE??????DELETE ."},on:{"update:mdActive":function(t){e.deleteAlert=t},"update:md-active":function(t){e.deleteAlert=t}}}),a("editForm",{attrs:{showForm:e.showForm,toggleEditForm:e.toggleEditForm,formData:this.$store.state.model.form_fields}}),a("md-card",{attrs:{"md-with-hover":""}},[a("md-card-header",[a("div",{staticClass:"md-title"},[e._v(e._s(e.$route.params.type.toUpperCase())+"\n      ")])]),e.isEditable?e._e():a("md-card-actions",[a("md-button",{on:{click:e.toggleEditForm}},[e._v("Edit")]),a("md-button",{on:{click:function(t){e.deleteAlert=!0}}},[e._v("Delete")])],1)],1),a("md-card",{attrs:{"md-with-hover":""}},[a("md-card-content",e._l(e.cardParentValues,function(t,n){return a("div",{staticClass:"detail_content"},[a("p",{staticClass:"thick"},[e._v(e._s(n.charAt(0).toUpperCase()+n.slice(1))+": ")]),a("p",[e._v(e._s(t))])])}),0)],1),e._l(e.cardValues,function(t){return a("md-card",{attrs:{"md-with-hover":""}},[a("md-card-header",[a("div",{staticClass:"md-title"},[e._v(e._s(t[0].toUpperCase()))])]),a("md-card-content",e._l(t[1],function(t,n){return a("div",{staticClass:"detail_content"},[a("p",{staticClass:"thick"},[e._v(e._s(n.charAt(0).toUpperCase()+n.slice(1))+": ")]),a("p",[e._v(e._s(t))])])}),0)],1)}),a("br")],2):e._e()},s=[],l=a("bbc9"),o={name:"detail",components:{editForm:l["a"]},data:function(){return{deleteAlert:!1,showForm:!1}},methods:{toggleEditForm:function(){this.showForm=!this.showForm}},mounted:function(){this.$store.dispatch("loadData",{app:this.$route.params.app,type:"detail",pk:this.$route.params.pk,model:this.$route.params.type,token:this.$session.get("token")})},computed:{cardValues:function(){return this.$store.getters.cardValues},cardParentValues:function(){return this.$store.getters.cardParentValues},isEditable:function(){return this.$store.getters.isEditable}}},i=o,r=(a("3bc3"),a("2877")),c=Object(r["a"])(i,n,s,!1,null,"1a3da132",null);t["default"]=c.exports},fb20:function(e,t,a){}}]);
//# sourceMappingURL=chunk-ce450342.870c4253.js.map