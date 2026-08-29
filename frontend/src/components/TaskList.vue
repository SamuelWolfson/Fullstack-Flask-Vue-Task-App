<template>
  <div class="task-list-container">
    <div v-if="taskStore.loading" class="loading">Loading tasks...</div>
    <div v-else-if="taskStore.tasks.length === 0" class="empty">
      No tasks found. Add one above!
    </div>
    <ul v-else class="task-list">
      <TaskItem
        v-for="task in taskStore.tasks"
        :key="task.id"
        :task="task"
      />
    </ul>
  </div>
</template>

<script setup>
import { useTaskStore } from '../stores/task'
import TaskItem from './TaskItem.vue'

const taskStore = useTaskStore()
</script>

<style scoped>
.task-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.loading, .empty {
  text-align: center;
  color: #777;
  padding: 20px 0;
}
</style>