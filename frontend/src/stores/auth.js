import { defineStore } from 'pinia'
import api from '../api/axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: JSON.parse(localStorage.getItem('user')) || null,
    token: localStorage.getItem('token') || null,
    error: null,
    loading: false
  }),
  getters: {
    isAuthenticated: (state) => !!state.token
  },
  actions: {
    async register(email, password) {
      this.loading = true
      this.error = null
      try {
        const response = await api.post('/users', { email, password })
        this.setAuthData(response.data)
      } catch (err) {
        this.error = err.response?.data?.error || 'Registration failed'
        throw err
      } finally {
        this.loading = false
      }
    },

    async login(email, password) {
      this.loading = true
      this.error = null
      try {
        const response = await api.post('/login', { email, password })
        this.setAuthData(response.data)
      } catch (err) {
        this.error = err.response?.data?.error || 'Login failed'
        throw err
      } finally {
        this.loading = false
      }
    },

    setAuthData(data) {
      this.token = data.token
      this.user = data.user
      localStorage.setItem('token', data.token)
      localStorage.setItem('user', JSON.stringify(data.user))
    },

    logout() {
      this.token = null
      this.user = null
      localStorage.removeItem('token')
      localStorage.removeItem('user')
    }
  }
})