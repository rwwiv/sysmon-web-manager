/* eslint no-param-reassign: 0 */
import supportAPI from '../api/support';


export default {
  state: {
    sysmonRepoLink: '',
    sysmonDownloadLink: '',
    defaultConfigDownloadLink: '',
  },
  mutations: {
    setSysmonRepoLink(state, link) {
       state.sysmonRepoLink = link;
    },
    setSysmonDownloadLink(state, link) {
      state.sysmonDownloadLink = link;
    },
    setDefaultConfigDownloadLink(state, link) {
      state.defaultConfigDownloadLink = link;
    },
  },
  actions: {
    getSysmonVersionRepoLink({ commit }) {
      supportAPI.getSysmonVersionRepoLink()
        .then((response) => {
          commit('setSysmonRepoLink', response.data.link);
        })
        .catch(() => {});
    },
    getSysmonDownloadLink({ commit }) {
      supportAPI.getSysmonDownloadLink()
        .then((response) => {
          commit('setSysmonDownloadLink', response.data.link);
        })
        .catch(() => {});
    },
    getDefaultConfigDownloadLink({ commit }) {
      supportAPI.getDefaultConfigDownloadLink()
        .then((response) => {
          commit('setDefaultConfigDownloadLink', response.data.link);
        })
        .catch(() => {});
    },
    changeSysmonRepoLink({ commit, link }) {
      supportAPI.setSysmonVersionRepoLink(link)
        .then(() => {
          commit('setSysmonRepoLink', link);
        })
        .catch(() => {});
    },
    changeSysmonDownloadLink({ commit, link }) {
      supportAPI.setSysmonDownloadLink(link)
        .then(() => {
          commit('setSysmonDownloadLink', link);
        })
        .catch(() => {});
    },
    changeConfigDownloadLink({ commit, link }) {
      supportAPI.setDefaultConfigDownloadLink(link)
        .then(() => {
          commit('setDefaultConfigDownloadLink', link);
        })
        .catch(() => {});
    },
  },
};
