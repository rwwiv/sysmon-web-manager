<template>
  <div class="box-header with-border">
    <div class="row">
      <div class="col-md-2">
        <h4 class="box-title">
          {{(groupName === "unassigned") ? "Ungrouped Hosts" : groupName}}
        </h4>
      </div>
      <div v-if="groupName !== 'unassigned'">
        <div class="col-md-3">
          <form class="form-inline">
            <div class="form-group">
              <select v-model="selectedConfig">
                <option v-for="config in allConfigs"
                        :selected="configSelected(config.name)"
                        v-bind:key="config.name">
                  {{config.name}}
                </option>
              </select>
            </div>
            <button class="btn btn-secondary" type="button" @click="updateGroup">Change config</button>
          </form>
        </div>
        <div class="col-md-3">
          <form class="form-inline">
            <div class="form-group">
              <select v-model="selectedVersion">
                <option v-for="version in allSysmonVersions"
                        :selected="versionSelected(version.version)"
                        v-bind:key="version.version">
                  {{version.version}}
                </option>
              </select>
            </div>
            <button class="btn btn-secondary" @click="updateGroup">Change version</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import groupAPI from '../api/groups';
  import configAPI from '../api/configs';
  import sysmonAPI from '../api/sysmon';

  export default {
    name: 'GroupHeader',
    props: [
      'groupName',
    ],
    data() {
      return {
        selectedConfig: '',
        selectedVersion: '',
        allConfigs: [],
        allSysmonVersions: [],
      };
    },
    beforeMount() {
      groupAPI.getSingleGroup(this.groupName)
        .then((response) => {
          console.log(response);
          this.selectedConfig = response.data.configuration;
          this.selectedVersion = response.data.sysmon;
        })
        .catch(() => {});
      configAPI.getAllConfigs()
        .then((response) => {
          console.log(response);
          this.allConfigs = response.data;
        });
      sysmonAPI.getSysmonVersions()
        .then((response) => {
          console.log(response);
          this.allSysmonVersions = response.data;
        });
    },
    methods: {
      updateGroup() {
        groupAPI.updateGroup(this.selectedVersion, this.selectedConfig, this.groupName);
      },
      configSelected(configName) {
        return this.selectedConfig === configName;
      },
      versionSelected(version) {
        return this.selectedVersion === version;
      },
    },
  };
</script>

<style scoped>
  .btn {
    margin-left: 1em;
  }
</style>
