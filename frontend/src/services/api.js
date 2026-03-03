import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/'

const apiClient = axios.create({
    baseURL: API_BASE_URL,
    headers: {
      'Content-Type': 'application/json',
    },
  })

export const postsAPI = {
    getAll() {
        return apiClient.get('/api/posts')
    },

    getById(id) {
        return apiClient.get(`/api/posts/${id}`)
    },
}

export default apiClient