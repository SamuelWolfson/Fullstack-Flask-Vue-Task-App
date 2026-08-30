<script setup>
defineProps({
id: { type: String, required: true },
label: { type: String, default: '' },
type: { type: String, default: 'text' },
modelValue: { type: [String, Number], default: '' },
placeholder: { type: String, default: '' },
required: { type: Boolean, default: false },
autocomplete: { type: String, default: 'off' }
})

defineEmits(['update:modelValue'])
</script>

<template>
  <div class="form-group">
    <div class="label-row" v-if="label || $slots.link">
      <label :for="id">{{ label }}</label>
      <slot name="link" />
    </div>
    <input
      :id="id"
      :type="type"
      :value="modelValue"
      :placeholder="placeholder"
      :required="required"
      :autocomplete="autocomplete"
      @input="$emit('update:modelValue', $event.target.value)"
    />
  </div>
</template>

<style scoped>
.form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 18px;
}

.label-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

label {
  font-size: 13px;
  font-weight: 600;
  color: #334155;
}

input {
  width: 100%;
  padding: 10px 14px;
  font-size: 14px;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  background-color: #ffffff;
  color: #0f172a;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
  outline: none;
}

input:focus {
  border-color: #2563eb;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
}

input::placeholder {
  color: #94a3b8;
}
</style>