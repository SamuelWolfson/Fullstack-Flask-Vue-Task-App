<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../../stores/auth';

const authStore = useAuthStore();

const email = ref('');

const handleEmailToResetPassword = async () => {
  try {
    await authStore.emailToResetPassword(email.value);
  } catch (err) {}
};
</script>

<template>
  <div class="email-to-reset-password-container">
    <h1>Email to Reset Password</h1>

    <input
      id="email"
      v-model="email"
      type="email"
      placeholder="example@example.com"
    />

    <button @click="handleEmailToResetPassword">Submit</button>
  </div>
</template>

<style scoped></style>
