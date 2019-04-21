<template>
  <div class="box">
    <div class="box-header with-border">
      <h4 class="box-title">
        Sysmon Versions
      </h4>
    </div>
    <!-- /.box-header -->
    <div class="box-body">
      <div class="col-auto">
        <button type="button" class="btn btn-primary" @click="checkSysmonVersion()">Check for updates to Sysmon.</button>
      </div>
      <table class="table no-margin">
        <thead>
          <tr>
            <th>Version Number</th>
            <th>Current?</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="version in sysmonVersions" :key="version.version">
            <td>{{ version.version }}</td>
            <td v-if="version.is_current">
              <span class="label label-primary" v-if="version.is_current">
                Current
              </span>
            </td>
            <td v-else></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
  import sysmonAPI from '../api/sysmon';

export default {
  name: 'VersionList',
  data() {
    return {
      sysmonVersions: [],
      errors: [],
    };
  },
  methods: {
    checkSysmonVersion() {
      sysmonAPI.checkSysmonUpdate()
        .then((response) => {
          this.getAllVersions();
          console.log('got all versions?');
          console.log(response);
      })
        .catch((e) => {
          this.errors.push(e);
        });
    },
    getAllVersions() {
      sysmonAPI.getSysmonVersions()
        .then((response) => {
        this.sysmonVersions = response.data;
        console.log(response.data);
      })
        .catch((e) => {
          this.errors.push(e);
        });
    },
  },
  mounted() {
    this.getAllVersions();
  },
};
</script>

<style scoped>
  td a {
    cursor:pointer;
  }
</style>

<style scoped>
  td a {
    cursor:pointer;
  }
</style>
