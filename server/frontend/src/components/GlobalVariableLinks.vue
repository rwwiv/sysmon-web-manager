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
