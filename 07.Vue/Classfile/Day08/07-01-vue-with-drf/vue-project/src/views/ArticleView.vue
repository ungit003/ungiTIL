<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink :to="{ name: 'CreateView' }">Create</RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue';

import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()
import { onMounted } from 'vue';
onMounted(() => {
  // mount 되기 전에 store에 있는 전체 게시글 요청 함수를 호출
  store.getArticles()
})


import { RouterLink } from 'vue-router';

</script>

<style>

</style>
