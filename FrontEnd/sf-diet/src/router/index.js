import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/products',
    name: 'products',

    component: () => import(/* webpackChunkName: "products" */ '../views/ProductView.vue'),
    children: [
      {
        path: ':id',
        name: 'products_table',
        component: () => import(/* webpackChunkName: "products_table" */ '../components/ProductTable.vue'),
        props: (route) => ({ query: route.query.q })
      },
      ],
  },
  {
    path: '/add_product',
    name: 'add_product',
    component: () => import (/* webpackChunkName: "add_product" */ '../views/AddProduct.vue')
  },
  {
    path: '/account',
    name: 'account',

    component: () => import('@/views/AccountView.vue'),
    children: [
      {
        path: '/add_data',
        name: 'add_data',
        component: () => import('@/components/AddData.vue')
      }
    ]
  },
  {
    path: '/login',
    name: 'login', 
    component: () => import ('@/views/LoginPage.vue')
  },
  {
    path: '/logout',
    name: 'logout',
    component: () => import ('@/components/LogOut.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
