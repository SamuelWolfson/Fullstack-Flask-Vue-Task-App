import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '../stores/auth';

import Login from '../';
import DashboardView from '../views/TaskList.vue/index.js';

const routes = [
  {
    path: '/',
    redirect: '/login',
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/register',
    name: 'Register',
    component: AuthView,
  },
  {
    path: '/task-list',
    name: 'TaskList',
    component: AuthView,
  },
  {
    path: '/email-to-reset-password',
    name: 'ForgotPassword',
    component: AuthView,
  },
  {
    path: '/reset-password',
    name: 'ResetPassword',
    component: AuthView,
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: AuthView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next({ name: 'Login' });
  } else if (to.meta.requiresGuest && authStore.isAuthenticated) {
    next({ name: 'Dashboard' });
  } else {
    next();
  }
});

export default router;
