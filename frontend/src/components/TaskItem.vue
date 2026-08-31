<script setup>
import { ref } from 'vue';
import { useTaskStore } from '../stores/task';
import BaseButton from './common/BaseButton.vue';
import BaseInput from './common/BaseInput.vue';

const props = defineProps({
  task: {
    type: Object,
    required: true,
  },
});

const taskStore = useTaskStore();
const isEditing = ref(false);
const isDeleting = ref(false);
const isSaving = ref(false);
const editTitle = ref('');

const handleToggle = async () => {
  await taskStore.toggleTask(props.task);
};

const enableEdit = () => {
  editTitle.value = props.task.title;
  isEditing.value = true;
};

const cancelEdit = () => {
  isEditing.value = false;
};

const saveEdit = async () => {
  if (!editTitle.value.trim()) return;
  isSaving.value = true;
  try {
    await taskStore.updateTask(props.task.id, { title: editTitle.value });
    isEditing.value = false;
  } finally {
    isSaving.value = false;
  }
};

const handleDelete = async () => {
  isDeleting.value = true;
  try {
    await taskStore.deleteTask(props.task.id);
  } finally {
    isDeleting.value = false;
  }
};
</script>

<template>
  <div :class="['task-item', { completed: task.completed }]">
    <!-- View Mode -->
    <div v-if="!isEditing" class="task-content">
      <label class="checkbox-container">
        <input
          type="checkbox"
          :checked="task.completed"
          @change="handleToggle"
        />
        <span class="checkmark"></span>
      </label>

      <span class="task-title" @dblclick="enableEdit">
        {{ task.title }}
      </span>

      <div class="task-actions">
        <BaseButton variant="secondary" class="action-btn" @click="enableEdit">
          Edit
        </BaseButton>
        <BaseButton
          variant="danger"
          class="action-btn"
          :loading="isDeleting"
          @click="handleDelete"
        >
          Delete
        </BaseButton>
      </div>
    </div>

    <!-- Edit Mode -->
    <form v-else @submit.prevent="saveEdit" class="edit-form">
      <div class="edit-input-wrapper">
        <BaseInput id="edit-task-input" v-model="editTitle" required />
      </div>
      <div class="edit-actions">
        <BaseButton type="submit" class="action-btn" :loading="isSaving">
          Save
        </BaseButton>
        <BaseButton variant="secondary" class="action-btn" @click="cancelEdit">
          Cancel
        </BaseButton>
      </div>
    </form>
  </div>
</template>

<style scoped>
.task-item {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 12px 16px;
  margin-bottom: 10px;
  transition: all 0.2s ease;
}

.task-content {
  display: flex;
  align-items: center;
  gap: 12px;
}

.checkbox-container {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.checkbox-container input {
  width: 18px;
  height: 18px;
  cursor: pointer;
  accent-color: #2563eb;
}

.task-title {
  flex: 1;
  font-size: 14px;
  color: #0f172a;
  word-break: break-word;
}

.completed .task-title {
  text-decoration: line-through;
  color: #94a3b8;
}

.task-actions,
.edit-actions {
  display: flex;
  gap: 6px;
}

.edit-form {
  display: flex;
  gap: 10px;
  align-items: center;
}

.edit-input-wrapper {
  flex: 1;
}

:deep(.edit-input-wrapper .form-group) {
  margin-bottom: 0;
}

:deep(.action-btn) {
  width: auto;
  padding: 6px 10px;
  font-size: 12px;
}
</style>
