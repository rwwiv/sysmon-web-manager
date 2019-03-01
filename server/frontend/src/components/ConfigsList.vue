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
              <a @click="editConfig(config.name)">
                <i class="fa fa-wrench"></i>
              </a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
  import axios from 'axios';
  import configs from '../../configsList.json';

export default {
  name: 'ConfigsList',
  data() {
    return {
      configs,
    };
  },
  methods: {
    // goal with viewConfig is just to display it in the console//
    viewConfig(name) {
      axios.get(`/updates/config/${name}`).then((response) => {
        console.log(response.data);
      });
    },
    // goal with edit is to display xml in an editable form //
    editConfig(name) {
      axios.get(`/configs/${name}`).then((response) => {
        var xmlText = response.data;
        console.log(xmlText);
        axios.post(`/configs/${name}`);
      });
    },
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
