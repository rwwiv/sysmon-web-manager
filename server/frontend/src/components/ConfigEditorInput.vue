<template>
  <div>
    <button class= "btn btn-secondary pull-left">Select a file to add a new configuration. <input type= "file" @change="loadConfig"></button>
      <textarea id="inputTextToSave" v-model="text" @loadstart="loadConfig" @change="didNotValidate()"></textarea>
    <button class="btn btn-secondary pull-left" @click="validateConfig">Validate</button>
    <label for="configNameBox"> Configuration Name</label><input type="text" @change="nameConfig(document.getElementById('configNameBox').value)" id="configNameBox" width="auto" v-model="text">
    <button class="btn btn-secondary pull-right" @click="saveConfig()">Save Changes </button>
    <b></b>
    <input type="checkbox" name="makeDefault" value="isDefault" aria-labelledby="default-checkbox">Check the box to set this configuration as the default.<br>
    <!--<div class="modal fade" id="confirm-modal" tabindex="-1" role="dialog" aria-labelledby="confirm-modal-label">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h3>Confirm Save Configuration</h3>
            <h4 class="modal-title"><b>Name:</b> {{this.configName}}</h4>
          </div>
          &lt;!&ndash; /.modal-header &ndash;&gt;
          <div class="modal-body">
            <h5>{{existingConfig(this.configName) ? 'You are about to make changes to an existing configuration. Press OK to proceed. To make a new configuration instead, cancel and then change the configuration name.' : 'You are about to save this new configuration. Press OK to proceed or cancel to make changes.'}}</h5>
          </div>
          &lt;!&ndash; /.modal-body &ndash;&gt;
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" @click="saveConfig()">OK</button>
            <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>
          </div>
          &lt;!&ndash; /.modal-footer &ndash;&gt;
        </div>
      </div>
    </div>
    &lt;!&ndash; End EDIT SYSMON CONFIG MODAL &ndash;&gt;
    <div class="modal fade" id="validate-modal" tabindex="-1" role="dialog" aria-labelledby="validate-modal-label">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h3>Validate Configuration</h3>
            <h4 class="modal-title"><b>Name:</b> {{this.configName}}</h4>
          </div>
          &lt;!&ndash; /.modal-header &ndash;&gt;
          <div class="modal-body">
            <h5>Please validate the configuration before saving.</h5>
          </div>
          &lt;!&ndash; /.modal-body &ndash;&gt;
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Ok</button>
          </div>
          &lt;!&ndash; /.modal-footer &ndash;&gt;
        </div>
      </div>
    </div>-->
    <!-- End EDIT SYSMON CONFIG MODAL -->
  </div>
</template>
<script>
  import axios from 'axios';

  export default {
    name: 'ConfigEditorInput.vue',
    data() {
      return {
        configName: '',
        isDefault: '',
        didValidate: '',
        existingConfig: '',
        overwriteExisting: '',
        XMLconfig: XMLDocument,
        file: '',
        inputTextToSave: '',
      };
    },
    beforeCreated() {},
    created() {
      axios.get('http://localhost:8000/configs/', this.$router.params.id).then((response) => { this.file = response.data; });
      this.configName = this.$route.params.id;
      alert(this.configName);
    },
    mounted() {},
    beforeDestroy() {},
    destroy() {},

    methods: {
      // getParams() {
      //   const vars = {};
      //   const parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, (m, key, value) => {
      //     vars[key] = value;
      //     console.log(vars);
      //     alert('did the url parsing');
      //   });
      //   return vars;
      // },

// Now you can get the parameters you want like so:
      //    var abc = params.abc;

      nameConfig(name) {
        this.configName = name;
      },
      loadConfig(ev) {
        const file = ev.target.files[0];
        const reader = new FileReader();

        function onload(fileLoadedEvent) {
          document.getElementById('inputTextToSave').value = fileLoadedEvent.target.result;
          document.getElementById('configNameBox').value = file.name;
          this.file = file;
        }

        reader.onload = onload;
        reader.readAsText(file);
      },
      didNotValidate() {
        this.didValidate = 0;
      },
      checkExistingConfig(name) {
        axios.get('http://localhost:8000/configs/', name).then((response) => {
          if (response.status !== 400) this.existingConfig = 0;
          else this.existingConfig = 1;
        });
      },
      saveConfig() {
        this.configName = document.getElementById('configNameBox').value;
        // this works
        this.inputTextToSave = document.getElementById('inputTextToSave').value;
        axios.get('http://localhost:8000/configs/', this.configName).then((response) => {
          if (response.status !== 400) this.existingConfig = 0;
          else this.existingConfig = 1;
        });
        if (this.didValidate === 0) $('#validate-modal').modal('hide');
        if (this.existingConfig === 1 && this.overwriteExisting === 0) {
              $('#confirm-modal').modal('hide');
            }
        const formData = new FormData();
        formData.append('file', this.file);
        axios.post(`http://localhost:8000/configs/${this.configName}`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        }).then((response) => {
          console.log(response.status);
        }); // , document.getElementById('isDefault').checked
        document.getElementById('inputTextToSave').value = 'File saved.';
        document.getElementById('configNameBox').value = '';
        document.getElementById('isDefault').checked = false;
        // not sure how to send the text data back to the server
      },
      validateConfig() { // check encoding?
        const helper = new DOMParser();
        document.getElementById('errorBox').value = helper.parseFromString(this.inputTextToSave, 'application/xml');
        this.XMLconfig = helper.parseFromString(this.inputTextToSave, 'application/xml');
        this.didValidate = 1;
        alert('Validation Complete');
        // alert('XML Parsing Error');
        // this.didValidate = 0;
        // if ((this.XMLconfig))
        //  {
        //  }
      },
      mounted() {
        this.configName = this.getParams().id;
        alert(this.configName); // says undefined
        axios.get('http://localhost:8000/configs/', this.configName).then((response) => {
          this.inputTextToSave = response;
        });
        document.getElementById('inputTextToSave').value = this.inputTextToSave;
        document.getElementById('configNameBox').value = this.configName;
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
