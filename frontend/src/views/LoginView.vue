<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import AuthCard from '../components/common/AuthCard.vue'
import BaseInput from '../components/common/BaseInput.vue'
import BaseButton from '../components/common/BaseButton.vue'

const email = ref('')
const password = ref('')
const authStore = useAuthStore()
const router = useRouter()

const handleLogin = async () => {
  try {
    await authStore.login(email.value, password.value)
    router.push({ name: 'Dashboard' })
  } catch (err) {}
}
</script>

<template>
  <AuthCard
    icon="✓"
    title="Welcome Back"
    subtitle="Sign in to manage your tasks"
    :error-message="authStore.error"
  >
    <form @submit.prevent="handleLogin">
      <BaseInput
        id="email"
        label="Email address"
        type="email"
        v-model="email"
        placeholder="name@example.com"
        required
        autocomplete="email"
      />

      <BaseInput
        id="password"
        label="Password"
        type="password"
        v-model="password"
        placeholder="••••••••"
        required
        autocomplete="current-password"
      >
        <template #link>
          <router-link to="/forgot-password" class="forgot-link">Forgot?</router-link>
        </template>
      </BaseInput>

      <BaseButton type="submit" :loading="authStore.loading">
        Sign In
      </BaseButton>
    </form>

    <template #footer>
      Don't have an account?
      <router-link to="/register" class="link">Create one</router-link>
    </template>
  </AuthCard>
</template>

<style scoped>
.forgot-link, .link {
  font-size: 12px;
  color: #2563eb;
  text-decoration: none;
  font-weight: 600;
}
.forgot-link:hover, .link:hover {
  text-decoration: underline;
}
</style>