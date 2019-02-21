<div>
  <div class="box">
    <div class="box-header with-border">
      <h4 class="box-title">
        Configurations
      </h4>
    </div>
    <!-- /.box-header -->
    <div class="box-body">
      <table class="table no-margin">
        <thead>
          <tr>
            <th>Name</th>
            <th>Is Default?</th>
            <th class="center-text icon-column">Edit</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="config in configs" :key="config.name">
            <td>{{ config.name }}</td>
            if(config.isDefault){
            { <td> Default </td>
            <td class="center-text">
              <a>
                <i class="fa fa-play"></i>
              </a>
            </td>
            <td class="center-text">
              <a @click="editConfig(config.name)">
                <i class="fa fa-trash"></i>
              </a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <script>
      import configs from '../../configsList.json';

      export default {
        name: 'ConfigList',
        data() {
          var newConfig;
          return {
            configs,
            newConfig,
            editConfig:'',
          }
        },
        methods:{
          newConfig(config){
            this.newConfig = config;
          },
          editConfig(config){
            //To do:  need to make a call to update associated config file.
            if(config){
              console.log(config);
              $('#agent-modal').modal('hide');
            }
            else {
              console.log('No selection made.');
            }
          },
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
</div>
</div>
