<template>
  <div class="box">
    <div class="box-header with-border">
      <h4 class="box-title">
        Agents
      </h4>
    </div>
    <!-- /.box-header -->
    <div class="box-body">
      <table class="table no-margin edit-all">
        <tbody>
          <tr>
            <td class="select-all">
              <input type="checkbox" value="checkAll" id="checkAll" v-model="selectAll"/>
              <label for="checkAll">Select All</label>
            </td>
            <td class="edit-all-options" align="right">
              <label for="manage-all">Manage Selected:</label>
              <select id="manage-all" v-model="manageAllSelected">
                <option disabled value="">
                  Select an Option
                </option>
                <option value="install">
                  Install Sysmon
                </option>
                <option value="restart">
                  Restart Sysmon
                </option>
                <option value="update">
                  Update Sysmon
                </option>
                <option value="config">
                  Change Sysmon Config
                </option>
                <option value="uninstall">
                  Uninstall Sysmon
                </option>
              </select>
              <button class="btn btn-primary" @click="manageAllAgents()">Apply</button>
            </td>
          </tr>
        </tbody>
      </table>

<!--
*** HOST LIST ***
* Generate single install button if new_agent, else offer management options.
* <popper> component is required for tooltip functionality.
-->
      <table class="table no-margin">
        <thead>
          <tr>
            <th></th>
            <th>IP Address</th>
            <th>Agent Status</th>
            <th>Sysmon Status</th>
            <th>Config</th>
            <th class="center-text">Version</th>
            <th class="center-text icon-column">Manage</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="agent in agents" :key="agent.id">
            <td><input class="agent-checkbox" :class="currentCheckAgentIsNew(agent.new_agent)" type="checkbox" :id="agent.uuid" :value="agent" v-model="checkedAgents" @change="getSelectedAgentIDs"/></td>
            <td>{{ agent.ip_address ? agent.ip_address : 'N/A' }}</td>
            <td>
              <span class="label" :class="currentStatusLabel(agent.online, agent.new_agent)">
              {{ currentStatusText(agent.online, agent.new_agent) }}
            </span>
            </td>
            <td>
              <span class="label" :class="currentStatusLabel(agent.exec_running, agent.new_agent)">
              {{ currentStatusText(agent.exec_running, agent.new_agent) }}
            </span>
            </td>
            <td>{{ agent.config_name_current ? agent.config_name_current : 'N/A' }}</td>
            <td class="center-text">{{ agent.sysmon_version_current ? agent.sysmon_version_current : 'N/A' }}</td>

<!--
*** INDIVIDUAL HOST MANAGEMENT ***
* Generate single install button if new_agent, else offer management options.
* <popper> component is required for tooltip functionality.
-->
            <td class="center-text control-icons">
<!-- v-if: New Agent -->
              <div class="management-options" v-if="agent.new_agent">
                <popper
                  trigger="hover"
                  :options="{
                    placement:'top',
                    modifiers: {offset: {offset: '0,5px'}}
                  }">
                  <div class="popper">
                    Install Sysmon
                  </div>
                  <a slot="reference" @click="installSysmon(agent.uuid)">
                    <i class="fa fa-download"></i>
                  </a>
                </popper>
              </div>
<!-- end v-if: New Agent -->

<!-- v-else: Existing Agent -->
              <div class="management-options" v-else>
<!-- Start / Restart Sysmon -->
                <popper
                  trigger="hover"
                  :options="{
                    placement:'top',
                    modifiers: {offset: {offset: '0,5px'}}
                  }">
                  <div class="popper">
                    Start / Restart Sysmon
                  </div>
                  <a slot="reference" @click="runSysmon(agent.uuid)" >
                    <i class="fa fa-play"></i>
                  </a>
                </popper>
<!-- Edit Sysmon Config -->
                <popper
                  trigger="hover"
                  :options="{
                    placement:'top',
                    modifiers: {offset: {offset: '0,5px'}}
                  }">
                  <div class="popper">
                    Edit Sysmon Config
                  </div>
                  <a slot="reference" data-toggle="modal" data-target="#agent-modal" @click="displayAgent(agent)">
                    <i class="fa fa-wrench"></i>
                  </a>
                </popper>
<!-- Uninstall Sysmon -->
                <popper
                  trigger="hover"
                  :options="{
                    placement:'top',
                    modifiers: {offset:{offset: '0,5px'}}
                  }">
                  <div class="popper">
                    Uninstall Sysmon
                  </div>
                  <a slot="reference" @click="uninstallSysmon(agent.uuid)" title="Uninstall Sysmon">
                    <i class="fa fa-trash"></i>
                  </a>
                </popper>
              </div>
<!-- end v-else: Existing Agent -->
            </td>
<!-- end INDIVIDUAL HOST MANAGEMENT -->
          </tr>
        </tbody>
      </table>
<!-- HOST LIST -->
    </div>
<!--
*** EDIT SYSMON CONFIG MODAL ***
* Generate single install button if new_agent, else offer management options.
* <popper> component is required for tooltip functionality.
-->
    <div class="modal fade" id="agent-modal" tabindex="-1" role="dialog" aria-labelledby="agent-modal-label">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
              <h3>Edit Sysmon Config</h3>
              <h4 class="modal-title"><b>IP:</b> {{selectedAgent.ipAddress ? selectedAgent.ipAddress : 'Agent/Host location unknown.'}}</h4>
            </div>
            <!-- /.modal-header -->
            <div class="modal-body">
              <h5><b>Current Sysmon Config:</b><br/>{{selectedAgent.config_name_current ? selectedAgent.config_name_current : 'No configuration file is currently associated with this agent/host.'}}</h5>
              <h5><b>Available Sysmon Configs:</b></h5>
                <select v-model="selectedConfig">
                  <option disabled value="">Select New Sysmon Config</option>
                  <option v-for="config in sysmonConfigs" :key="config.id" v-bind:value="config.name">{{config.name}}</option>
                </select>
              <!--  Could offer to edit the config file from here
                <router-link v-if="selectedConfig" class="edit-config-link" :to="{name: 'management', query:{configFile: selectedConfig}}" data-dismiss="modal">
                  <i class="fa fa-gear"></i> Edit this config file.
                </router-link>
              -->
            </div>
<!-- /.modal-body -->
            <div class="modal-footer">
              <button type="button" class="btn btn-primary" @click="saveConfig(selectedAgent.uuid, selectedConfig)">Save changes</button>
              <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
            </div>
<!-- /.modal-footer -->
          </div>
        </div>
    </div>
<!-- End EDIT SYSMON CONFIG MODAL -->


<!-- Loading: Covers entire host list -->

    <div id="loadingOverlay" class="overlay hidden">
      <i class="fa fa-refresh fa-spin"></i>
    </div>

  </div>
<!-- /.box -->
</template>

<script>
  import axios from 'axios';
  import Popper from 'vue-popperjs';
  import 'vue-popperjs/dist/vue-popper.css';
  import '../assets/_css/tooltips.css';

  export default {
    name: 'AgentList',
    data() {
      return {
        agents: [],
        errors: [],
        sysmonConfigs: [],
        selectedAgent: '',
        selectedConfig: '',
        checkedAgents: [],
        checkedAgentsIDs: [],
        selectAll: false,
        manageAllSelected: '',
        timer: '',
      };
    },
    components: {
      popper: Popper,
    },
    methods: {
      displayAgent(agent) {
        this.selectedAgent = agent;
      },
      currentCheckAgentIsNew(agentStatus) {
        if (agentStatus) {
          return 'agent-is-new';
        }
        return '';
      },
      currentStatusLabel(agentStatus, needsInstall = false) {
        if (needsInstall) {
          return 'label-primary';
        }
        if (agentStatus) {
          return 'label-success';
        }
        return 'label-danger';
      },
      currentStatusText(agentStatus, needsInstall = false) {
        if (needsInstall) {
          return 'New';
        }
        if (agentStatus) {
          return 'Online';
        }
        return 'Offline';
      },
      hideLoadingState(){
        let loaderIsNotVisible = $('#loadingOverlay').hasClass('hidden');
        if(!loaderIsNotVisible){
          $('#loadingOverlay').addClass('hidden');
        }
      },
      showLoadingState(){
        let loaderIsNotVisible = $('#loadingOverlay').hasClass('hidden');
        
        if(loaderIsNotVisible){
          $('#loadingOverlay').removeClass('hidden');
        }
      },
      saveConfig(agentID, config) {
        if (config) {
          axios.patch(`http://localhost:8000/agents/${agentID}/config/${config}`)
          .then((response) => {
            console.log(response);
          })
          .catch((e) => {
            console.log(e.message);
          });
          $('#agent-modal').modal('hide');
          this.getHostList();
        } else {
          console.log('No selection made.');
        }
      },
      runSysmon(agentID) {
        this.showLoadingState();
        axios.post(`http://localhost:8000/agents/${agentID}`)
        .then((response) => {
          console.log(response);
          this.hideLoadingState();
          this.getHostList();
        })
        .catch((e) => {
          console.log(e.message);
          this.hideLoadingState();
        });
      },
      installSysmon(agentID) {
        this.showLoadingState();
        axios.patch(`http://localhost:8000/agents/${agentID}`)
        .then((response) => {
          //Debug
          //console.log(response);
          this.hideLoadingState();
          this.getHostList();
        })
        .catch((e) => {
          this.hideLoadingState();
          console.log(e.message);
        });
      },
      uninstallSysmon(agentID) {
        this.showLoadingState();
        axios.delete(`http://localhost:8000/agents/${agentID}`)
        .then((response) => {
          //Debug
          console.log(response);
          this.hideLoadingState();
          this.getHostList();
        })
        .catch((e) => {
          console.log(e.message);
          this.hideLoadingState();
        });
      },
      getHostList() {
        axios.get('http://localhost:8000/agents')
        .then((response) => {
          this.agents = response.data;
          //Debug
          //console.log(response.data);
        })
        .catch((e) => {
          this.errors.push(e);
        });
      },
      getAvailableSysmonConfigs() {
        axios.get('http://localhost:8000/configs')
        .then((response) => {
          this.sysmonConfigs = response.data;
          //Debug
          //console.log(response.data);
        })
        .catch((e) => {
          this.errors.push(e);
        });
      },
      //Grab IDs from Selected Agents
      getSelectedAgentIDs(){
        this.checkedAgentsIDs = [];
        for(let i = 0; i < this.checkedAgents.length; i++){
          this.checkedAgentsIDs.push(this.checkedAgents[i].uuid);
        }
      },
      //Grab all Agent Objects
      selectAllAgents() {
        this.checkedAgents = [];
        if (!this.selectAll) {
          for (let i = 0; i < this.agents.length; i++) {
            this.checkedAgents.push(this.agents[i]);
          }
        }
        this.getSelectedAgentIDs();
      },
      //Grab only NEW && Selected agents
      selectedNewAgents() {
        this.checkedAgentsIDs = [];
        for (let i = 0; i < this.checkedAgents.length; i++) {
          if (this.checkedAgents[i].new_agent) {
            this.checkedAgentsIDs.push(this.checkedAgents[i].uuid);
          }
        }
      },
      manageAllAgents() {
        switch (this.manageAllSelected) {
          case 'install':
            this.showLoadingState();
            this.selectedNewAgents();
            axios.post('http://localhost:8000/multi/install', JSON.stringify(this.checkedAgentsIDs))
            .then((response) => {
              //Debug
              //console.log(response.data);
              this.hideLoadingState();
              this.getHostList();
            })
            .catch((e) => {
              console.log(e.message);
              this.hideLoadingState();
            });
          break;
          case 'restart':
            this.showLoadingState();
            axios.post('http://localhost:8000/multi/restart', JSON.stringify(this.checkedAgentsIDs))
            .then((response) => {
              //Debug
              //console.log(response.data);
              this.hideLoadingState();
              this.getHostList();
            })
            .catch((e) => {
              console.log(e.message);
              this.hideLoadingState();
            });
          break;
          case 'update':
            
          break;
          case 'config':
            
          break;
          case 'uninstall':
            this.showLoadingState();
            axios.post('http://localhost:8000/multi/uninstall', JSON.stringify(this.checkedAgentsIDs))
            .then((response) => {
              //Debug
              //console.log(response.data);
              this.hideLoadingState();
              this.getHostList();
            })
            .catch((e) => {
              console.log(e.message);
              this.hideLoadingState();
            });
          break;
          default:
            // Nothing selected
          break;
        }
      },
      stopHostListAutoUpdate() {
        clearInterval(this.timer);
      },
    },
    mounted() {
      this.getHostList();
      this.timer = setInterval(this.getHostList, 10000);
      this.getAvailableSysmonConfigs();
      const that = this;
      // Handle iCheckBox in the host list table head.
      jQuery('#checkAll').on('ifChanged', (e) => {
        if (e.target.checked) {
          that.selectAllAgents();
          that.selectAll = true;
        } else {
          that.selectAllAgents();
          that.selectAll = false;
        }
      });
    },
    beforeDestroy() {
      clearInterval(this.timer);
    },
  };

</script>

<style scoped>
thead{
  background-color:#f3f3f3;
}
.fa{
  font-size:20px;
}
.select-all {

}
.edit-all td{
  border:0;
}
.edit-all input,
.edit-all label{
  display:inline-block;
}
.edit-all label,
.edit-all-options button {
  margin-left:10px;
}
.edit-all-options label {
  margin-right:10px;
}
td a {
  cursor:pointer;
}
.center-text {
  text-align:center;
}
.icon-column{
  width:20%;
}
.edit-all-options>span{
  margin-right:15px;
}
.edit-all-options>span:last-child{
  margin-right:0;
}
.install-btn,
.management-options>span {
  margin-right:10%;
}
.management-options>span:last-child {
  margin-right:0;
}
.edit-config-link{
  margin-left:10px;
  cursor:pointer;
}
</style>
