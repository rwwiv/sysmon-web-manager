import Vue from 'vue';
import Router from 'vue-router';
import store from './store';

Vue.use(Router);

const requireAuth = (to, from, next) => {
  if (process.REQUIRE_AUTH !== 1) {
    next();
  } else if (store.modules.user.state.loginStatus === 0) {
    next();
  } else {
    next('login');
  }
};

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import('./views/Login.vue'),
    },
    {
      path: '/',
      redirect: {
        name: 'monitor',
      },
      beforeEach: (to, from, next) => {
        requireAuth(to, from, next);
      },
      name: 'wrapper',
      component: () => import('./views/Wrapper.vue'),
      children: [
        {
          path: '/monitor',
          name: 'monitor',
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import('./views/Monitor.vue'),
        },
        {
          path: '/config-manager',
          name: 'config-manager',
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import('./views/ConfigManager.vue'),
        },
        {
          path: '/config-editor/:id',
          name: 'config-editor',
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import('./views/ConfigEditor.vue'),
        },
        {
          path: '/config-editor/new',
          name: 'config-editor-new',
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import('./views/ConfigEditor.vue'),
        },
        {
          path: '/support',
          name: 'support',
          component: () => import('./views/Support.vue'),
        },
        {
          path: '/versions',
          name: 'versions',
          component: () => import('./views/Versions.vue'),
        },
      ],
    },
  ],
});
