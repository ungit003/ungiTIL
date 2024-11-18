import CartView from '@/views/CartView.vue'
import HomeView from '@/views/HomeView.vue'
import ProductDetailView from '@/views/ProductDetailView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: HomeView
    },
    {
      path: '/cart',
      component: CartView
    },
    {
      path: '/:product_id',
      component: ProductDetailView
    }
  ],
})

export default router
