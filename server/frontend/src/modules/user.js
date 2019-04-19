/* eslint no-param-reassign: 0 */
import userAPI from '../api/users';

export default {
  state: {
    loggedIn: false,
    username: '',
  },
  mutations: {
    logInUser(state, username) {
      state.loggedIn = true;
      state.username = username;
    },
  },
  actions: {
    authUser({ commit, username, password }) {
      userAPI.authUser(username, password)
        .then(() => {
          commit('logInUser', username);
        })
        .catch(() => {});
    },
    createUser({ commit, username, password }) {
      userAPI.createUser(username, password)
        .then(() => {
          commit('logInUser', username);
        })
        .catch(() => {});
    },
  },
};
