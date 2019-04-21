<template>
<section class="groups">
  <!-- /#controls-top -->
  <div class="clearfix" id="controls-top">
    <table class="table no-margin edit-all">
        <tbody>
          <tr>
            <td class="select-all">
              <input type="checkbox" value="checkAll" id="checkAll" v-model="selectAll"/>
              <label for="checkAll">Select All</label>
            </td>
            <td class="edit-all-options" align="left">
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
                <option value="uninstall">
                  Uninstall Sysmon
                </option>
              </select>
              <button class="btn btn-primary" @click="manageAllAgents('allAgents', true)">Apply</button>
            </td>
            <td align="right">
              <div v-if="groupSaving" class="" id="container-createGroupBtn">
                <button type="button" class="btn btn-primary" id="btn-createGroup" data-toggle="modal" data-target="#createGroupModal"><i class="fa fa-refresh fa-spin"></i></button>
              </div>
              <div v-else class="" id="container-createGroupBtn">
                <button type="button" class="btn btn-primary" id="btn-createGroup" data-toggle="modal" data-target="#createGroupModal">Create Group</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>

    <!-- Modal -->
    <div class="modal fade" id="createGroupModal" tabindex="-1" role="dialog" aria-labelledby="createGroupModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title" id="myModalLabel">Create New Group</h4>
          </div>
          <div class="modal-body">
            <h5><b>Group Name:</b></h5>
            <input type="text" v-model="desiredGroupName" placeholder="Enter New Group Name"/>
            <h5><b>Select Sysmon Configuration:</b></h5>
            <select v-model="selectedGroupConfig">
              <option disabled value="">Available Configurations</option>
              <option v-for="config in sysmonConfigs" :key="config.id" v-bind:value="config.name">{{config.name}}</option>
            </select>
            <h5><b>Select Sysmon Version:</b></h5>
            <select v-model="selectedGroupVersion">
              <option disabled value="">Available Sysmon Versions</option>
              <option v-for="version in sysmonVersions" :key="version.id" v-bind:value="version.version">{{version.version}}</option>
            </select>
            <h4 id="create-group-error-message" class="error-message hidden">You must provide a Group Name, Configuration, and Sysmon Version to create a group.</h4>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>
            <button type="button" class="btn btn-primary" @click="saveGroup(desiredGroupName, selectedGroupConfig, selectedGroupVersion)">Create Group</button>
          </div>
        </div>
      </div>
    </div>
  </div>
<!-- /End #controls-top -->


<!--
************************************************************************
 GROUPED SYSMON AGENTS
************************************************************************
-->
<!-- /.box -->
<ul id="group-list">
  <li class="box" v-for="(agents, group) in groupedAgents">
    <div class="box-header with-border">
      <h4 class="box-title">
       {{(group == "unassigned") ? "Ungrouped Hosts" : group}}
      </h4>
    </div>
    <!-- /.box-header -->
    <div class="box-body">
<!--
*** HOST LIST ***
* Generate single install button if new_agent, else offer management options.
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

            <td class="ip-address">
              <popper
                  trigger="hover"
                  :options="{
                    placement:'top',
                    modifiers: {offset: {offset: '0,0'}}
                  }">
                  <div class="popper">UUID: {{agent.uuid}}</div>
                  <p slot="reference">{{ agent.ip_address ? agent.ip_address : 'N/A' }}</p>
              </popper>
            </td>
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
******************************************************************************
  INDIVIDUAL HOST MANAGEMENT
  Generate single install button if new_agent, else offer management options.
  <popper> component is required for tooltip functionality.
******************************************************************************
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
                  <a slot="reference" @click="installSysmon(agent.uuid, group)">
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
                  <a slot="reference" @click="runSysmon(agent.uuid, group)" >
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
                    Host Settings
                  </div>
                  <a slot="reference" data-toggle="modal" data-target="#agent-modal" @click="displayAgent(agent, group)">
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
                  <a slot="reference" @click="uninstallSysmon(agent.uuid, group)" title="Uninstall Sysmon">
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
<!-- end HOST LIST -->
    </div>

<!-- Loading Overlay -->
    <div class="overlay hostOverlays hidden" :class="getOverlayGroupClassName(group)">
      <i class="fa fa-refresh fa-spin"></i>
    </div>
  </li>
</ul>
<!-- /.box -->


<!--
************************************************************************
  HOST SETTINGS MODAL
************************************************************************
-->
    <div class="modal fade" id="agent-modal" tabindex="-1" role="dialog" aria-labelledby="agent-modal-label">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
              <h3>Host Settings</h3>
              <h4 class="modal-title"><b>IP Address:</b> {{selectedAgent.ip_address ? selectedAgent.ip_address : 'Agent/Host location unknown.'}},<br/><b>UUID:</b> {{selectedAgent.uuid ? selectedAgent.uuid : 'Agent/Host cannot be identified.'}}</h4>
            </div>
            <!-- /.modal-header -->
            <div class="modal-body">
              <h5><b>Current Sysmon Config:</b><br/>{{selectedAgent.config_name_current ? selectedAgent.config_name_current : 'No configuration file is currently associated with this agent/host.'}}</h5>
              <h5><b>Available Sysmon Configs:</b></h5>
              <select v-model="selectedConfig">
                <option disabled value="">Select New Sysmon Config</option>
                <option v-for="config in sysmonConfigs" :key="config.id" v-bind:value="config.name">{{config.name}}</option>
              </select>
              <h5><b>Group:</b><br/>{{selectedAgent.group ? selectedAgent.group : 'Not currently grouped.'}}</h5>
              <h5><b>Move to Group:</b></h5>
              <select v-model="moveToGroup">
                <option disabled value="">Select Group</option>
                <option v-for="selection in availableGroups" v-bind:value="selection.name">{{selection.name}}</option>
              </select>
              <div id="settings-error" class="hidden">
                <h4 class="error-message">You must select a new group or Sysmon configuration file to save new settings.</h4>
              </div>
            </div>
<!-- /.modal-body -->
            <div class="modal-footer">
              <button type="button" class="btn btn-primary" @click="saveSettings(selectedAgent.uuid, selectedConfig, selectedGroup, moveToGroup)">Save Settings</button>
              <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
            </div>
<!-- /.modal-footer -->
          </div>
        </div>
    </div>
<!-- End EDIT SYSMON CONFIG MODAL -->
</section>
</template>

<script>
  import Popper from 'vue-popperjs';
  import 'vue-popperjs/dist/vue-popper.css';
  import '../assets/_css/tooltips.css';
  import agentAPI from '../api/agents';
  import configAPI from '../api/configs';

  const loadingOverlay = $('#loadingOverlay');

  export default {
    name: 'AgentList',
    data() {
      return {
        agents: [],
        availableGroups: [],
        moveToGroup: '',
        groupedAgents:[],
        errors: [],
        sysmonConfigs: [],
        sysmonVersions: [],
        selectedAgent: '',
        selectedGroup: '',
        selectedConfig: '',
        selectedGroupConfig: '',
        selectedVersion: '',
        selectedGroupVersion: '',
        desiredGroupName: '',
        groupSaving: false,
        newConfigSaving: false,
        moveGroupSaving: false,
        settingsSaving: false,
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
      displayAgent(agent, group) {
        this.selectedAgent = agent;
        this.selectedGroup = group;
        //console.log(this.selectedAgent);
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
      getOverlayGroupClassName(groupName){
        return groupName;
      },
      showHideLoadingOverlay(groupName, allSelected = false){
        //Show / Hide all group loading overlays.
        if(groupName == 'allAgents' && allSelected){
          let allHostOverlays = $('.overlay.hostOverlays');
          let allOverlaysHidden = $('.overlay.hostOverlays').hasClass('hidden');
          //all loaders are visible, so hide them
          if(!allOverlaysHidden){
            allHostOverlays.addClass('hidden');
            return;
          }
          else{
            allHostOverlays.removeClass('hidden');
            return;
          }
        }

        //Show / Hide individual group loading overlays.
        let currentOverlay = $('.overlay.' + groupName);
        let currentLoadingOverlayHidden = $('.overlay.' + groupName).hasClass('hidden');
        //Loader is visible, so hide it
        if(!currentLoadingOverlayHidden){
          currentOverlay.addClass('hidden');
          return;
        }
        //Show loader
        currentOverlay.removeClass('hidden');
        return;
      },
      saveSettings(agentID, config = '', groupName, moveToGroup = '') {
        if(config == '' && moveToGroup == ''){
          $('#settings-error').removeClass('hidden');
          return;
        }
        else {
          $('#settings-error').addClass('hidden');
        }

        if(config || moveToGroup){
          this.showHideLoadingOverlay(groupName);
          this.settingsSaving = true;
        }

        if (config) {
          this.newConfigSaving = true;
          agentAPI.updateAgentConfig(agentID, config)
          .then((response) => {
            this.newConfigSaving = false;
            if(this.settingsSaving){
              if(!this.moveGroupSaving){
                this.showHideLoadingOverlay(groupName);
                this.settingsSaving = false;
              }
            }
            this.getHostList();
            //Debug
            //console.log(response);
          })
          .catch((e) => {
            this.newConfigSaving = false;
            if(!this.moveGroupSaving){
              this.showHideLoadingOverlay(groupName);
              this.settingsSaving = false;
            }
            console.log(e.message);
          });
        }
        if (moveToGroup) {
          this.moveGroupSaving = true;
          axios.patch(`http://localhost:8000/groups/${agentID}/${moveToGroup}`)
          .then((response) => {
            this.moveGroupSaving = false;
            if(this.settingsSaving){
              if(!this.newConfigSaving){
                this.showHideLoadingOverlay(groupName);
                this.settingsSaving = false;
              }
            }
            this.getHostList();
            //Debug
            //console.log(response);
          })
          .catch((e) => {
            this.moveGroupSaving = false;
            if(!this.newConfigSaving){
              this.showHideLoadingOverlay(groupName);
              this.settingsSaving = false;
            }
            console.log(e.message);
          });
        }
        $('#agent-modal').modal('hide');
        return;
      },
      saveGroup(groupName, groupConfig, version){
        if(groupName && groupConfig && version){
          console.log("group name:" + groupName);
          console.log("sysmon version:" + version);
          $('#create-group-error-message').addClass('hidden');
          $('#createGroupModal').modal('hide');
          this.groupSaving = true;
          axios({
            method:'post',
            url: `http://localhost:8000/groups/${groupName}`,
            data:{
              "sysmon_version":version,
              "configuration":groupConfig,
            }
          })
          .then((response) => {
            this.groupSaving = false;
            console.log(response);
          })
          .catch((e) => {
            this.groupSaving = false;
            console.log(e.message);
          });
        }
        else {
          $('#create-group-error-message').removeClass('hidden');
        }
      },
      runSysmon(agentID, groupName) {
        this.showHideLoadingOverlay(groupName);
        agentAPI.runSysmon(agentID)
          .then((response) => {
          console.log(response);
          this.showHideLoadingOverlay(groupName);
          this.getHostList();
        })
        .catch((e) => {
          console.log(e.message);
          this.showHideLoadingOverlay(groupName);
        });
      },
      installSysmon(agentID, groupName) {
        this.showHideLoadingOverlay(groupName);
        axios.patch(`http://localhost:8000/agents/${agentID}`)
        .then(() => {
          // Debug
          // console.log(response);
          this.showHideLoadingOverlay(groupName);
          this.getHostList();
        })
        .catch((e) => {
          this.showHideLoadingOverlay(groupName);
          console.log(e.message);
        });
      },
      uninstallSysmon(agentID, groupName) {
        this.showHideLoadingOverlay(groupName);
        agentAPI.uninstallSysmon(agentID)
        .then((response) => {
          // Debug
          //console.log(response);
         this.showHideLoadingOverlay(groupName);
          this.getHostList();
        })
        .catch((e) => {
          console.log(e.message);
          this.showHideLoadingOverlay(groupName);
        });
      },
      getHostList() {
        agentAPI.getAllAgents()
        .then((response) => {
          this.agents = response.data;
          const currentAgents = response.data;
          const currentGroups = this.availableGroups;
          console.log(this.availableGroups);

          //If agents belong to a group, add them to the groupedAgents object according to group name.
          //Else add them to the groupedAgents object as "unassigned"
          let currentGroupedAgents = {"unassigned":[]};
          for(let i = 0; i < currentGroups.length; i++){
            currentGroupedAgents[currentGroups[i]["name"]] = [];
          }
          for(let i = 0; i < currentAgents.length; i++){
            if(currentAgents[i]["group"]){
              currentGroupedAgents[currentAgents[i]["group"]].push(currentAgents[i]);
            }
            else {
              currentGroupedAgents["unassigned"].push(currentAgents[i]);
            }
          }
          this.groupedAgents = currentGroupedAgents;
          //console.log(currentGroupedAgents);
          // Debug
           // console.log(response.data);
        })
        .catch((e) => {
          console.log(e.message);
          this.errors.push(e);
        });
      },
      getAvailableGroups(){
        axios.get('http://localhost:8000/groups')
        .then((response) => {
          this.availableGroups = response.data;
          //Debug
          //console.log(response.data);
        })
        .catch((e) => {
          console.log(e.message);
        });
      },
      getAvailableSysmonConfigs() {
        configAPI.getAllConfigs()
        .then((response) => {
          this.sysmonConfigs = response.data;
          // Debug
           //console.log(response.data);
        })
        .catch((e) => {
          this.errors.push(e);
        });
      },
      getAvailableSysmonVersions() {
        axios.get('http://localhost:8000/sysmon')
        .then((response) => {
          this.sysmonVersions = response.data;
          // Debug
          //console.log(response.data);
        })
        .catch((e) => {
          this.errors.push(e);
          console.log(e.message);
        });
      },
      // Grab IDs from Selected Agents
      getSelectedAgentIDs() {
        this.checkedAgentsIDs = [];
        for (let i = 0; i < this.checkedAgents.length; i++) {
          this.checkedAgentsIDs.push(this.checkedAgents[i].uuid);
        }
      },
      // Grab all Agent Objects
      selectAllAgents() {
        this.checkedAgents = [];
        if (this.selectAll) {
          for (let i = 0; i < this.agents.length; i++) {
            this.checkedAgents.push(this.agents[i]);
          }
        }
        this.getSelectedAgentIDs();
      },
      // Grab only NEW && Selected agents
      selectedNewAgents() {
        this.checkedAgentsIDs = [];
        for (let i = 0; i < this.checkedAgents.length; i++) {
          if (this.checkedAgents[i].new_agent) {
            this.checkedAgentsIDs.push(this.checkedAgents[i].uuid);
          }
        }
      },
      manageAllAgents(groupName, allSelected) {
        switch (this.manageAllSelected) {
          case 'install':
            this.showHideLoadingOverlay(groupName, true);
            this.selectedNewAgents();
            agentAPI.installSysmonMultiple(this.checkedAgentsIDs)
            .then(() => {
              // Debug
              // console.log(response.data);
              this.showHideLoadingOverlay(groupName, true);
              this.getHostList();
            })
            .catch((e) => {
              console.log(e.message);
              this.showHideLoadingOverlay(groupName, true);
            });
          break;
          case 'restart':
            this.showHideLoadingOverlay(groupName, true);
            agentAPI.runSysmonMultiple(this.checkedAgentsIDs)
            .then(() => {
              // Debug
              // console.log(response.data);
              this.showHideLoadingOverlay(groupName, true);
              this.getHostList();
            })
            .catch((e) => {
              console.log(e.message);
              this.showHideLoadingOverlay(groupName, true);
            });
          break;
          case 'update':

          break;
          case 'config':

          break;
          case 'uninstall':
            this.showHideLoadingOverlay(groupName, true);
            agentAPI.uninstallSysmonMultiple(this.checkedAgentsIDs)
            .then(() => {
              // Debug
              // console.log(response.data);
              this.showHideLoadingOverlay(groupName, true);
              this.getHostList();
            })
            .catch((e) => {
              console.log(e.message);
              this.showHideLoadingOverlay(groupName, true);
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
      this.getAvailableGroups();
      this.getAvailableSysmonConfigs();
      this.getAvailableSysmonVersions();
      this.getHostList();
      this.timer = setInterval(this.getHostList, 10000);
      // Handle iCheckBox in the host list table head.
      const that = this;
      jQuery('#checkAll').change(() => {
        that.selectAllAgents();
        // Debug
        // console.log(that.selectAll);
        // console.log(that.checkedAgents);
      });
    },
    beforeDestroy() {
      clearInterval(this.timer);
    },
  };

</script>

<style scoped>
#controls-top {
  margin:0 0 20px 0;
}
#container-createGroupBtn {
  width:100%;
}
.error-message{
  color:rgb(221,75,57);
}

#group-list {
  list-style-type:none;
  padding-left:0;
}

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
td, th{
  cursor:default;
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
.modal-body{
  padding-top:0;
}
</style>
