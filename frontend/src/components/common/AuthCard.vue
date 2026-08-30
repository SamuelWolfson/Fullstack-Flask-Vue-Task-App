<script setup>
defineProps({
    icon: { type: String, default: '' },
    title: { type: String, default: '' },
    subtitle: { type: String, default: '' },
    errorMessage: { type: String, default: '' },
    successMessage: { type: String, default: '' }
})
</script>

<template>
  <div class="auth-wrapper">
    <div class="auth-card">
      <div v-if="icon || title || subtitle" class="auth-header">
        <div v-if="icon" class="logo-icon">{{ icon }}</div>
        <h2 v-if="title">{{ title }}</h2>
        <p v-if="subtitle">{{ subtitle }}</p>
      </div>

      <div v-if="errorMessage" class="banner error-banner">
        {{ errorMessage }}
      </div>

      <div v-if="successMessage" class="banner success-banner">
        {{ successMessage }}
      </div>

      <slot />

      <div v-if="$slots.footer" class="auth-footer">
        <slot name="footer" />
      </div>
    </div>
  </div>
</template>


<style scoped>
.auth-wrapper {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f8fafc;
  padding: 20px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

.auth-card {
  width: 100%;
  max-width: 400px;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01);
  border: 1px solid #e2e8f0;
  padding: 32px;
}

.auth-header {
  text-align: center;
  margin-bottom: 28px;
}

.logo-icon {
  width: 44px;
  height: 44px;
  background-color: #eff6ff;
  color: #2563eb;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  font-weight: bold;
  margin: 0 auto 16px;
}

.auth-header h2 {
  margin: 0 0 6px;
  color: #0f172a;
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -0.025em;
}

.auth-header p {
  margin: 0;
  color: #64748b;
  font-size: 14px;
}

.banner {
  padding: 10px 12px;
  border-radius: 6px;
  font-size: 13px;
  text-align: center;
  margin-bottom: 18px;
}

.error-banner {
  background-color: #fef2f2;
  border: 1px solid #fecaca;
  color: #dc2626;
}

.success-banner {
  background-color: #f0fdf4;
  border: 1px solid #bbf7d0;
  color: #166534;
}

.auth-footer {
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid #f1f5f9;
  text-align: center;
  font-size: 13px;
  color: #64748b;
}
</style>