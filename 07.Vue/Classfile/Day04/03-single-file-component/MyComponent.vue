<template>
  <div class="greeting">
    {{ msg }}
  </div>
</template>

<script setup>
// 이제 임포트로 바뀜. 리턴 필요x
import { ref } from "vue";

const msg = ref("hello");
</script>

<style scoped>
.greeting {
  color: red;
}
</style>
