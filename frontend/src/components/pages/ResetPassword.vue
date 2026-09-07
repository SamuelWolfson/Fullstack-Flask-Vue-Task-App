<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../../stores/auth';

const authStore = useAuthStore();
const password = ref('');
const confirmPassword = ref('');

const handleResetPassword = async () => {
  try {
    await authStore.resetPassword(password.value, confirmPassword.value);
  } catch (err) {}
};
</script>

<template>
  <div class="reset-password-container">
    <h1>Password Reset</h1>

    <input
      id="password"
      type="password"
      v-model="password"
      placeholder="••••••"
    />

    <input
      id="password"
      type="password"
      v-model="confirmPassword"
      placeholder="••••••"
    />

    <button @click="handleResetPassword">Submit</button>
  </div>
</template>

<style scoped></style>
