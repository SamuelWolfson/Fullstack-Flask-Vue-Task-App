<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import { useTaskStore } from '../stores/task';

import BaseButton from '../components/common/BaseButton.vue';
import TaskForm from '../components/TaskForm.vue';
import TaskList from '../components/TaskList.vue';

const authStore = useAuthStore();
const taskStore = useTaskStore();
const router = useRouter();

onMounted(() => {
  taskStore.fetchTasks();
});

const handleLogout = () => {
  authStore.logout();
  router.push({ name: 'Login' });
};
</script>

<template>
  <div class="dashboard-wrapper">
    <div class="dashboard-card">
      <header class="dashboard-header">
        <div class="header-title">
          <div class="logo-icon">✓</div>
          <h2>Task Manager</h2>
        </div>
        <div class="user-info">
          <span>{{ authStore.user?.email }}</span>
          <BaseButton
            variant="secondary"
            @click="handleLogout"
            class="logout-btn"
          >
            Logout
          </BaseButton>
        </div>
      </header>

      <main class="dashboard-main">
        <TaskForm />
        <TaskList />
      </main>
    </div>
  </div>
</template>

<style scoped>
.dashboard-wrapper {
  min-height: 100vh;
  background-color: #f8fafc;
  padding: 40px 20px;
  display: flex;
  justify-content: center;
  font-family:
    -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial,
    sans-serif;
}

.dashboard-card {
  width: 100%;
  max-width: 600px;
  background: #ffffff;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
  padding: 32px;
  align-self: flex-start;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 1px solid #f1f5f9;
}

.header-title {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo-icon {
  width: 36px;
  height: 36px;
  background-color: #eff6ff;
  color: #2563eb;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

.header-title h2 {
  margin: 0;
  font-size: 20px;
  color: #0f172a;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 13px;
  color: #64748b;
  font-weight: 500;
}

:deep(.logout-btn) {
  width: auto;
  padding: 6px 12px;
  font-size: 13px;
}
</style>
