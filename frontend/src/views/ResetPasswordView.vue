<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '../api/axios'
import AuthCard from '../components/common/AuthCard.vue'
import BaseInput from '../components/common/BaseInput.vue'
import BaseButton from '../components/common/BaseButton.vue'

const password = ref('')
const confirmPassword = ref('')
const message = ref('')
const error = ref('')
const loading = ref(false)

const route = useRoute()
const router = useRouter()
const token = route.query.token

const handleResetPassword = async () => {
  message.value = ''
  error.value = ''

  if (password.value !== confirmPassword.value) {
    error.value = 'Passwords do not match'
    return
  }

  loading.value = true

  try {
    const response = await api.post('/reset-password', {
      token,
      password: password.value
    })
    message.value = response.data.message
    setTimeout(() => {
      router.push({ name: 'Login' })
    }, 2000)
  } catch (err) {
    error.value = err.response?.data?.error || 'Failed to reset password'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <AuthCard
    icon="🔒"
    title="Reset Password"
    subtitle="Enter your new password below"
    :error-message="error"
    :success-message="message"
  >
    <form @submit.prevent="handleResetPassword">
      <BaseInput
        id="password"
        label="New Password"
        type="password"
        v-model="password"
        placeholder="••••••••"
        required
        autocomplete="new-password"
      />

      <BaseInput
        id="confirmPassword"
        label="Confirm Password"
        type="password"
        v-model="confirmPassword"
        placeholder="••••••••"
        required
        autocomplete="new-password"
      />

      <BaseButton type="submit" :loading="loading">
        Update Password
      </BaseButton>
    </form>

    <template #footer>
      <router-link to="/login" class="link">Back to Sign In</router-link>
    </template>
  </AuthCard>
</template>

<style scoped>
.link {
  font-size: 13px;
  color: #2563eb;
  text-decoration: none;
  font-weight: 600;
}
.link:hover {
  text-decoration: underline;
}
</style>