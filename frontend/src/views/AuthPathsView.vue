<script setup>
import { useAuthStore } from '@/stores/auth';
import ErrorState from '@/components/state-managment/ErrorState.vue';

const authStore = useAuthStore();


</script>

<template>
<div class="auth-paths-container">

  <ErrorState
    v-if="authStore.error"
    :icon="'⚠️'"
    :title="'Authentication Error'"
    :message="authStore.error"
    :actionButtonLabel="'Retry'"
    @action-button-click="authStore.back()"
  />

</div>
</template>

<style scoped>

</style>