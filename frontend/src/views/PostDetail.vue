<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { postsAPI } from '@/services/api.js'
import MarkdownRenderer from '@/components/MarkdownRenderer.vue'

const route = useRoute()
const markdown = ref('')
const title = ref('')
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const res = await postsAPI.getById(route.params.id)
    title.value = res.data.name || 'Без названия'
    markdown.value = res.data.content || ''
  } catch (err) {
    console.error('Ошибка загрузки статьи:', err)
    error.value = 'Не удалось загрузить статью'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="min-h-[calc(100vh-8rem)] flex items-start justify-center px-4 py-8 md:py-12 bg-slate-950">
    <!-- Основной контейнер с тенью и эффектом стекла -->
    <div
      class="
        w-full max-w-4xl
        bg-slate-900/70 backdrop-blur-md
        border border-slate-700/50
        rounded-2xl md:rounded-3xl
        shadow-2xl shadow-black/50
        overflow-hidden
        transition-all duration-300
      "
    >
      <!-- Внутренний контент с отступами -->
      <div class="p-6 md:p-10 lg:p-12">
        <!-- Заголовок -->
        <h1
          v-if="!loading && !error"
          class="text-3xl md:text-4xl lg:text-5xl font-bold mb-8 md:mb-10 leading-tight tracking-tight text-slate-50"
        >
          {{ title }}
        </h1>

        <!-- Состояния загрузки / ошибки -->
        <div v-if="loading" class="py-20 text-center text-slate-400">
          <div class="animate-pulse text-lg">Загрузка статьи...</div>
        </div>

        <div v-else-if="error" class="py-20 text-center text-red-400 text-lg">
          {{ error }}
        </div>

        <div v-else-if="!markdown.trim()" class="py-20 text-center text-slate-500 italic">
          Содержимое статьи отсутствует
        </div>

        <!-- Основной контент -->
        <div v-else class="prose prose-invert prose-slate max-w-none prose-headings:scroll-mt-20">
          <MarkdownRenderer :markdown="markdown" />
        </div>
      </div>
    </div>
  </div>
</template>