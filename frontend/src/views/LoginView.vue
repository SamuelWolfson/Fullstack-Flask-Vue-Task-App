<template>
  <div class="auth-wrapper">
    <div class="auth-card">
      <div class="auth-header">
        <div class="logo-icon">✓</div>
        <h2>Welcome Back</h2>
        <p>Sign in to manage your tasks</p>
      </div>

      <form @submit.prevent="handleLogin" class="auth-form">
        <div class="form-group">
          <label for="email">Email address</label>
          <input
            id="email"
            v-model="email"
            type="email"
            placeholder="name@example.com"
            required
            autocomplete="email"
          />
        </div>

        <div class="form-group">
          <div class="label-row">
            <label for="password">Password</label>
            <router-link to="/forgot-password" class="forgot-link">Forgot?</router-link>
          </div>
          <input
            id="password"
            v-model="password"
            type="password"
            placeholder="••••••••"
            required
            autocomplete="current-password"
          />
        </div>

        <div v-if="authStore.error" class="error-banner">
          {{ authStore.error }}
        </div>

        <button type="submit" class="submit-btn" :disabled="authStore.loading">
          <span v-if="!authStore.loading">Sign In</span>
          <span v-else class="spinner"></span>
        </button>
      </form>

      <div class="auth-footer">
        Don't have an account?
        <router-link to="/register" class="signup-link">Create one</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const email = ref('')
const password = ref('')
const authStore = useAuthStore()
const router = useRouter()

const handleLogin = async () => {
  try {
    await authStore.login(email.value, password.value)
    router.push({ name: 'Dashboard' })
  } catch (err) {
    // Error is managed inside Pinia store
  }
}
</script>

<style scoped>
.auth-wrapper {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f8fafc;
  padding: 20px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

.auth-card {
  width: 100%;
  max-width: 400px;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01);
  border: 1px solid #e2e8f0;
  padding: 32px;
}

.auth-header {
  text-align: center;
  margin-bottom: 28px;
}

.logo-icon {
  width: 44px;
  height: 44px;
  background-color: #eff6ff;
  color: #2563eb;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  font-weight: bold;
  margin: 0 auto 16px;
}

.auth-header h2 {
  margin: 0 0 6px;
  color: #0f172a;
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -0.025em;
}

.auth-header p {
  margin: 0;
  color: #64748b;
  font-size: 14px;
}

.auth-form {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.label-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

label {
  font-size: 13px;
  font-weight: 600;
  color: #334155;
}

.forgot-link {
  font-size: 12px;
  color: #2563eb;
  text-decoration: none;
  font-weight: 500;
}

.forgot-link:hover {
  text-decoration: underline;
}

input {
  width: 100%;
  padding: 10px 14px;
  font-size: 14px;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  background-color: #ffffff;
  color: #0f172a;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
  outline: none;
}

input:focus {
  border-color: #2563eb;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
}

input::placeholder {
  color: #94a3b8;
}

.error-banner {
  background-color: #fef2f2;
  border: 1px solid #fecaca;
  color: #dc2626;
  padding: 10px 12px;
  border-radius: 6px;
  font-size: 13px;
  text-align: center;
}

.submit-btn {
  width: 100%;
  padding: 11px;
  background-color: #2563eb;
  color: #ffffff;
  font-size: 14px;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.15s ease;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 4px;
}

.submit-btn:hover:not(:disabled) {
  background-color: #1d4ed8;
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.auth-footer {
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid #f1f5f9;
  text-align: center;
  font-size: 13px;
  color: #64748b;
}

.signup-link {
  color: #2563eb;
  font-weight: 600;
  text-decoration: none;
  margin-left: 4px;
}

.signup-link:hover {
  text-decoration: underline;
}

/* Loading Spinner */
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