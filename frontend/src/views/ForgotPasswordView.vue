<template>
  <div class="auth-wrapper">
    <div class="auth-card">
      <div class="auth-header">
        <div class="logo-icon">🔑</div>
        <h2>Forgot Password?</h2>
        <p>Enter your email and we'll send you a reset link</p>
      </div>

      <form @submit.prevent="handleForgotPassword" class="auth-form">
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

        <div v-if="message" class="success-banner">
          {{ message }}
        </div>

        <div v-if="error" class="error-banner">
          {{ error }}
        </div>

        <button type="submit" class="submit-btn" :disabled="loading">
          <span v-if="!loading">Send Reset Link</span>
          <span v-else class="spinner"></span>
        </button>
      </form>

      <div class="auth-footer">
        Remembered your password?
        <router-link to="/login" class="back-link">Back to Sign In</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import api from '../api/axios'

const email = ref('')
const message = ref('')
const error = ref('')
const loading = ref(false)

const handleForgotPassword = async () => {
  message.value = ''
  error.value = ''
  loading.value = true

  try {
    const response = await api.post('/forgot-password', { email: email.value })
    message.value = response.data.message
  } catch (err) {
    error.value = err.response?.data?.error || 'Failed to send reset link'
  } finally {
    loading.value = false
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

label {
  font-size: 13px;
  font-weight: 600;
  color: #334155;
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

.success-banner {
  background-color: #f0fdf4;
  border: 1px solid #bbf7d0;
  color: #166534;
  padding: 10px 12px;
  border-radius: 6px;
  font-size: 13px;
  text-align: center;
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

.back-link {
  color: #2563eb;
  font-weight: 600;
  text-decoration: none;
  margin-left: 4px;
}

.back-link:hover {
  text-decoration: underline;
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