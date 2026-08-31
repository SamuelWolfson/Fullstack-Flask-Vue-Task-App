<script setup>
import { computed } from 'vue';
import { useTaskStore } from '../stores/task';
import TaskItem from './TaskItem.vue';

const taskStore = useTaskStore();

const activeTasks = computed(() => {
  return taskStore.tasks.filter((task) => !task.completed);
});

const completedTasks = computed(() => {
  return taskStore.tasks.filter((task) => task.completed);
});
</script>

<template>
  <div class="task-list-wrapper">
    <div v-if="taskStore.loading" class="state-container">
      <div class="spinner"></div>
      <p>Loading tasks...</p>
    </div>

    <div
      v-else-if="taskStore.tasks.length === 0"
      class="state-container empty-state"
    >
      <div class="empty-icon">📝</div>
      <p class="empty-title">No tasks found</p>
      <p class="empty-subtitle">Add a task above to get started!</p>
    </div>

    <div v-else class="tasks-sections">
      <section class="task-group">
        <h3 class="section-title">Active Tasks ({{ activeTasks.length }})</h3>

        <div v-if="activeTasks.length > 0" class="tasks-container">
          <TaskItem v-for="task in activeTasks" :key="task.id" :task="task" />
        </div>
        <p v-else class="empty-group-text">All caught up! No active tasks.</p>
      </section>

      <section
        v-if="completedTasks.length > 0"
        class="task-group completed-group"
      >
        <h3 class="section-title">Completed ({{ completedTasks.length }})</h3>

        <div class="tasks-container completed-list">
          <TaskItem
            v-for="task in completedTasks"
            :key="task.id"
            :task="task"
          />
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.task-list-wrapper {
  margin-top: 16px;
}

.task-group {
  margin-bottom: 24px;
}

.completed-group {
  margin-top: 32px;
  padding-top: 20px;
  border-top: 1px dashed #e2e8f0;
}

.section-title {
  font-size: 12px;
  font-weight: 700;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin: 0 0 12px;
}

.empty-group-text {
  font-size: 13px;
  color: #94a3b8;
  font-style: italic;
  margin: 0;
}

/* Reduced visibility for completed items */
.completed-list :deep(.task-item) {
  opacity: 0.55;
  background-color: #f8fafc;
  border-color: #f1f5f9;
}

.completed-list :deep(.task-item:hover) {
  opacity: 0.9;
}

.state-container {
  text-align: center;
  padding: 40px 20px;
  color: #64748b;
}

.empty-icon {
  font-size: 32px;
  margin-bottom: 8px;
}

.empty-title {
  font-weight: 600;
  color: #334155;
  margin: 0 0 4px;
}

.empty-subtitle {
  font-size: 13px;
  margin: 0;
  color: #94a3b8;
}

.spinner {
  width: 24px;
  height: 24px;
  border: 3px solid #e2e8f0;
  border-radius: 50%;
  border-top-color: #2563eb;
  animation: spin 0.8s linear infinite;
  margin: 0 auto 12px;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
