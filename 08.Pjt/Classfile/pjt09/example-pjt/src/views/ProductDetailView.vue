<template>
  <div>
    <h1>상세 페이지</h1>
    <div v-if="product">
      <img :src="product.image" alt="">
      <h3>{{ product.title }}</h3>
      <p>가격 : {{ product.price }}</p>
      <p>카테고리 : {{ product.category }}</p>
    </div>
    <div v-else>
      <p>Loading ... </p>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
const route = useRoute()
const productId = route.params.product_id


import { useCartStore } from '@/stores/cart';
const store = useCartStore()
const product = store.getProductById(productId)

console.log('product in component =', product)

</script>

<style scoped>
.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.product-card {
  border: 1px solid black;
  width: 200px;
  padding: 15px;
}

.product-image {
  width: 100%;
}

.product-details {
  text-align: center;
}
</style>