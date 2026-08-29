import { defineStore } from 'pinia'
import api from '../api/axios'

export const useTaskStore = defineStore('task', {
  state: () => ({
    tasks: [],
    loading: false,
    error: null
  }),
  actions: {
    async fetchTasks() {
      this.loading = true
      try {
        const response = await api.get('/tasks')
        this.tasks = response.data
      } catch (err) {
        this.error = err.response?.data?.error || 'Failed to fetch tasks'
      } finally {
        this.loading = false
      }
    },

    async addTask(title) {
      try {
        const response = await api.post('/tasks', { title })
        this.tasks.push(response.data)
      } catch (err) {
        this.error = err.response?.data?.error || 'Failed to add task'
      }
    },

    async toggleTask(task) {
      try {
        const response = await api.patch(`/tasks/${task.id}`, {
          completed: !task.completed
        })
        const index = this.tasks.findIndex((t) => t.id === task.id)
        if (index !== -1) {
          this.tasks[index] = response.data
        }
      } catch (err) {
        this.error = err.response?.data?.error || 'Failed to update task'
      }
    },

    async deleteTask(taskId) {
      try {
        await api.delete(`/tasks/${taskId}`)
        this.tasks = this.tasks.filter((t) => t.id !== taskId)
      } catch (err) {
        this.error = err.response?.data?.error || 'Failed to delete task'
      }
    }
  }
})