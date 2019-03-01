<template>
  <div class="box">
    <div class="box-header with-border">
      <h4 class="box-title">
        Agents
      </h4>
    </div>
    <!-- /.box-header -->
    <div class="box-body">
      <table class="table no-margin">
        <thead>
          <tr>
            <th>IP Address</th>
            <th>Status</th>
            <th>Config</th>
            <th class="center-text">Version</th>
            <th class="center-text icon-column">Manage</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="agent in agents" :key="agent.id">
            <td>{{ agent.ip_address ? agent.ip_address : 'N/A' }}</td>
            <td>
              <span class="label" :class="currentStatusLabel(agent.online, agent.needs_install)">
              {{ currentStatusText(agent.online, agent.needs_install) }}
            </span>
            </td>
            <td>{{ agent.config_name_current ? agent.config_name_current : 'N/A' }}</td>
            <td class="center-text">{{ agent.sysmon_version_current ? agent.sysmon_version_current : 'N/A' }}</td>
            <td class="center-text control-icons">
              <a @click="runSysmon(agent.uuid)">
                <i class="fa fa-play"></i>
              </a>
              <a data-toggle="modal" data-target="#agent-modal" @click="displayAgent(agent)">
                <i class="fa fa-wrench"></i>
              </a>
              <a @click="uninstallSysmon(agent.uuid)">
                <i class="fa fa-trash"></i>
              </a>
            </td>
            
          </tr>
        </tbody>
      </table>
    </div>
    <!-- /.box-body -->

    <!-- Modal -->
    <div class="modal fade" id="agent-modal" tabindex="-1" role="dialog" aria-labelledby="agent-modal-label">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
              <h4 class="modal-title"><b>IP:</b> {{selectedAgent.ipAddress ? selectedAgent.ipAddress : 'Agent/Host location unknown.'}}</h4>
            </div>
            <!-- /.modal-header -->
            <div class="modal-body">
              <h5><b>Current Sysmon Config:</b><br/>{{selectedAgent.config_name_current ? selectedAgent.config_name_current : 'No configuration file is currently associated with this agent/host.'}}</h5>
              <h5><b>Available Sysmon Configs:</b></h5>
                <select v-model="selectedConfig">
                  <option disabled value="">Select New Sysmon Config</option>
                  <option v-for="config in availableSysmonConfigs" :key="config.id" v-bind:value="config.name">{{config.name}}</option>
                </select>
                <router-link v-if="selectedConfig" class="edit-config-link" :to="{name: 'management', query:{configFile: selectedConfig}}" data-dismiss="modal">
                  <i class="fa fa-gear"></i> Edit this config file.
                </router-link>
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
    <!-- /.Modal -->

  </div>
  <!-- /.box -->
</template>

<script>
  import axios from 'axios';
  /***
  * To Do: the available configs needs to come from the /configs API call
  * which is non-functional as of 2-27-19.
  ***/
  import availableSysmonConfigs from '../../agentAvailableSysmonConfigSample.json';

  export default {
    name: 'AgentList',
    data() {
      return { 
        agents: [],
        errors: [],
        availableSysmonConfigs,
        selectedAgent: '',
        selectedConfig:'',
      }
    },
    methods:{
      displayAgent(agent){
        this.selectedAgent = agent;
      },
      currentStatusLabel(agentStatus, needsInstall){
        if(needsInstall){
          return 'label-primary';
        }
        if(agentStatus){
          return 'label-success';
        }
        return 'label-danger';
      },
      currentStatusText(agentStatus, needsInstall){
        if(needsInstall){
          return 'New';
        }
        if(agentStatus){
          return 'Online';
        }
        return 'Offline';
      },
      runSysmon(agentID){
        //As of 2-27-19 this API call responds with a 404
        axios.post('http://127.0.0.1:8000/agents/'+agentID)
        .then(response =>{
          console.log(response);
          this.getHostList();
        })
        .catch(e =>{
          console.log(e.message);
        });
      },
      saveConfig(agentID, config){
        //To Do:  On successful patch, need to update list view to reflect change in selected config.  
        //As of 2-27-19 this API call responds with a 404
        if(config){
          axios.patch('http://127.0.0.1:8000/agents/'+agentID+'/config/'+config)
          .then(response =>{
            console.log(response);
          })
          .catch(e =>{
            console.log(e.message);
          });
          $('#agent-modal').modal('hide');
          this.getHostList();
        }
        else {
          console.log('No selection made.');
        }
      },
      uninstallSysmon(agentID){
        //As of 2-27-19 this API call responds with a 404
        axios.delete('http://127.0.0.1:8000/agents/'+agentID)
        .then(response =>{
          console.log(response);
          this.getHostList();
        })
        .catch(e => {
          console.log(e.message);
        });
      },
      getHostList(){
        axios.get('http://127.0.0.1:8000/agents', { crossdomain: true })
        .then(response => {
          this.agents = response.data;
          console.log(response.data);
        })
        .catch(e => {
          this.errors.push(e)
        })
      }
    },
    mounted:function(){
      this.getHostList();
    }
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
  width:20%;
}
.control-icons a {
  margin-right:10%;
}
.control-icons a:last-child {
  margin-right:0;
}
.edit-config-link{
  margin-left:10px;
  cursor:pointer;
}
</style>
