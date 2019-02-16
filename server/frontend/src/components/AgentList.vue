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
            <th>IP Addr.</th>
            <th>Status</th>
            <th>Config Name</th>
            <th class="center-text">Sysmon Version</th>
            <th class="center-text icon-column">Run</th>
            <th class="center-text icon-column">Settings</th>
            <th class="center-text icon-column">Remove</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="agent in agents" :key="agent.id">
            <td>{{ agent.ipAddress }}</td>
            <td>
              <span class="label" :class="currentStatusLabel(agent.status)">
              {{ agent.status }}
            </span>
            </td>
            <td>{{ agent.config }}</td>
            <td class="center-text">{{ agent.version }}</td>
            <td class="center-text">
              <a>
                <i class="fa fa-play"></i>
              </a>
            </td>
            <td class="center-text">
              <a data-toggle="modal" data-target="#agent-modal" @click="displayAgent(agent)">
                <i class="fa fa-wrench"></i>
              </a>
            </td>
            <td class="center-text">
              <a @click="uninstallSysmon(agent.id)">
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
              <h4 class="modal-title"><b>IP:</b> {{selectedAgent.ipAddress}}</h4>
            </div>
            <!-- /.modal-header -->
            <div class="modal-body">
              <h5><b>Current Sysmon Config:</b><br/>{{selectedAgent.config}}</h5>
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
              <button type="button" class="btn btn-primary" @click="saveConfig(selectedAgent.id, selectedConfig)">Save changes</button>
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
  import agents from '../../agentSample.json';
  import availableSysmonConfigs from '../../agentAvailableSysmonConfigSample.json';

  export default {
    name: 'AgentList',
    data() {
      return { 
        agents,
        availableSysmonConfigs,
        selectedAgent: '',
        selectedConfig:'',
      }
    },
    methods:{
      displayAgent(agent){
        this.selectedAgent = agent;
      },
      currentStatusLabel(agentStatus){
        switch (agentStatus){
          case 'running':
            return 'label-success';
          break;
          case 'offline':
            return 'label-danger';
          break;
          default:
            return 'label-default';
          break;
        }
      },
      saveConfig(agentID, config){
        //To do:  need to make a call to update associated config file.
        if(config){
          console.log(config);
          $('#agent-modal').modal('hide');
        }
        else {
          console.log('No selection made.');
        }
      },
      uninstallSysmon(agentID){
        //To do:  need to make a call to remove this from DB / remove sysmon from host.
        console.log(agentID);
      }
    },
    mounted:function(){
      //To do:  need to access data locally on load.
      // this.$http.get('http://localhost:80/agentSample.json').then((data)=>{
      //   console.log(data.body)
      // });
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
  width:10%;
}
.edit-config-link{
  margin-left:10px;
  cursor:pointer;
}
</style>
