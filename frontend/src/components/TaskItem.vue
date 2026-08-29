<template>
  <li class="task-item">
    <span :class="{ completed: task.completed }">
      {{ task.title }}
    </span>
    <div class="actions">
      <button @click="taskStore.toggleTask(task)" class="toggle-btn">
        {{ task.completed ? 'Undo' : 'Complete' }}
      </button>
      <button @click="taskStore.deleteTask(task.id)" class="delete-btn">
        Delete
      </button>
    </div>
  </li>
</template>

<script setup>
import { useTaskStore } from '../stores/task'

defineProps({
  task: {
    type: Object,
    required: true
  }
})

const taskStore = useTaskStore()
</script>

<style scoped>
.task-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #eee;
}

.completed {
  text-decoration: line-through;
  color: #888;
}

.actions {
  display: flex;
  gap: 6px;
}

.toggle-btn {
  background-color: #2196f3;
  color: white;
  border: none;
  padding: 4px 8px;
  border-radius: 4px;
  cursor: pointer;
}

.delete-btn {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 4px 8px;
  border-radius: 4px;
  cursor: pointer;
}
</style>