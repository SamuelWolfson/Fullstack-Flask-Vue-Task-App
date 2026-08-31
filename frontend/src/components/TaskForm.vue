<script setup>
import { ref } from 'vue';
import { useTaskStore } from '../stores/task';
import BaseInput from './common/BaseInput.vue';
import BaseButton from './common/BaseButton.vue';

const title = ref('');
const loading = ref(false);
const taskStore = useTaskStore();

const handleSubmit = async () => {
  if (!title.value.trim()) return;
  loading.value = true;
  try {
    await taskStore.addTask(title.value);
    title.value = '';
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <form @submit.prevent="handleSubmit" class="task-form">
    <div class="input-wrapper">
      <BaseInput
        id="task-title"
        v-model="title"
        placeholder="What needs to be done?"
        required
      />
    </div>
    <BaseButton type="submit" :loading="loading"> Add Task </BaseButton>
  </form>
</template>

<style scoped>
.task-form {
  display: flex;
  gap: 12px;
  align-items: flex-start;
  margin-bottom: 24px;
}

.input-wrapper {
  flex: 1;
}

/* Override BaseInput default bottom margin for inline layout */
:deep(.form-group) {
  margin-bottom: 0;
}

:deep(.base-btn) {
  width: auto;
  white-space: nowrap;
  padding: 10px 20px;
}
</style>
