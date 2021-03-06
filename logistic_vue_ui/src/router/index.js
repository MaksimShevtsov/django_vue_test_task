import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Customers from '../views/customers.vue'
import Shipping from '../views/shippingmethods.vue'
import Orders from '../views/orders.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/customers',
    name: 'customers',
    component: Customers
  },
  {
    path: '/shippingmethods',
    name: 'shippingmethods',
    component: Shipping
  },
  {
    path: '/orders',
    name: 'orders',
    component: Orders
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
