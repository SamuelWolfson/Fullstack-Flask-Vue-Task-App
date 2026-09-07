<script setup>
const props = defineProps({
  icon: {
    type: String,
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
  message: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <div class="empty-state-container">
    <span class="empty-icon">{{ icon }}</span>

    <h1 class="empty-title">{{ title }}</h1>

    <h2 class="empty-message">{{ message }}</h2>
  </div>
</template>

<style scoped></style>
