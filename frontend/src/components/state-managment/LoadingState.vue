<script setup>
defineProps({
  message: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <div class="loading-state-container">
    <div class="spinner"></div>

    <p>{{ message }}</p>
  </div>
</template>

<style scoped></style>
