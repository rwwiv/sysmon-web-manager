import axios from 'axios';
import constants from '../modules/constants';

const supportLinksUrl = `${constants.serverUrl}/support/links`;
const supportConfigUrl = `${supportLinksUrl}/configs`;
const supportSysmonUrl = `${supportLinksUrl}/sysmon`;

export default {
  getSysmonVersionRepoLink() {
    return axios.get(`${supportSysmonUrl}/repo`);
  },
  setSysmonVersionRepoLink(link) {
    const data = {
      link,
    };
    return axios.post(`${supportSysmonUrl}/repo`, data);
  },
  getDefaultConfigDownloadLink() {
    return axios.get(`${supportConfigUrl}/download`);
  },
  setDefaultConfigDownloadLink(link) {
    const data = {
      link,
    };
    return axios.post(`${supportConfigUrl}/download`, data);
  },
  getSysmonDownloadLink() {
    return axios.get(`${supportSysmonUrl}/download`);
  },
  setSysmonDownloadLink(link) {
    const data = {
      link,
    };
    return axios.post(`${supportSysmonUrl}/download`, data);
  },
};
