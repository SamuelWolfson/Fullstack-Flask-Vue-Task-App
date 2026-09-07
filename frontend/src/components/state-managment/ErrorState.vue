<script setup>
defineProps({
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
  actionButtonLabel: {
    type: String,
    required: true,
  },
});

const onActionButtonClick = () => {
  emit('action-button-click');
};
</script>

<template>
  <div class="error-state-container">
    <span class="error-icon">{{ icon }}</span>

    <h1 class="error-title">{{ title }}</h1>

    <p class="error-message">{{ message }}</p>

    <button class="action-button" @click="onActionButtonClick">
      {{ actionButtonLabel }}
    </button>
  </div>
</template>

<style scoped></style>
