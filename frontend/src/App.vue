<script setup>
import Header from '@/components/layout/Header.vue'
import Footer from '@/components/layout/Footer.vue'
import { RouterView } from 'vue-router'

</script>

<template>
  <div class="min-h-screen bg-slate-950 text-slate-100 flex flex-col">
    <Header />
    <main class="flex-1">
      <RouterView />
    </main>
    <Footer />
  </div>
</template>