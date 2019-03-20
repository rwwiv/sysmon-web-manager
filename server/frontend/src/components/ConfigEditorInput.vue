<template>
  <div style="display: block;" id="configEd">
    <xml id="config" src="../sysmonconfig-export.xml"></xml>
  <label for="configEd" id="configEdLabel">Edit configuration. Validate and save using the buttons below.</label>
    <div class="textWrapper"><textarea cols="2" rows="20" id="editingConfig"></textarea></div>
  <div class="col-auto">
    <button class="btn btn-secondary pull-left">Validate</button>
    <button class="btn btn-secondary pull-right">Save Changes</button>
  </div>
  </div>
</template>
<script>
    export default {
        name: 'ConfigEditorInput.vue',
    };
</script>

<style scoped>
  textarea
  {
    width:100%;
    overflow-y: auto;
    overflow-x: auto;
  }
  .textWrapper
  {
    border:1px solid #999999;
    margin:5px 0;
    padding:3px;
  }
</style>
