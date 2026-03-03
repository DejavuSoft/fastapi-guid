import { createRouter, createWebHistory } from 'vue-router'
import PostsList from '@/views/PostsList.vue'
import PostDetail from '@/views/PostDetail.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: PostsList,
      meta: {
        title: 'ServerBase - База знаний'
      },
    },
    {
      path: '/posts/:id',
      name: 'post-detail',
      component: PostDetail,
      meta: {
        title: 'Post detail'
      },
    },
  ],

  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  },
})

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'FastAPI Shop'
  next()
})

export default router