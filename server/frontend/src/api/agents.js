import axios from 'axios';
import constants from '../modules/constants';

export default {
  getAllAgents() {
    return axios.get(`${constants.serverUrl}/agents/`);
  },
  installSysmon(uuid) {
    return axios.patch(`${constants.serverUrl}/agents/${uuid}`);
  },
  uninstallSysmon(uuid) {
    return axios.delete(`${constants.serverUrl}/agents/${uuid}`);
  },
  runSysmon(uuid) {
    return axios.post(`${constants.serverUrl}/agents/${uuid}`);
  },
  updateAgentConfig(uuid, configName) {
    return axios.patch(`${constants.serverUrl}/agents/${uuid}/config/${configName}`);
  },
  installSysmonMultiple(array) {
    return axios.post(`${constants.serverUrl}/multi/install`, JSON.stringify(array));
  },
  uninstallSysmonMultiple(array) {
    return axios.post(`${constants.serverUrl}/multi/install`, JSON.stringify(array));
  },
  runSysmonMultiple(array) {
    return axios.post(`${constants.serverUrl}/multi/restart`, JSON.stringify(array));
  },

};
