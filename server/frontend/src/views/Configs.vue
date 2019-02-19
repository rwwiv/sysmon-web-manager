<template>
	<section class="content container-fluid">
		<h1>Configuration Management</h1>
    <div class = "list-header-row">
		<button>
		Add New Configuration
		</button>
    <!-- <ul v-if "configs.length">
           <ConfigListItem
             v-for=config in configs"
             :key="config.name"
             :config = "config"
             @delete="deleteConfig"
             @edit="editConfig"
             @view="viewConfig"
             />
            </ul>
            <p v-else>
              No configurations. Click add new to make a new configuration.
            </p>
            -->
    </div>
      <div class="config row">
        <div class="col-xs-6">
          <h3>Available Configurations</h3>
          <!-- Named Configurations -->
          <!-- To do: need a component to drive li element generation -->
          <ul class="list-group list-all-configs">
            <li class="list-group-item" id="configID_default2">
              <div class="box box-solid box-host">
                <div class="box-header">
                  <h4 class="box-title"><i class="fa fa-circle text-success"></i>Default Configuration</h4>
                  <div class="box-tools pull-right">
									<button>
                    View
                  </button>
									<button>
                    Edit
                  </button>
									<button>
                    Delete
                  </button>
                    <i class="fa fa-play"></i>
                    <i class="fa fa-wrench"></i>
                    <i class="fa fa-trash"></i>
                  </div>
                </div>
              </div>
            </li>
            <li class="list-group-item" id="configID_1">
              <div class="box box-solid box-host">
                <div class="box-header">
                  <h4 class="box-title"><i class="fa fa-circle text-success"></i>Configuration 1</h4>
                  <div class="box-tools pull-right">
									<button>
                    View
                  </button>
									<button>
                    Edit
                  </button>
									<button>
                    Delete
                  </button>
                    <i class="fa fa-play"></i>
                    <i class="fa fa-wrench"></i>
                    <i class="fa fa-trash"></i>
                  </div>
                </div>
              </div>
            </li>
            <li class="list-group-item" id="configID_default">
              <div class="box box-solid box-host">
                <div class="box-header">
                  <h4 class="box-title"><i class="fa fa-circle text-success"></i>Configuration 2</h4>
                  <div class="box-tools pull-right">
									<button>
                    View
                  </button>
									<button>
                    Edit
                  </button>
									<button>
                    Delete
                  </button>
                    <i class="fa fa-play"></i>
                    <i class="fa fa-wrench"></i>
                    <i class="fa fa-trash"></i>
                  </div>
                </div>
              </div>
            </li>
          </ul>
			</div>
			<!-- Sysmon Configs -->
			<!-- To do:  Need a component to drive config li element generation -->
			</div>
	</section>
</template>
<!--<script>

import HelloWorld from './components/HelloWorld.vue';

<script>
export default {
  components: {
    HelloWorld,
  },
};
</script>

Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
	input[type="checkbox"]{
		margin-right:10px;
	}

	.list-group{
		padding:10px;
		overflow-y:scroll;
		max-height:400px;
	}


	.list-group-item {
		padding:0px;
		border:0px;
		background-color:transparent;
		position:relative;

		i {
			margin-right:15px;
		}

		input[type="checkbox"],
		input[type="radio"]{
			position:absolute;
			width:5%;
			top:0;
		}
	}

	.list-group-item:last-child{
		.box{
			margin-bottom:0;
		}
	}
	.box {
		width:95%;
		left:5%;
	}
	.box-host {
		border:1px solid #d2d6de;
	}

	.box-host > .box-header{
		background-color:#f3f3f3;
	}
	.box-tools {
		i:last-child{
			margin-right:0;
		}
	}
</style>
