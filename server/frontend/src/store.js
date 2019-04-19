import Vuex from 'vuex';
import 'es6-promise/auto';
import user from './modules/user';

export default new Vuex.Store({
  modules: {
    user,
  },
});
