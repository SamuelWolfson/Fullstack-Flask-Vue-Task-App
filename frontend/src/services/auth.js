import api from '@/services/axios'

export const authService = {
  async login(email, password) {
    const response = await api.post('/login', { email, password })
    return response.data
  },

  async register(userData) {
    const response = await api.post('/users', userData)
    return response.data
  },

  async resetPassword(token, newPassword) {
  const response = await api.post('/reset-password', { token, password: newPassword })
  return response.data
  },
}