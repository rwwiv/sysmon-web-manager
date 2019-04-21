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
            <th></th>
            <th class = "center-text icon-column">View/Edit</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="config in configs" :key="config.name">
            <td>{{ config.name }}</td>
            <td v-if="config.default">
              <span class="label label-primary" v-if="config.default">
                Default
              </span>
            </td>
            <td v-else></td>
            <td class="center-text">
              <router-link :to="{name: 'ConfigEditor', params: {id: config.name}}"
                           active-class="active">
                <a>
                  <i class="fa fa-search-plus"></i>
                </a>
              </router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
  import configAPI from '../api/configs';

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
      configAPI.getAllConfigs()
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
  thead{
    background-color:#f3f3f3;
  }
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
