import axios from 'axios';

export default class GroupAPI {
    getAllConfigs() {
        return axios.get(`/groups`)
    }
}
