import Vue from 'vue';
import 'bootstrap';
import 'admin-lte';
import 'bootstrap/dist/css/bootstrap.css';
import 'admin-lte/dist/css/AdminLTE.css';
import 'ionicons/dist/scss/ionicons.scss';
import 'font-awesome/scss/font-awesome.scss';
import 'admin-lte/dist/css/skins/skin-black.css';
import 'icheck/skins/minimal/blue.css';
import 'icheck/icheck';
import App from './App.vue';
import router from './router';


Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
