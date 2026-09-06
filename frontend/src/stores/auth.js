import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import { useLocalStorage } from '@vueuse/core'
import { authService } from '@/services/auth'

export const useAuthStore = defineStore('auth', () => {
  const user = useLocalStorage('auth_user', '')
  const token = useLocalStorage('auth_token', null)

  const error = ref('')
  const loading = ref(false)

  const isAuthenticated = computed(() => !!token.value)

  const setAuthData = (data, email = '') => {
    token.value = data.token
    user.value = data.user?.email || email
  }

  const logout = () => {
    token.value = null
    user.value = ''
  }

  const resetPassword = async (token, newPassword) => {
    loading.value = true
    error.value = ''
    try {
      const data = await authService.resetPassword(token, newPassword)
      return data
    } catch (err) {
      error.value = err.response?.data?.message || 'Failed to reset password'
      throw err
    } finally {
      loading.value = false
    }
  }

  const register = async (email, password) => {
    loading.value = true
    error.value = ''
    try {
      const data = await authService.register({ email, password })
      setAuthData(data, email)
    } catch (err) {
      console.error('Error during registration:', err)
      error.value =
        err.response?.data?.error ||
        err.response?.data?.message ||
        'Registration failed'
      throw err
    } finally {
      loading.value = false
    }
  }

  const login = async (email, password) => {
    loading.value = true
    error.value = ''
    try {
      const data = await authService.login(email, password)
      setAuthData(data)
    } catch (err) {
      console.error('Error during login:', err)
      error.value =
        err.response?.data?.error ||
        err.response?.data?.message ||
        'Login failed'
      throw err
    } finally {
      loading.value = false
    }
  }

  return {
    user,
    token,
    error,
    loading,
    isAuthenticated,
    register,
    login,
    setAuthData,
    logout,
    resetPassword,
  }
})