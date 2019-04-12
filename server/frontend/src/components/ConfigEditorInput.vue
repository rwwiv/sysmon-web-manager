<template>
  <div>
    <button class= "btn btn-secondary pull-left">Select a file to add a new configuration. <input type= "file" @change="loadConfig"></button>
      <textarea id="inputTextToSave" v-model="text" @loadstart="loadConfig" @change="didNotValidate()"></textarea>
    <button class="btn btn-secondary pull-left" @click="validateConfig">Validate</button>
    <label for="configNameBox"> Configuration Name</label><input type="text" @change="nameConfig(configNameBox.value)" id="configNameBox" width="auto" v-model="text">
    <button class="btn btn-secondary pull-right" @click="saveConfig">Save Changes </button>
    <b></b>
    <input type="checkbox" name="makeDefault" value="isDefault">Check the box to set this configuration as the default.<br>
    <parsererror id = "errorBox" v-model="text">
    <sourcetext></sourcetext>
</parsererror>
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
        file: '',
        inputTextToSave: '',
      };
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
          this.file = file;
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
          if (responseStatus !== 400) {
            confirmMsg = 'You are about to save this new configuration. Press OK to proceed or cancel to make changes.';
          } else {
            confirmMsg = 'You are about to make changes to an existing configuration. Press OK to proceed. To make a new configuration instead, cancel and then change the configuration name.';
          } // this works
          if (confirm(confirmMsg)) { // need to first convert to xml from string and then check if valid
             this.inputTextToSave = document.getElementById('inputTextToSave').value;
             const formData = new FormData();
             formData.append('file', this.file);
             axios.post(`http://localhost:8000/configs/${this.configName}`, formData, {
             headers: {
                 'Content-Type': 'multipart/form-data',
               },
             }).then((response) => {
              responseStatus = response.status; // this works but the inputText may not
              }); // , document.getElementById('isDefault').checked
            document.getElementById('inputTextToSave').value = 'File saved.';
            document.getElementById('configNameBox').value = '';
            document.getElementById('isDefault').checked = false;
          }
          // not sure how to send the text data back to the server
        }
      },
      validateConfig() { // check encoding?
        var helper = new DOMParser();
        document.getElementById('errorBox').value = helper.parseFromString(this.inputTextToSave, 'application/xml');
        this.XMLconfig = helper.parseFromString(this.inputTextToSave, 'application/xml');
        // if(this.XMLconfig)
        this.didValidate = 1;
        alert('Validation Complete');
        // alert('XML Parsing Error');
       // this.didValidate = 0;
       // if ((this.XMLconfig))
      //  {
      //  }
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

</style>
