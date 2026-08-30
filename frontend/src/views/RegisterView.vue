<template>
  <AuthCard
    icon="👤"
    title="Create Account"
    subtitle="Get started with your free account"
    :error-message="authStore.error"
  >
    <form @submit.prevent="handleRegister">
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
        autocomplete="new-password"
      />

      <BaseButton type="submit" :loading="authStore.loading">
        Create Account
      </BaseButton>
    </form>

    <template #footer>
      Already have an account?
      <router-link to="/login" class="link">Sign In</router-link>
    </template>
  </AuthCard>
</template>

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

const handleRegister = async () => {
  try {
    await authStore.register(email.value, password.value)
    router.push({ name: 'Dashboard' })
  } catch (err) {}
}
</script>

<style scoped>
.link {
  font-size: 13px;
  color: #2563eb;
  text-decoration: none;
  font-weight: 600;
  margin-left: 4px;
}
.link:hover {
  text-decoration: underline;
}
</style>