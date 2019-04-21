/* eslint no-param-reassign: 0 */
import userAPI from '../api/users';

const statusEnum = {
  LOGIN_SUCCESS: 0,
  LOGIN_FAILURE: 1,
  LOGOUT: 2,
};

export default {
  state: {
    username: '',
    loginStatus: statusEnum.LOGOUT,
  },
  actions: {
    authUser({ commit, username, password }) {
      userAPI.authUser(username, password)
        .then(() => {
          commit('logInUser', username);
        });
    },
    createUser({ commit, username, password }) {
      userAPI.createUser(username, password)
        .then(() => {
          commit('logInUser', username);
        });
    },
    logoutUser({ commit }) {
      commit('userLogout');
    },
  },
  mutations: {
    userLogin(state, username) {
      state.loginStatus = statusEnum.LOGIN_SUCCESS;
      state.username = username;
    },
    userLogout(state) {
      state.loggedIn = statusEnum.LOGOUT;
      state.username = '';
    },
    loginFailure(state) {
      state.loginFailed = statusEnum.LOGIN_FAILURE;
    },
  },
};
