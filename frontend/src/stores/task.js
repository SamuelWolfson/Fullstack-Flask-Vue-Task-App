import { ref } from 'vue'
import { defineStore } from 'pinia'
import { taskService } from '@/services/task'

export const useTaskStore = defineStore('task', () => {
  const tasks = ref([])
  const loading = ref(false)
  const error = ref('')

  const fetchTasks = async () => {
    loading.value = true
    error.value = ''
    try {
      tasks.value = await taskService.getTasks()
    } catch (err) {
      console.error('Error fetching tasks:', err)
      error.value =
        err.response?.data?.error ||
        err.response?.data?.message ||
        'Failed to fetch tasks'
    } finally {
      loading.value = false
    }
  }

  const addTask = async (title) => {
    error.value = ''
    try {
      const newTask = await taskService.createTask(title)
      tasks.value.push(newTask)
    } catch (err) {
      console.error('Error adding task:', err)
      error.value =
        err.response?.data?.error ||
        err.response?.data?.message ||
        'Failed to add task'
    }
  }

  const toggleTask = async (task) => {
    error.value = ''
    try {
      const updatedTask = await taskService.toggleTask(task.id, task.completed)
      const index = tasks.value.findIndex((item) => item.id === task.id)
      if (index > -1) {
        tasks.value[index] = updatedTask
      }
    } catch (err) {
      console.error('Error toggling task:', err)
      error.value =
        err.response?.data?.error ||
        err.response?.data?.message ||
        'Failed to toggle task'
    }
  }

  const updateTask = async (taskId, updates) => {
    error.value = ''
    try {
      const updatedTask = await taskService.updateTask(taskId, updates)
      const index = tasks.value.findIndex((item) => item.id === taskId)
      if (index > -1) {
        tasks.value[index] = updatedTask
      }
    } catch (err) {
      console.error('Error updating task:', err)
      error.value =
        err.response?.data?.error ||
        err.response?.data?.message ||
        'Failed to update task'
    }
  }

  const deleteTask = async (taskId) => {
    error.value = ''
    try {
      await taskService.deleteTask(taskId)
      tasks.value = tasks.value.filter((item) => item.id !== taskId)
    } catch (err) {
      console.error('Error deleting task:', err)
      error.value =
        err.response?.data?.error ||
        err.response?.data?.message ||
        'Failed to delete task'
    }
  }

  return {
    tasks,
    loading,
    error,
    fetchTasks,
    addTask,
    toggleTask,
    updateTask,
    deleteTask,
  }
})