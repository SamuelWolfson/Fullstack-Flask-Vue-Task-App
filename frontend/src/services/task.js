import api from '@/services/axios'

export const taskService = {
  async getTasks() {
    const response = await api.get('/tasks')
    return response.data
  },

  async createTask(title) {
    const response = await api.post('/tasks', { title })
    return response.data
  },

  async toggleTask(id, completed) {
    const response = await api.patch(`/tasks/${id}`, { completed: !completed })
    return response.data
  },

  async updateTask(id, updates) {
    const response = await api.patch(`/tasks/${id}`, updates)
    return response.data
  },

  async deleteTask(id) {
    await api.delete(`/tasks/${id}`)
  },
}