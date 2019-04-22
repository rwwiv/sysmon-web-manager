import axios from 'axios';
import constants from '../modules/constants';

export default {
  getAllConfigs() {
    return axios.get(`${constants.serverUrl}/configs/`);
  },
  getSingleConfig(configName) {
    return axios.get(`${constants.serverUrl}/configs/${configName}`);
  },
  createConfig(data) {
    return axios.post(`${constants.serverUrl}/configs/`, data);
  },
  updateConfig(data) {
    return axios.post(`${constants.serverUrl}/configs/`, data);
  },
};
