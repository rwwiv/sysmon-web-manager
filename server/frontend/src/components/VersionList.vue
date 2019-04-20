<!--<template>-->
<!--  <div class="box">-->
<!--    <div class="box-header with-border">-->
<!--      <h4 class="box-title">-->
<!--        Sysmon Versions-->
<!--      </h4>-->
<!--    </div>-->
<!--    &lt;!&ndash; /.box-header &ndash;&gt;-->
<!--    <div class="box-body">-->
<!--      <div class="col-auto">-->
<!--        <button type="button" class="btn btn-primary" @click="checkSysmonVersion()">Check for updates to Sysmon.</button>-->
<!--      </div>-->
<!--      <table class="table no-margin">-->
<!--        <thead>-->
<!--          <tr>-->
<!--            <th>Version Number</th>-->
<!--            <th></th>-->
<!--            <th>Current?</th>-->
<!--          </tr>-->
<!--        </thead>-->
<!--        <tbody>-->
<!--          <tr v-for="version in sysmonVersions" :key="version.name">-->
<!--            <td>{{ version.name }}</td>-->
<!--            <td v-if="version.is_current">-->
<!--              <span class="label label-primary" v-if="version.is_current">-->
<!--                Current Version-->
<!--              </span>-->
<!--            </td>-->
<!--            <td v-else></td>-->
<!--          </tr>-->
<!--        </tbody>-->
<!--      </table>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->
<script>
  import axios from 'axios';

  console.log('at versionlist');
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
      axios.post('http://localhost:8000/sysmon/').then(this.getAllVersions());
    },
    getAllVersions() {
      axios.get('http://localhost:8000/sysmon').then((response) => {
        this.sysmonVersions = response.data;
        console.log(response.data);
      })
        .catch((e) => {
          this.errors.push(e);
        });
    },
  },
  mounted() {
    console.log('at VersionsLIst');
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
