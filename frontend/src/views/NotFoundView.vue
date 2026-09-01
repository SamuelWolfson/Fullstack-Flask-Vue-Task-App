<script setup>
import { useRouter } from 'vue-router';
import BaseButton from '../components/common/BaseButton.vue';

const router = useRouter();

const goHome = () => {
  router.push({ name: 'Dashboard' });
};
</script>

<template>
  <div class="not-found-container">
    <div class="not-found-card">
      <h1 class="error-code">404</h1>
      <h2 class="title">העמוד לא נמצא</h2>
      <p class="description">
        מצטערים, העמוד שחיפשת אינו קיים או שהועבר לכתובת אחרת
      </p>

      <BaseButton variant="primary" @click="goHome">
        חזרה ללוח הבקרה
      </BaseButton>
    </div>
  </div>
</template>

<style scoped>
.not-found-container {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 80vh;
  padding: 1.5rem;
}

.not-found-card {
  text-align: center;
  max-width: 400px;
  width: 100%;
}

.error-code {
  font-size: 5rem;
  font-weight: 800;
  margin: 0;
  color: #3b82f6;
  line-height: 1;
}

.title {
  font-size: 1.5rem;
  font-weight: 600;
  margin-top: 1rem;
  margin-bottom: 0.5rem;
}

.description {
  color: #6b7280;
  margin-bottom: 1.5rem;
}
</style>
