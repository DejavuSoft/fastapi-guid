<script setup>
import { ref, computed, nextTick, onUpdated } from 'vue'
import { marked } from 'marked'

const props = defineProps({ markdown: String })
const emit = defineEmits(['copy'])

const codeBlocks = ref([])

const renderer = new marked.Renderer()
renderer.code = (code, infostring) => {
  const lang = (code.lang || 'text').toLowerCase().split(' ')[0]
  const id = `code-${Math.random().toString(36).slice(2)}`
  
  codeBlocks.value.push({ id, code })
  
  const escaped = code.raw
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;')

  return `
    <div class="code-block relative bg-slate-900/90 backdrop-blur-sm border border-slate-700 rounded-xl overflow-hidden my-6" data-id="${id}">
      <div class="flex items-center justify-between bg-slate-800/80 px-4 py-2 border-b border-slate-700">
        <span class="text-xs text-slate-400">${lang}</span>
        <button class="copy-btn text-xs bg-slate-700 hover:bg-emerald-600 px-3 py-1 rounded-md transition-colors" data-id="${id}">
          Копировать
        </button>
      </div>
      <pre class="p-5 overflow-x-auto text-sm"><code class="language-${lang}">${escaped}</code></pre>
    </div>
  `
}

const compiled = computed(() => {
  codeBlocks.value = []
  return marked.parse(props.markdown || '', { renderer })
})

onUpdated(() => {
  nextTick(() => {
    document.querySelectorAll('.copy-btn').forEach(btn => {
      btn.onclick = () => {
        const id = btn.dataset.id
        const block = codeBlocks.value.find(b => b.id === id)
        if (block) {
          navigator.clipboard.writeText(block.code)
          alert('✅ Скопировано!')
        }
      }
    })
  })
})
</script>

<template>
  <article class="prose prose-invert prose-slate max-w-none" v-html="compiled" />
</template>