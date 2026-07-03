import { createRouter, createWebHistory } from 'vue-router'
import SignUp from '../views/SignUp.vue'
import Login from '../views/Login.vue'
import Tasks from '../views/Tasks.vue'

const routes = [
  {
    path: '/',
    name: 'home',
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUp
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/tasks',
    name: 'tasks',
    component: Tasks
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router