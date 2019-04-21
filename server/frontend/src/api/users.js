import axios from 'axios';
import constants from '../modules/constants';

export default {
  authUser(username, password) {
    const data = {
      username,
      password,
    };
    return axios.post(`${constants.serverUrl}/users/auth`, data);
  },
  createUser(username, password) {
    const data = {
      username,
      password,
    };
    return axios.post(`${constants.serverUrl}/users/create`, data);
  },
};
