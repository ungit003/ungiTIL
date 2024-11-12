<template>
  <div>
    <TodoListItem 
    v-for="todo in store.todos"
    :key="todo.id"
    :todo="todo"
    />
  </div>
</template>

<script setup>
import TodoListItem from '@/components/TodoListItem.vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
// console.log(store.todos)  제대로 가져왔는지 체크

</script>

<style scoped>

</style>