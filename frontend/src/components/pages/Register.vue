<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../../stores/auth';

const authStore = useAuthStore();

const email = ref('');
const password = ref('');

const handleRegister = async () => {
  try {
    await authStore.register(email.value, password.value);
  } catch (err) {}
};
</script>

<template>
  <div class="register-container">
    <h1>Register</h1>

    <input
      id="email"
      type="email"
      v-model="email"
      placeholder="example@example.com"
    />

    <input
      id="password"
      type="password"
      v-model="password"
      placeholder="••••••"
    />

    <button @click="handleRegister">Submit</button>
  </div>
</template>

<style scoped></style>
