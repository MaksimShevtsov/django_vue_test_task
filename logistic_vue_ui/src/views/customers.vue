<template>
    <div class="block">
        <div class="title">
            <h3 class="title is-3 has-text-centered">
                Customers
            </h3>
        </div>
        <div class="content">
        
            <button class="button is-success" @click="showModal()">Add customer</button>
       
        </div>
        <div class="conteiner">
            <table class="table table is-hoverable">
                <thead>
                    <tr>
                    <th title="CUSTOMER ID">
                        <div class="field has-addons">
                            <div class="control">
                                <input class="input is-small"
                                    v-model="CustomerIdFilter"
                                    v-on:keyup="FilterFn()"
                                    type="text" 
                                    placeholder="Find by id">
                            </div>
                            <div>
                                <button @click="sortResult('customer_id',true)" class="button is-small is-white">
                                    <img src="https://img.icons8.com/ios-glyphs/15/000000/down--v1.png"/>
                                </button>
                            </div>
                            <div>
                                <button @click="sortResult('customer_id',false)" class="button is-small is-white">
                                    <img src="https://img.icons8.com/ios-glyphs/15/000000/up--v1.png"/>
                                </button>
                            </div>
                        </div>
                        Customer Id</th>
                    <th title="CUSTOMER NAME">
                        <div class="field has-addons">
                           <div class="control">
                                <input class="input is-small"
                                    v-model="CustomerNameFilter"
                                    v-on:keyup="FilterFn()"
                                    type="text" 
                                    placeholder="Find by name">
                            </div>
                            <div class="block">
                                <button @click="sortResult('customer_name',true)" class="button is-small is-white">
                                    <img src="https://img.icons8.com/ios-glyphs/15/000000/down--v1.png"/>
                                </button>
                            </div>
                            <div>
                                <button @click="sortResult('customer_name',false)" class="button is-small is-white">
                                    <img src="https://img.icons8.com/ios-glyphs/15/000000/up--v1.png"/>
                                </button>
                            </div>
                        </div>
                        Customer name</th>
                    <th title="CUSTOMER ADDRESS">
                        <div class="field has-addons">
                           <div class="control">
                                <input class="input is-small"
                                    v-model="CustomerAddFilter"
                                    v-on:keyup="FilterFn()"
                                    type="text" 
                                    placeholder="Find by address">
                            </div>
                            <div class="block">
                                <button @click="sortResult('customer_delivery_address',true)" class="button is-small is-white">
                                    <img src="https://img.icons8.com/ios-glyphs/15/000000/down--v1.png"/>
                                </button>
                            </div>
                            <div>
                                <button @click="sortResult('customer_delivery_address',false)" class="button is-small is-white">
                                    <img src="https://img.icons8.com/ios-glyphs/15/000000/up--v1.png"/>
                                </button>
                            </div>
                        </div>
                        Delivery address</th>
                    </tr>
                </thead>
                <tbody>
                    <tr 
                        v-for="customer in customers"
                        v-bind:key="customer.id">
                        <td>{{customer.customer_id}}</td>
                        <td>{{customer.customer_name}}</td>
                        <td>{{customer.customer_delivery_address}}</td>
                        <td><button @click="editClick(customer)" class="button is-small is-white">
                            <img src="https://img.icons8.com/ios-glyphs/15/000000/edit--v1.png"/>
                        </button>
                        </td>
                        <td>
                            <button @click="deleteClick(customer.customer_id)" class="button is-small is-white">
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
                        <p class="modal-card-title">Customer</p>
                            <button class="delete" aria-label="close" @click="cancelModal()">></button>
                    </header>
                    <section class="modal-card-body">
                        <div class="input-group mb-3">
                            <span class="input-group-text">Name</span>
                            <input class="input is-primary" type="text" placeholder="Customer name" v-model="CustomerName">
                        </div>
                        <div class="input-group mb-3">
                            <span class="input-group-text">Address</span>
                            <input class="input is-primary" type="text" placeholder="Customer address" v-model="CustomerAddr">
                        </div>                         
                    </section>
                <footer class="modal-card-foot">
                    <button class="button is-success" type="button" @click="createClick()" v-if="CustomerId==0">Create</button>
                    <button class="button is-success" type="button" @click="updateClick()" v-if="CustomerId!=0">Update</button>
                    <button class="button" @click="cancelModal()">Cancel</button>
                </footer>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios"

export default ({
    name: 'Customers',
    
    data() {
        return {
            customers:{},
            CustomerAddr:"",
            showModalFlag: false,
            okPressed: false,
            CustomerId:0,
            CustomerNameFilter:"",
            CustomerIdFilter:"",
            CustomerAddFilter:"",
            customersWithoutFilter:{}
        }
    },

    methods: {
        refreshData(){
            axios.get('/api/v1/customers')
            .then((response)=>{
                this.customers=response.data;
                this.customersWithoutFilter=response.data;
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
        axios.post('/api/v1/customers',{
            customer_name:this.CustomerName,
            customer_delivery_address:this.CustomerAddr
        })
        .then((response)=>{
            this.refreshData();
            alert(response.data);
        });
        },

        editClick(method){
        this.okPressed = false;
        this.showModalFlag = true;
        this.CustomerId=method.customer_id;
        this.CustomerName=method.customer_name;
        this.CustomerAddr=method.customer_delivery_address;
        },

        updateClick(){
        this.okPressed = true;
        this.showModalFlag = false;
        axios.put('/api/v1/customers',{
            customer_id:this.CustomerId,
            customer_name:this.CustomerName,
            customer_delivery_address:this.CustomerAddr
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
        axios.delete("/api/v1/customer/"+id)
        .then((response)=>{
            this.refreshData();
            alert(response.data);
        });

        },

        FilterFn(){
            var CustomersIdFilter=this.CustomerIdFilter;
            var CustomersNameFilter=this.CustomerNameFilter;
            var CustomerAddFilter=this.CustomerAddFilter;

            this.customers=this.customersWithoutFilter.filter(
                function(el){
                    return el.customer_id.toString().toLowerCase().includes(
                        CustomersIdFilter.toString().trim().toLowerCase()
                    )&&
                    el.customer_name.toString().toLowerCase().includes(
                        CustomersNameFilter.toString().trim().toLowerCase()
                    )&&
                    el.customer_delivery_address.toString().toLowerCase().includes(
                        CustomerAddFilter.toString().trim().toLowerCase()
                    )
                });
        },
        sortResult(prop,asc){
            this.customers=this.customersWithoutFilter.sort(function(a,b){
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
