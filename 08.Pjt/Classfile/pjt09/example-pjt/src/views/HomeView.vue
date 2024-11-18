<template>
  <div>
    <h1>상품 목록 리스트</h1>
    <div class="product-list">
      <div
        v-for="product in store.products"
        :key="product.id"
        class="product-card"
      >
        <img :src="product.image" alt="" class="product-image">
        <div class="product-details">
          <h3>{{  product.title }}</h3>
          <p>가격 : ${{ product.price }}</p>
          <button @click="goDetail(product)">상세 페이지로 이동</button>
          <button @click="addToCart(product)">장바구니로 이동</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCartStore } from '@/stores/cart';
const store = useCartStore()

// API 로 데이터를 다운로드 받아야한다.
// setup 에서 호출하는 게 맞을까?
// 무슨 문제점이 발생할 수 있을까?
// DOM 입장에서 없는 데이터로 화면을 그리려고 시도 할 수 있다.
// setup: DOM이 그려지기 전에 호출
// 데이터 다운로드는 DOM이 그려지고 난 후에 가져오는 걸 권장
import { onMounted } from 'vue';

onMounted(() => {
  store.getProducts()
})

import { useRouter } from 'vue-router';
const router = useRouter()

const goDetail = (product) => {
  router.push(`/${product.id}`)
}

const addToCart = (product) => {
  store.addToCart(product)
  router.push('/cart')
}
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