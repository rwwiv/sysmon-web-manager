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
        <router-link to="ConfigEditor" active-class="active" button class="btn btn-secondary pull-right">Add New Configuration</router-link>
      </div>
      <table class="table no-margin">
        <thead>
          <tr>
            <th>Name</th>
            <th>Is Default?</th>
            <th class = "center-text icon-column">View/Edit</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="config in configs" :key="config.NAME">
            <td>{{ config.NAME }}Name</td>
            <td>{{ config.IS_DEFAULT ? 'Default': '' }}Default Status</td>
            <td class="center-text">
              <router-link to="ConfigEditor" active-class="active">
                <a><i class="fa fa-search-plus"></i> </a>
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
  methods: {
    getAllConfigs() {
      axios.get('http://localhost:8000/configs')
        .then((response) => {
          this.configs = response.data;
          console.log(response.data);
        })
        .catch((e) => {
          this.errors.push(e);
        });
    },
  },
  mounted() {
  this.getAllConfigs();
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
