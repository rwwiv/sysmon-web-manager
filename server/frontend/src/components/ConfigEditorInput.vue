<template>
  <div>
    <button class= "btn btn-secondary pull-left">Select a file to add a new configuration. <input type= "file" @change="loadConfig"></button>
      <textarea id="inputTextToSave" v-model="text" @loadstart="loadConfig"></textarea>
    <button class="btn btn-secondary pull-left">Validate</button>
    <button class="btn btn-secondary pull-right">Save Changes</button>
  </div>
</template>
<script>
  import axios from 'axios';

  export default {
        // name: 'ConfigEditorInput.vue',
        methods: {
          loadConfig(ev) {
            const file = ev.target.files[0];
            const reader = new FileReader();
            reader.onload = function (fileLoadedEvent) {
              document.getElementById('inputTextToSave').value = fileLoadedEvent.target.result;
            };
            reader.readAsText(file);
          },
          viewConfig() {
            axios.get('http://localhost:8080/file.txt').then(response => response.data);
          },
        },
    };
</script>

<style scoped>
  textarea
  {
    width:100%;
    height: 30em;
    min-height: fit-content;
    overflow-y: auto;
    overflow-x: auto;
  }
  textWrapper
  {
    border:1px solid #999999;
    margin:5px 0;
    padding:3px;
  }
</style>
