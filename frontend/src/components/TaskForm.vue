<template>
  <form @submit.prevent="handleSubmit" class="task-form">
    <input
      v-model="title"
      type="text"
      placeholder="What needs to be done?"
      required
    />
    <button type="submit">Add Task</button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import { useTaskStore } from '../stores/task'

const title = ref('')
const taskStore = useTaskStore()

const handleSubmit = async () => {
  if (!title.value.trim()) return
  await taskStore.addTask(title.value)
  title.value = ''
}
</script>

<style scoped>
.task-form {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

input {
  flex: 1;
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 8px 16px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>