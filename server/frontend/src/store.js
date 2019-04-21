import Vue from 'vue';
import Vuex from 'vuex';
import 'es6-promise/auto';
import user from './modules/user';
import support from './modules/support';


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user,
    support,
  },
});
