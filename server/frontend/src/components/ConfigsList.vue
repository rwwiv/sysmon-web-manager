<template>
  <div class="box">
    <div class="box-header with-border">
      <h4 class="box-title">
        Configurations
      </h4>
    </div>
    <!-- /.box-header -->
    <div class="box-body">
      <div class="col-auto">
        <button class="btn btn-secondary pull-right">Add New Configuration</button>
      </div>
      <table class="table no-margin">
        <thead>
          <tr>
            <th>Name</th>
            <th>Is Default?</th>
            <th class = "center-text icon-column">View</th>
            <th class = "center-text icon-column">Edit</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="config in configs" :key="config.name">
            <td>{{ config.name }}</td>
            <td>{{ config.isDefault }}</td>
            <td class="center-text">
              <a @click="viewConfig(config.name)">
                <i class="fa fa-search-plus"></i>
              </a>
            </td>
            <td class="center-text">
              <router-link to="ConfigEditor" active-class="active">
                <a><i class="fa fa-wrench"></i> </a>
              </router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
  import axios from 'axios';

export default {
  name: 'ConfigsList',
  data() {
    return {
      configs: [],
      errors: [],
      editConfig: '',
      viewConfig: '',
    };
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/configs', { crossdomain: true })
      .then((response) => {
        this.configs = response.data;
        console.log(response.data);
      })
      .catch((e) => {
        this.errors.push(e);
      });
  },
};
</script>

<style scoped>
  td a {
    cursor:pointer;
  }
  .center-text {
    text-align:center;
  }
  .icon-column{
    width:10%;
  }
</style>
