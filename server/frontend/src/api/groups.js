import axios from 'axios';
import constants from '../modules/constants';

export default {
  moveAgentToGroup(agent, group) {
    return axios.patch(`${constants.serverUrl}/groups/${agent}/${group}`);
  },
  createGroup(version, groupConfig, groupName) {
    return axios({
             method: 'post',
             url: `${constants.serverUrl}/groups/${groupName}`,
             data: {
               sysmon_version: version,
               configuration: groupConfig,
             },
           });
  },
  getSingleGroup(name) {
    return axios.get(`${constants.serverUrl}/groups/${name}`);
  },
  getAllGroups() {
    return axios.get(`${constants.serverUrl}/groups`);
  },

  updateGroup(version, groupConfig, groupName) {
    return axios({
      method: 'put',
      url: `${constants.serverUrl}/groups/${groupName}`,
      data: {
        sysmon_version: version,
        configuration: groupConfig,
      },
    });
  },
};
