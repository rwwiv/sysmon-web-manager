import axios from 'axios';
import constants from '../modules/constants';

export default {
  checkSysmonUpdate(data) {
    return axios.post(`${constants.serverUrl}/sysmon/`, data);
  },
  getSysmonVersions() {
    return axios.get(`${constants.serverUrl}/sysmon/`);
  },
};
