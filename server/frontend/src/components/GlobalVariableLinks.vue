<template>
    <div class="box">
      <div class="box-header with-border">
        <h4 class="box-title">
          Global Variable Links
        </h4>
      </div>
      <div class="box-body">
        <table class="table no-margin">
          <thead>
            <tr>
              <th>Global Variable</th>
              <th></th>
              <th class = "center-text icon-column">Value</th>
            </tr>
          </thead>
          <tbody>
          <tr>
            <td>variable name</td>
            <td class="center-text">
              variable value
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

</style>
