<template>
    <div class="block">
        <div class="title">
            <h3 class="title is-3 has-text-centered">
                Shipping method
            </h3>
        </div>
        <div class="content">
        
            <button class="button is-success" @click="showModal()">Add shipping method</button>
       
        </div>
        <div class="conteiner">
            <table class="table table is-hoverable">
                <thead>
                    <tr>
                    <th title="SHIPPING ID.">
                        <div class="field has-addons">
                            <div class="control">
                                <input class="input is-small"
                                    v-model="ShippingIdFilter"
                                    v-on:keyup="FilterFn()"
                                    type="text" 
                                    placeholder="Find by id">
                            </div>
                            <div>
                                <button @click="sortResult('shipping_method_id',true)" class="button is-small is-white">
                                    <img src="https://img.icons8.com/ios-glyphs/15/000000/down--v1.png"/>
                                </button>
                            </div>
                            <div>
                                <button @click="sortResult('shipping_method_id',false)" class="button is-small is-white">
                                    <img src="https://img.icons8.com/ios-glyphs/15/000000/up--v1.png"/>
                                </button>
                            </div>
                        </div>
                        Method Id</th>
                    <th title="SHIPPING METHOD">
                        <div class="field has-addons">
                           <div class="control">
                                <input class="input is-small"
                                    v-model="ShippingNameFilter"
                                    v-on:keyup="FilterFn()"
                                    type="text" 
                                    placeholder="Find by method">
                            </div>
                            <div class="block">
                                <button @click="sortResult('shipping_method_name',true)" class="button is-small is-white">
                                    <img src="https://img.icons8.com/ios-glyphs/15/000000/down--v1.png"/>
                                </button>
                            </div>
                            <div>
                                <button @click="sortResult('shipping_method_name',false)" class="button is-small is-white">
                                    <img src="https://img.icons8.com/ios-glyphs/15/000000/up--v1.png"/>
                                </button>
                            </div>
                        </div>
                        Shipping method</th>
                    </tr>
                </thead>
                <tbody>
                    <tr 
                        v-for="method in shippingmethods"
                        v-bind:key="method.id">
                        <td>{{method.shipping_method_id}}</td>
                        <td>{{method.shipping_method_name}}</td>
                        <td><button @click="editClick(method)" class="button is-small is-white">
                            <img src="https://img.icons8.com/ios-glyphs/15/000000/edit--v1.png"/>
                        </button>
                        </td>
                        <td>
                            <button @click="deleteClick(method.shipping_method_id)" class="button is-small is-white">
                                <img src="https://img.icons8.com/ios-glyphs/15/000000/delete-sign.png"/>
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="modal" :class="{'is-active': showModalFlag}">
            <div class="modal-background"></div>
                <div class="modal-card">
                    <header class="modal-card-head">
                        <p class="modal-card-title">Shipping method</p>
                            <button class="delete" aria-label="close" @click="cancelModal()">></button>
                    </header>
                    <section class="modal-card-body">
                        <div class="input-group mb-3">
                            <span class="input-group-text"> Shipping method</span>
                            <input class="input is-primary" type="text" placeholder="New shipping method" v-model="ShippingMethodName">
                        </div>                       
                    </section>
                <footer class="modal-card-foot">
                    <button class="button is-success" type="button" @click="createClick()" v-if="ShippingMethodId==0">Create</button>
                    <button class="button is-success" type="button" @click="updateClick()" v-if="ShippingMethodId!=0">Update</button>
                    <button class="button" @click="cancelModal()">Cancel</button>
                </footer>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios"

export default ({
    name: 'Shipping',
    
    data() {
        return {
            shippingmethods:{},
            showModalFlag: false,
            okPressed: false,
            ShippingMethodId:0,
            ShippingMethodNameFilter:"",
            ShippingMethodIdFilter:"",
            shipmentsWithoutFilter:{}
        }
    },

    methods: {
        refreshData(){
            axios.get('/api/v1/shipping_methods')
            .then((response)=>{
                this.shippingmethods=response.data;
                this.shipmentsWithoutFilter=response.data;
            });
        },

        showModal() {
        this.okPressed = false;
        this.showModalFlag = true;
        },

        okModal() {
        this.okPressed = true;
        this.showModalFlag = false;
        },

        cancelModal() {
        this.okPressed = false;
        this.showModalFlag = false;
        },

        createClick(){
        this.okPressed = true;
        this.showModalFlag = false;
        axios.post('/api/v1/shipping_methods',{
            shipping_method_name:this.ShippingMethodName
        })
        .then((response)=>{
            this.refreshData();
            alert(response.data);
        });
        },

        editClick(method){
        this.okPressed = false;
        this.showModalFlag = true;
        this.modalTitle="Edit shipping method";
        this.ShippingMethodId=method.shipping_method_id;
        this.ShippingMethodName=method.shipping_method_name;
        },

        updateClick(){
        this.okPressed = true;
        this.showModalFlag = false;
        axios.put('/api/v1/shipping_methods',{
            shipping_method_id:this.ShippingMethodId,
            shipping_method_name:this.ShippingMethodName
        })
        .then((response)=>{
            this.refreshData();
            alert(response.data);
        });
        },

        deleteClick(id){
        if(!confirm("Are you sure?")){
            return;
        }
        axios.delete("/api/v1/shipping_method/"+id)
        .then((response)=>{
            this.refreshData();
            alert(response.data);
        });

        },

        FilterFn(){
            var ShippingMethodIdFilter=this.ShippingIdFilter;
            var ShippingMethodNameFilter=this.ShippingNameFilter;

            this.shippingmethods=this.shipmentsWithoutFilter.filter(
                function(el){
                    return el.shipping_method_id.toString().toLowerCase().includes(
                        ShippingMethodIdFilter.toString().trim().toLowerCase()
                    )&&
                    el.shipping_method_name.toString().toLowerCase().includes(
                        ShippingMethodNameFilter.toString().trim().toLowerCase()
                    )
                });
        },
        sortResult(prop,asc){
            this.shippingmethods=this.shipmentsWithoutFilter.sort(function(a,b){
                if(asc){
                    return (a[prop]>b[prop])?1:((a[prop]<b[prop])?-1:0);
                }
                else{
                    return (b[prop]>a[prop])?1:((b[prop]<a[prop])?-1:0);
                }
            })
        }
    },
    mounted:function(){
        this.refreshData();
    }

})
</script>
