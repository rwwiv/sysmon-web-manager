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
      beforeEach: requireAuth(),
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
          path: '/management',
          name: 'management',
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import('./views/Management.vue'),
        },
        {
          path: '/config-editor',
          name: 'config-editor',
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import('./views/ConfigEditor.vue'),
        },
      ],
    },
  ],
});
