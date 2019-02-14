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
            <th>Sysmon Version</th>
            <th>Run</th>
            <th>Settings</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="agent in agents" :key="agent.id">
            <td>{{ agent.ipAddress }}</td>
            <td>
              <span class="label label-success" :class="[statusClass]">
              {{ agent.status }}
            </span>
            </td>
            <td>{{ agent.config }}</td>
            <td>{{ agent.version }}</td>
            <td>
              <a>
                <i class="fa fa-play"></i>
              </a>
            </td>
            <td>
              <a>
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
  import agents from '../../agentSample.json';

  export default {
    name: 'AgentList',
    data() {
      return { agents };
    },
  };

</script>

<style scoped>

</style>
