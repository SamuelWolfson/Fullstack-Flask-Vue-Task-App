<template>
  <div class="auth-container">
    <h2>Register Account</h2>
    <form @submit.prevent="handleRegister">
      <div>
        <label>Email:</label>
        <input v-model="email" type="email" required />
      </div>
      <div>
        <label>Password:</label>
        <input v-model="password" type="password" required />
      </div>
      <p v-if="authStore.error" class="error">{{ authStore.error }}</p>
      <button type="submit" :disabled="authStore.loading">
        {{ authStore.loading ? 'Creating Account...' : 'Register' }}
      </button>
    </form>
    <p>
      Already have an account? <router-link to="/login">Login</router-link>
    </p>
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

const handleRegister = async () => {
  try {
    await authStore.register(email.value, password.value)
    router.push({ name: 'Dashboard' })
  } catch (err) {
    // Error handling managed within the store
  }
}
</script>

<style scoped>
.auth-container {
  max-width: 400px;
  margin: 60px auto;
  padding: 24px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.auth-container form div {
  margin-bottom: 14px;
  display: flex;
  flex-direction: column;
}

.auth-container label {
  font-weight: bold;
  margin-bottom: 4px;
}

.auth-container input {
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.auth-container button {
  width: 100%;
  padding: 10px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

.error {
  color: #d32f2f;
  margin-bottom: 12px;
}
</style>