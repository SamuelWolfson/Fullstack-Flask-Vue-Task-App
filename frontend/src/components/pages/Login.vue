<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../../stores/auth';

const authStore = useAuthStore();

const email = ref('');
const password = ref('');

const handleLogin = async () => {
  try {
    await authStore.login(email.value, password.value);
  } catch (err) {}
};
</script>

<template>
  <div class="login-container">
    <h1>Login</h1>

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

    <button @click="handleLogin">Submit</button>
  </div>
</template>

<style scoped></style>
