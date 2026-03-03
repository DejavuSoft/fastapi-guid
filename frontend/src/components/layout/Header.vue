<template>
    <header class="bg-slate-900/90 backdrop-blur-md border-b border-slate-800 sticky top-0 z-10">
      <div class="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
        
        <!-- Логотип / название проекта -->
        <router-link to="/" class="text-xl md:text-2xl font-bold tracking-tight text-emerald-400 hover:text-emerald-300 transition">
          ServerBase — База знаний
        </router-link>
  
        <!-- Навигация -->
        <nav class="flex items-center gap-6 md:gap-10 text-sm md:text-base font-medium">
          <router-link 
            to="/" 
            class="hover:text-emerald-400 transition-colors"
            active-class="text-emerald-400"
          >
            Гайды
          </router-link>
          
          <a 
            href="#" 
            class="hover:text-emerald-400 transition-colors"
          >
            Темы
          </a>
          
          <a 
            href="#" 
            class="hover:text-emerald-400 transition-colors"
          >
            Поиск
          </a>
  
          <!-- Можно потом заменить на авторизацию / профиль -->
          <button 
            class="bg-slate-700 hover:bg-slate-600 active:bg-emerald-700 px-4 py-1.5 rounded-md text-sm transition-colors"
          >
            Войти
          </button>
        </nav>
      </div>
    </header>
  </template>
  
  <script setup>
  // Пока логики нет — можно добавить позже:
  // - sticky поведение при скролле
  // - мобильное меню (бургер)
  // - индикатор активной страницы (уже частично сделано через router-link)
  </script>
  
  <style scoped>
  /* Дополнительные уточнения, если нужно */
  nav a {
    @apply relative;
  }
  
  nav a.router-link-active::after {
    content: '';
    @apply absolute -bottom-1 left-0 w-full h-0.5 bg-emerald-400;
  }
  </style>