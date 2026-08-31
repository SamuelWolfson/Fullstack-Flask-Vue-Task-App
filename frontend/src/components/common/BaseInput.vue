<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  id: { type: String, required: true },
  label: { type: String, default: '' },
  type: { type: String, default: 'text' },
  modelValue: { type: String, default: '' },
  placeholder: { type: String, default: '' },
  required: { type: Boolean, default: false },
  autocomplete: { type: String, default: 'off' }
})

defineEmits(['update:modelValue'])

const showPassword = ref(false)

const computedType = computed(() => {
  if (props.type === 'password') {
    return showPassword.value ? 'text' : 'password'
  }
  return props.type
})
</script>

<template>
  <div class="form-group">
    <div class="label-row" v-if="label || $slots.link">
      <label v-if="label" :for="id" class="form-label">{{ label }}</label>
      <slot name="link"></slot>
    </div>
    
    <div class="input-wrapper">
      <input
        :id="id"
        :type="computedType"
        :value="modelValue"
        :placeholder="placeholder"
        :required="required"
        :autocomplete="autocomplete"
        class="form-input"
        @input="$emit('update:modelValue', $event.target.value)"
      />

      <button
        v-if="type === 'password'"
        type="button"
        class="toggle-password-btn"
        @click="showPassword = !showPassword"
      >
        <svg
          v-if="showPassword"
          xmlns="http://www.w3.org/2000/svg"
          width="18"
          height="18"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z" />
          <circle cx="12" cy="12" r="3" />
        </svg>

        <svg
          v-else
          xmlns="http://www.w3.org/2000/svg"
          width="18"
          height="18"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path d="M9.88 9.88a3 3 0 1 0 4.24 4.24" />
          <path d="M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68" />
          <path d="M6.61 6.61A13.52 13.52 0 0 0 2 12s3 7 10 7a9.74 9.74 0 0 0 5.39-1.61" />
          <line x1="2" x2="22" y1="2" y2="22" />
        </svg>
      </button>
    </div>
  </div>
</template>

<style scoped>
.form-group {
  margin-bottom: 16px;
  display: flex;
  flex-direction: column;
}

.label-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
}

.form-label {
  font-size: 14px;
  font-weight: 500;
  color: #334155;
  margin-bottom: 0;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.form-input {
  width: 100%;
  padding: 10px 40px 10px 12px;
  font-size: 14px;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  outline: none;
  transition: border-color 0.2s;
}

.form-input:focus {
  border-color: #2563eb;
}

.toggle-password-btn {
  position: absolute;
  right: 10px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #64748b;
  transition: color 0.2s;
}

.toggle-password-btn:hover {
  color: #1e293b;
}
</style>