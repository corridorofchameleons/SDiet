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
      }],
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
