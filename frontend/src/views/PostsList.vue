<script setup>
import { onMounted, ref } from 'vue'
import { postsAPI } from '@/services/api.js'
import { useRouter } from 'vue-router'

const posts = ref([])
const router = useRouter()

onMounted(async () => {
  const res = await postsAPI.getAll()
  posts.value = res.data.posts
})

// Функция форматирования даты (можно вынести в composable или utils)
const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'short',
    year: 'numeric'
  })
}
</script>

<template>
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10 md:py-12">
    <!-- Заголовок секции (опционально) -->
    <h1 class="text-3xl md:text-4xl font-bold text-center mb-10 text-slate-100">
      Все статьи и гайды
    </h1>

    <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
      <div
        v-for="post in posts"
        :key="post.id"
        @click="router.push(`/posts/${post.id}`)"
        class="
          group
          bg-slate-900/80 backdrop-blur-sm
          border border-slate-800
          rounded-2xl
          overflow-hidden
          shadow-lg
          hover:shadow-2xl
          hover:border-emerald-700/50
          hover:bg-slate-900/90
          transition-all duration-300
          cursor-pointer
        "
      >
        <!-- Тег + дата -->
        <div class="flex items-center justify-between px-5 pt-5 pb-3 text-sm">
          <span
            class="
              px-3 py-1
              text-xs font-medium
              rounded-full
              bg-emerald-900/40
              text-emerald-300
              border border-emerald-800/50
            "
          >
            {{ post.tags?.name || 'Без категории' }}
          </span>

          <span class="text-slate-500">
            {{ formatDate(post.created_at) }}
          </span>
        </div>

        <!-- Заголовок -->
        <h2 class="px-5 pb-2 text-xl font-semibold text-slate-100 group-hover:text-emerald-400 transition-colors">
          {{ post.name || 'Без названия' }}
        </h2>

        <!-- Описание -->
        <p class="px-5 pb-6 text-slate-400 text-sm line-clamp-3 leading-relaxed">
          {{ post.description || 'Описание отсутствует...' }}
        </p>
      </div>
    </div>

    <!-- Пустое состояние (если постов нет) -->
    <div
      v-if="posts.length === 0 && !loading"
      class="text-center py-20 text-slate-500"
    >
      Пока нет ни одной статьи...
    </div>
  </div>
</template>