import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import { useLocalStorage } from '@vueuse/core'
import { authService } from '@/services/auth'

export const useAuthStore = defineStore('auth', () => {
  const user = useLocalStorage('auth_user', null)
  const token = useLocalStorage('auth_token', null)

  const error = ref('')
  const loading = ref(false)

  const isAuthenticated = computed(() => !!token.value)

  const setAuthData = (data) => {
    token.value = data.token
    user.value = data.user
  }

  const logout = () => {
    token.value = null
    user.value = null
  }

  const register = async (email, password) => {
    loading.value = true
    error.value = ''
    try {
      const data = await authService.register({ email, password })
      setAuthData(data)
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
      const data = await authService.login({ email, password })
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
  }
})