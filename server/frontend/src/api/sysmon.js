import axios from 'axios';
import constants from '../modules/constants';

export default {
  checkSysmonUpdate() {
    return axios.post(`${constants.serverUrl}/sysmon/`);
  },
  getSysmonVersions() {
    return axios.get(`${constants.serverUrl}/sysmon/`);
  },
};
