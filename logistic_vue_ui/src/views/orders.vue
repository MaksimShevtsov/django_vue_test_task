<template>
    <div class="block">
        <div class="title">
        <h3 class="title is-3 has-text-centered">
            Orders
        </h3>
        </div>
        <div class="container">
            <div class="columns">
                <div class="column">
                    <button class="button is-success" @click="showModal()">Add order</button>
                </div>
                <div class="column">
                    <div class="control">
                        <input class="input is-small"
                            v-model="OrderIdFilter"
                            v-on:keyup="FilterFn()"
                            type="text" 
                            placeholder="Find by order id">
                    </div>                    
                </div>
                <div class="column">
                        <span>Sorting by Tracking No</span>

                        <button @click="sortResult('tracking_no',true)" class="button is-small is-white">
                            <img src="https://img.icons8.com/ios-glyphs/15/000000/down--v1.png"/>
                        </button>

                        <button @click="sortResult('tracking_no',false)" class="button is-small is-white">
                            <img src="https://img.icons8.com/ios-glyphs/15/000000/up--v1.png"/>
                        </button>
 
                </div>
            </div> 
        </div>
        <div class="conteiner">
            <table class="table is-striped is-fullwidth">
                <thead>
                    <tr>
                    <th title="ORDER NO.">Order number</th>
                    <th title="CUSTOMER NAME">Customer name</th>
                    <th title="CUSTOMER ID">Customer Id</th>
                    <th title="DELIVERY ADDRESS">Delivery address</th>
                    <th title="SHIPPING METHOD">Shipping method Id</th>
                    <th title="SHIPPING METHOD">Shipping method</th>
                    <th title="SHIPPING DATE">Shipping date</th>
                    <th title="TRACKING NO.">Tracking number</th>
                    <th title="STATUS">Status</th>
                    </tr>
                </thead>
                <tfoot>
                    <tr>
                    <th title="ORDER NO.">Order number</th>
                    <th title="CUSTOMER NAME">Customer name</th>
                    <th title="CUSTOMER ID">Customer Id</th>
                    <th title="DELIVERY ADDRESS">Delivery address</th>
                    <th title="SHIPPING METHOD">Shipping method Id</th>
                    <th title="SHIPPING METHOD">Shipping method</th>
                    <th title="SHIPPING DATE">Shipping date</th>
                    <th title="TRACKING NO.">Tracking number</th>
                    <th title="STATUS">Status</th> 
                    </tr>
                </tfoot>
                <tbody>
                    <tr 
                        v-for="order in orders"
                        v-bind:key="order.id">
                        <td>{{order.order_id}}</td>
                        <td>{{order.customer.customer_name}}</td>
                        <td>{{order.customer.customer_id}}</td>
                        <td>{{order.customer.customer_delivery_address}}</td>
                        <td>{{order.shipping_method.shipping_method_id}}</td>
                        <td>{{order.shipping_method.shipping_method_name}}</td>
                        <td>{{order.shipping_date}}</td>
                        <td>{{order.tracking_no}}</td>
                        <td>{{order.status}}</td>
                        <td><button @click="editClick(order)" class="button is-small is-white">
                            <img src="https://img.icons8.com/ios-glyphs/15/000000/edit--v1.png"/>
                        </button>
                        </td>
                        <td>
                            <button @click="deleteClick(order.order_id)" class="button is-small is-white">
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
                        <p class="modal-card-title">Order</p>
                            <button class="delete" aria-label="close" @click="cancelModal()">></button>
                    </header>
                    <section class="modal-card-body">
                        <div class="input-group py-3">
                            <div class="columns">                                                      
                                <div class="column is-one-fifth"><span class="input-group-text">Customer</span></div>
                                <div class="column">
                                    <div class="select is-normal">
                                        <select v-model="CustomerId">
                                            <option v-for="cust in customers"
                                                    v-bind:key="cust.id">
                                                    {{cust.customer_id}} - {{cust.customer_name}}
                                            </option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                            <div class="columns">                                                      
                                <div class="column is-one-fifth"><span class="input-group-text">Shipping method</span></div>
                                <div class="column">
                                    <div class="select is-normal">
                                        <select v-model="ShippingMethod">
                                            <option v-for="ship in shippingmethods"
                                                    v-bind:key="ship.id">
                                                    {{ship.shipping_method_id}} - {{ship.shipping_method_name}}
                                            </option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="input-group py-3">
                            <span class="input-group-text">Shipping date</span>
                            <input class="input is-primary" type="date" placeholder="Customer name" v-model="ShippingDate">
                        </div>
                        <div class="input-group py-3">
                            <span class="input-group-text">Tracking number</span>
                            <input class="input is-primary" type="text" placeholder="Customer address" v-model="TrackingNumber">
                        </div>
                        <div class="input-group py-3">
                            <span class="input-group-text">Status</span>
                            <input class="input is-primary" type="bool" placeholder="Status" v-model="Status">
                        </div>                            
                    </section>
                <footer class="modal-card-foot">
                    <button class="button is-success" type="button" @click="createClick()" v-if="OrderId==0">Create</button>
                    <button class="button is-success" type="button" @click="updateClick()" v-if="OrderId!=0">Update</button>
                    <button class="button" @click="cancelModal()">Cancel</button>
                </footer>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios"

export default ({
    name: 'Orders',
    
    data() {
        return {
            orders:[],
            shippingmethods:[],
            CustomerId:0,
            CustomerAddr:"",
            showModalFlag: false,
            okPressed: false,
            OrderId:0,
            OrderIdFilter:"",
            ordersWithoutFilter:[],
            ShippingMethod:"",
            ShippingDate:"",
            TrackingNumber:0,
            Status:true
        }
    },

    methods: {
        refreshData(){
            axios.get('/api/v1/orders')
            .then((response)=>{
                this.orders=response.data;
                this.ordersWithoutFilter=response.data;
            });
            axios.get('/api/v1/shipping_methods')
            .then((response)=>{
                this.shippingmethods=response.data;
            });
            axios.get('/api/v1/customers')
            .then((response)=>{
                this.customers=response.data;
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
        axios.post('/api/v1/orders',{
            customer_id:this.CustomerId,
            shipping_method_id:this.ShippingMethod,
            shipping_date:this.ShippingDate,
            tracking_no:this.TrackingNumber,
            status:this.Status
        })
        .then((response)=>{
            this.refreshData();
            alert(response.data);
        });
        },

        editClick(method){
        this.okPressed = false;
        this.showModalFlag = true;
        this.CustomerId=method.customer.customer_id;
        this.ShippingMethod=method.shipping_method.shipping_method_id;
        this.OrderId=method.order_id;
        this.ShippingDate=method.shipping_date;
        this.TrackingNumber=method.tracking_no;
        this.Status=method.status;
        },

        updateClick(){
        this.okPressed = true;
        this.showModalFlag = false;
        axios.put('/api/v1/orders',{
            order_id:this.OrderId,
            shipping_date:this.ShippingDate,
            tracking_no:this.TrackingNumber,
            status:this.Status,
            customer_id:this.CustomerId,
            shipping_method_id:this.ShippingMethod,            
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
        axios.delete("/api/v1/order/"+id)
        .then((response)=>{
            this.refreshData();
            alert(response.data);
        });

        },

        FilterFn(){
            var OrderIdFilter=this.OrderIdFilter;

            this.orders=this.ordersWithoutFilter.filter(
                function(el){
                    return el.order_id.toString().toLowerCase().includes(
                        OrderIdFilter.toString().trim().toLowerCase()
                    )
                });
        },
        sortResult(prop,asc){
            this.orders=this.ordersWithoutFilter.sort(function(a,b){
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