<script setup>
defineProps({
  type: { type: String, default: 'button' },
  disabled: { type: Boolean, default: false },
  loading: { type: Boolean, default: false },
  variant: { type: String, default: 'primary' },
});

defineEmits(['click']);
</script>

<template>
  <button
    :type="type"
    :disabled="disabled || loading"
    :class="['base-btn', variant]"
    @click="$emit('click', $event)"
  >
    <span v-if="!loading"><slot /></span>
    <span v-else class="spinner"></span>
  </button>
</template>

<style scoped>
.base-btn {
  width: 100%;
  padding: 11px;
  font-size: 14px;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.15s ease;
  display: flex;
  justify-content: center;
  align-items: center;
}

.primary {
  background-color: #2563eb;
  color: #ffffff;
}

.primary:hover:not(:disabled) {
  background-color: #1d4ed8;
}

.secondary {
  background-color: #64748b;
  color: #ffffff;
}

.secondary:hover:not(:disabled) {
  background-color: #475569;
}

.danger {
  background-color: #dc2626;
  color: #ffffff;
}

.danger:hover:not(:disabled) {
  background-color: #b91c1c;
}

.base-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.spinner {
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top-color: #ffffff;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
