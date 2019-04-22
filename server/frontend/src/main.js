import Vue from 'vue';
import Vuex from 'vuex';
import 'bootstrap';
import 'admin-lte';
import 'bootstrap/dist/css/bootstrap.css';
import 'admin-lte/dist/css/AdminLTE.css';
import 'ionicons/dist/scss/ionicons.scss';
import 'font-awesome/scss/font-awesome.scss';
import 'admin-lte/dist/css/skins/skin-black.css';
import './assets/_css/animate.css';
import App from './App.vue';
import router from './router';
import store from './store';


Vue.config.productionTip = false;
Vue.use(Vuex);

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
