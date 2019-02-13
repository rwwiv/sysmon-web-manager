<template>
	<section class="content container-fluid">
		<h1>Monitor</h1>
	  	<div class="monitor row">
	  		<div class="col-xs-6">
	  			<h3>Available Hosts</h3>
	  			<h4><input type="checkbox" name="selectAll"/>Select All</h4>
	  			<!-- Individual Hosts -->
	  			<!-- To do: need a component to drive li element generation -->
		    	<ul class="list-group list-all-hosts">
		    		<li class="list-group-item" id="hostID_1">
		    			<input type="checkbox" name="hostID_1"/>
		    			<div class="box box-solid box-host">
		    				<div class="box-header">
		    					<h4 class="box-title"><i class="fa fa-circle text-success"></i>Host 1</h4>
		    					<div class="box-tools pull-right">
		    						<i class="fa fa-play"></i>
		    						<i class="fa fa-wrench"></i>
		    						<i class="fa fa-trash"></i>
		    					</div>
		    				</div>
		    				<div class="box-body">
		    					IP Address / Network
		    				</div>
		    			</div>
		    		</li>
		    		<li class="list-group-item" id="hostID_2">
		    			<input type="checkbox" name="hostID_2"/>
		    			<div class="box box-solid box-host">
		    				<div class="box-header">
		    					<h4 class="box-title"><i class="fa fa-circle text-danger"></i>Host 2</h4>
		    					<div class="box-tools pull-right">
		    						<i class="fa fa-play"></i>
		    						<i class="fa fa-wrench"></i>
		    						<i class="fa fa-trash"></i>
		    					</div>
		    				</div>
		    				<div class="box-body">
		    					IP Address / Network
		    				</div>
		    			</div>
		    		</li>
		    		<li class="list-group-item" id="hostID_3">
		    			<input type="checkbox" name="hostID_3"/>
		    			<div class="box box-solid box-host">
		    				<div class="box-header">
		    					<h4 class="box-title"><i class="fa fa-circle text-default"></i>Host 3</h4>
		    					<div class="box-tools pull-right">
		    						<i class="fa fa-play"></i>
		    						<i class="fa fa-wrench"></i>
		    						<i class="fa fa-trash"></i>
		    					</div>
		    				</div>
		    				<div class="box-body">
		    					IP Address / Network
		    				</div>
		    			</div>
		    		</li>


		    	</ul>
			</div>
			<!-- Sysmon Configs -->
			<!-- To do:  Need a component to drive config li element generation -->
			<div class="col-xs-6">
				<h3>Available Sysmon Configurations</h3>
		    	<ul class="list-group">
		    		<li class="list-group-item">
						<input type="radio" name="config_select"/>
		    			<div class="box box-solid box-host">
		    				
		    				<div class="box-body">
		    					Config Name
		    				</div>
		    			</div>
		    		</li>
		    	</ul>
	    	</div>
	  	</div>
	  	

	</section>
</template>

<script>

import HelloWorld from '../components/HelloWorld.vue';
export default {
	components: {
		HelloWorld
	},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
	input[type="checkbox"]{
		margin-right:10px;
	}

	.list-group{
		padding:10px;
		overflow-y:scroll;
		max-height:400px;
	}

	.list-all-hosts {
		/*background-color:#e1e7ef;*/
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