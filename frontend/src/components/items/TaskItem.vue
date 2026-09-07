<script setup>
const props = defineProps({
  task: {
    type: Object,
    required: true,
  },
});

const handleToggle = () => {
  emit('toggle', props.task.id);
};

const handleDelete = () => {
  emit('delete', props.task.id);
};

const handleEdit = () => {
  emit('edit', props.task.id);
};
</script>

<template>
  <div class="task-item">
    <input type="checkbox" :checked="task.completed" @change="handleToggle" />
    <span :class="{ completed: task.completed }">{{ task.title }}</span>
    <button @click="handleEdit" class="btn btn-edit">Edit</button>
    <button @click="handleDelete" class="btn btn-delete">Delete</button>
  </div>
</template>

<style scoped>

</style>
