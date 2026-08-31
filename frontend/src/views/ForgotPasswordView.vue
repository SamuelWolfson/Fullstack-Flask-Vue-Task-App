<script setup>
import { ref } from 'vue';
import api from '../api/axios';
import AuthCard from '../components/common/AuthCard.vue';
import BaseInput from '../components/common/BaseInput.vue';
import BaseButton from '../components/common/BaseButton.vue';

const email = ref('');
const message = ref('');
const error = ref('');
const loading = ref(false);

const handleForgotPassword = async () => {
  message.value = '';
  error.value = '';
  loading.value = true;

  try {
    const response = await api.post('/forgot-password', { email: email.value });
    message.value = response.data.message;
  } catch (err) {
    error.value = err.response?.data?.error || 'Failed to send reset link';
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <AuthCard
    icon="🔑"
    title="Forgot Password?"
    subtitle="Enter your email to receive a reset link"
    :error-message="error"
    :success-message="message"
  >
    <form @submit.prevent="handleForgotPassword">
      <BaseInput
        id="email"
        label="Email address"
        type="email"
        v-model="email"
        placeholder="name@example.com"
        required
        autocomplete="email"
      />

      <BaseButton type="submit" :loading="loading">
        Send Reset Link
      </BaseButton>
    </form>

    <template #footer>
      Remembered your password?
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
  margin-left: 4px;
}
.link:hover {
  text-decoration: underline;
}
</style>
