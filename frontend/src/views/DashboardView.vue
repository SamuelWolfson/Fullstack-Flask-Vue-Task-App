<template>
  <div class="dashboard-container">
    <header class="dashboard-header">
      <h2>Task Manager</h2>
      <div class="user-info">
        <span>Logged in as: <strong>{{ authStore.user?.email }}</strong></span>
        <button @click="handleLogout" class="logout-btn">Logout</button>
      </div>
    </header>

    <main class="dashboard-main">
      <TaskForm />
      <TaskList />
    </main>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { useTaskStore } from '../stores/task'

import TaskForm from '../components/TaskForm.vue'
import TaskList from '../components/TaskList.vue'

const authStore = useAuthStore()
const taskStore = useTaskStore()
const router = useRouter()

onMounted(() => {
  taskStore.fetchTasks()
})

const handleLogout = () => {
  authStore.logout()
  router.push({ name: 'Login' })
}
</script>

<style scoped>
.dashboard-container {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  border-bottom: 1px solid #ddd;
  padding-bottom: 10px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logout-btn {
  background-color: #555;
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
}
</style>