<template>
  <div>
    <button class= "btn btn-secondary pull-left">Select a file to add a new configuration. <input type= "file" @change="loadConfig"></button>
      <textarea id="inputTextToSave" v-model="text" @loadstart="loadConfig"></textarea>
    <button class="btn btn-secondary pull-left">Validate</button>
    <label for="configName"> Configuration Name</label><input type="text" @change="nameConfig(configName.data)" id="configName" width="auto" v-model="text">
    <button class="btn btn-secondary pull-right" @click="saveConfig">Save Changes </button>
  </div>
</template>
<script>
  import axios from 'axios';

  let configName;
  export default {
        // name: 'ConfigEditorInput.vue',

        methods: {
          nameConfig(name) {
            configName = name;
          },
          loadConfig(ev) {
            const file = ev.target.files[0];
            const reader = new FileReader();
            reader.onload = function (fileLoadedEvent) {
              document.getElementById('inputTextToSave').value = fileLoadedEvent.target.result;
              document.getElementById('configName').value = file.name;
            };
            reader.readAsText(file);
          },
          saveConfig() {
            let confirmMsg;
            let responseStatus;
            axios.get(`http://localhost:8000/configs/${configName}`).then((response) => {
              responseStatus = response.status;
            })
            if (responseStatus !== '400') {
              confirmMsg = 'You are about to save this new configuration. Press OK to proceed or cancel to make changes.';
            } else {
              confirmMsg = 'You are about to make changes to an existing configuration. Press OK to proceed. To make a new configuration, change the configuration name.'
            }
            if (confirm(confirmMsg)) {
              const textToSave = document.getElementById('inputTextToSave').value;
              document.getElementById('inputTextToSave').value = 'File saved.';
            }
            // not sure how to send the text data back to the server
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
