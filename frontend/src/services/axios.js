import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:5000',
  headers: {
    'Content-Type': 'application/json',
  },
})

api.interceptors.request.use(
  (config) => {
    let token = localStorage.getItem('auth_token')
    if (token) {
      try {
        token = JSON.parse(token)
      } catch (e) {
        token = token.replace(/^"(.*)"$/, '$1')
      }
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

export default api