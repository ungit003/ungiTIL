<template>
  <div>
    <p 
    @click="store.updateTodo(todo.id)"
    :class="{ 'is-done': todo.isDone }">{{ todo.text }}</p>
    <button @click="store.deleteTodo(todo.id)">삭제</button>
  </div>
</template>

<script setup>
defineProps({
  todo: Object
})

import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()
</script>

<style scoped>
.is-done {
  text-decoration: line-through;
}
</style>