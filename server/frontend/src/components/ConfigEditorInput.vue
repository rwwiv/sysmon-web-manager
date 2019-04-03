<template>
  <div>
    <button class= "btn btn-secondary pull-left">Select a file to add a new configuration. <input type= "file" @change="loadConfig"></button>
      <textarea id="inputTextToSave" v-model="text" @loadstart="loadConfig" @change="didNotValidate()"></textarea>
    <button class="btn btn-secondary pull-left" @click="validateConfig">Validate</button>
    <label for="configNameBox"> Configuration Name</label><input type="text" @change="nameConfig(configNameBox.value)" id="configNameBox" width="auto" v-model="text">
    <button class="btn btn-secondary pull-right" @click="saveConfig">Save Changes </button>
  </div>
</template>
<script>
  import axios from 'axios';

  export default {
    name: 'ConfigEditorInput.vue',
    data() {
      return {
        configName: '',
        didValidate: '',
        XMLconfig: XMLDocument,
        inputTextToSave: '',
      }
    },
    methods: {
      nameConfig(name) {
        this.configName = name;
      },
      loadConfig(ev) {
        const file = ev.target.files[0];
        const reader = new FileReader();
        reader.onload = function (fileLoadedEvent) {
          document.getElementById('inputTextToSave').value = fileLoadedEvent.target.result;
          document.getElementById('configNameBox').value = file.name;
        };
        reader.readAsText(file);
      },
      didNotValidate(){
        this.didValidate = 0;
      },
      saveConfig() {
        let confirmMsg;
        let responseStatus;
        if (this.didValidate === 0) {
          confirm('Please validate before saving.');// this works
        } else {
          this.configName = document.getElementById('configNameBox').value;
          axios.get('http://localhost:8000/configs/', this.configName).then((response) => {
            responseStatus = response.status;
          });
          if (responseStatus !== '400') {
            confirmMsg = 'You are about to save this new configuration. Press OK to proceed or cancel to make changes.';
          } else {
            confirmMsg = 'You are about to make changes to an existing configuration. Press OK to proceed. To make a new configuration instead, cancel and then change the configuration name.';
          } // this works
          if (confirm(confirmMsg)) {
             this.inputTextToSave = document.getElementById('inputTextToSave').value;
             axios.post(`http://localhost:8000/configs/${this.configName}`, this.inputTextToSave.value).then((response) => {
              responseStatus = response.status; // this works
              });
            document.getElementById('inputTextToSave').value = 'File saved.';
            document.getElementById('configNameBox').value = '';
          }
          // not sure how to send the text data back to the server
        }
      },
      validateConfig() {
        const helper = new DOMParser();
        try {
          this.XMLconfig = helper.parseFromString(this.inputTextToSave, 'text/xml'); // this never throws an exception
          // alert(inputTextToSave.toString());
          this.didValidate = 1;
          alert('Validation Complete');
        } catch (e) {
          alert('XML Parsing Error');
          this.didValidate = 0;
          // alert(e.getError());
          // alert(result.value.toString());
        }
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
