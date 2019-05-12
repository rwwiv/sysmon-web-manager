"use strict";

import Vue from 'vue';
import axios from "axios";

const API_URL = (process.env.VUE_APP_API_URL === undefined) ? window.location.hostname : process.env.VUE_APP_API_URL;
const API_PORT = (process.env.VUE_APP_API_PORT === undefined) ? 8000 : process.env.VUE_APP_API_PORT;
const AUTH_TOKEN = process.env.VUE_APP_AUTH_TOKEN;

// Full config:  https://github.com/axios/axios#request-config
axios.defaults.baseURL = `https://${API_URL}:${API_PORT}`;
axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';


let config = {
  // baseURL: `${API_URL}:${API_PORT}`,
  timeout: 60 * 1000, // Timeout
  withCredentials: true, // Check cross-site Access-Control
};

const _axios = axios.create(config);

_axios.interceptors.request.use(
  function(config) {
    // Do something before request is sent
    return config;
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

// Add a response interceptor
_axios.interceptors.response.use(
  function(response) {
    // Do something with response data
    return response;
  },
  function(error) {
    // Do something with response error
    return Promise.reject(error);
  }
);

Plugin.install = function(Vue, options) {
  Vue.axios = _axios;
  window.axios = _axios;
  Object.defineProperties(Vue.prototype, {
    axios: {
      get() {
        return _axios;
      }
    },
    $axios: {
      get() {
        return _axios;
      }
    },
  });
};

Vue.use(Plugin);

export default Plugin;
