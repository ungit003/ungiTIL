<template>
  <div>
    <nav>
      <RouterLink to="/">Home</RouterLink> |
      <RouterLink to="/cart">Cart</RouterLink>
    </nav>
  </div>
</template>

<script setup>
// setup: Vue 라이프 사이클
// Setup: 최초 세팅
// Mount: DOM 이 그려진 후
// Update: 호면 완성 후 데이터 변경 시
// UnMount: 다른 컴포넌트 이동 시
import { RouterLink } from 'vue-router';
</script>
