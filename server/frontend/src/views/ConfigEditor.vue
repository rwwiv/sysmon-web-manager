<template>
  <section class="content">
    <div class="row">
      <div class="col-md-12">
        <div>
          <button class= "btn btn-secondary pull-left">Select a file to add a new configuration. <input type= "file" @change="loadConfig"></button>
          <label for="inputTextToSave"></label><textarea id="inputTextToSave" v-model="text" @loadstart="loadConfig" @change="didNotValidate()"></textarea>
          <button class="btn btn-secondary pull-left" @click="validateConfig">Validate</button>
          <label for="configNameBox"> Configuration Name</label><input type="text" @change="nameConfig(document.getElementById('configNameBox').value)" id="configNameBox" width="auto" v-model="text">
          <button class="btn btn-secondary pull-right" @click="saveConfig()">Save Changes </button>
          <b></b>
          <label>
            <input type="checkbox" name="makeDefault" value="isDefault" aria-labelledby="default-checkbox">
          </label>Check the box to set this configuration as the default.<br>

      </div>
    </div>
    </div>
  </section>
</template>

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
    beforeCreated() {
      console.log('beforeCreated');
      this.configName = this.$route.params.id;
      console.log(this.configName);
      console.log(this.route);
    },
    created() {
      console.log('created');
      console.log(this.$route.params.id);
      // alert(this.$route.params.id);
    },
    mounted() {
      this.configName = this.$route.params.id;
      document.getElementById('configNameBox').value = this.configName;
      document.getElementById('inputTextToSave').value = 'eventually the config';
      axios.get('http://localhost:8000/configs/', this.configName).then((response) => { this.file = response.data; });
      function onload(fileLoadedEvent) {
        document.getElementById('inputTextToSave').value = fileLoadedEvent.target.result;
        document.getElementById('configNameBox').value = this.file.name;
      }
      const reader = new FileReader();
      reader.onload = onload;
      this.inputTextToSave = reader.readAsText(this.file);
    },
    beforeDestroy() {},
    destroy() {},

    methods: {
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
        console.log(this.configName);
        // this works
        this.inputTextToSave = document.getElementById('inputTextToSave').value;
        console.log(this.inputTextToSave);
        axios.post('http://localhost:8000/configs/', this.configName);
        // axios.put('http://localhost:8000/configs/', this.configName, this.file).then((response) => { console.log(response); });
        axios
          .put(
            'http://localhost:8000/configs/',
            { NAME: this.configName, IS_DEFAULT: document.getElementById('makeDefault').value.checked(), data: this.inputTextToSave },
            { headers: { 'Content-Type': 'text/plain' } },
          )
          .then(r => console.log(r.status))
          .catch(e => console.log(e));
        // axios.get('http://localhost:8000/configs/', this.configName).then((response) => {
        //   if (response.status !== 400) this.existingConfig = 0;
        //   else this.existingConfig = 1;
        // });
        // if (this.didValidate === 0) $('#validate-modal').modal('hide');
        // if (this.existingConfig === 1 && this.overwriteExisting === 0) {
        //   $('#confirm-modal').modal('hide');
        // }
        // const formData = new FormData();
        // formData.append('file', this.file);
        // axios.post(`http://localhost:8000/configs/${this.configName}`, formData, {
        //   headers: {
        //     'Content-Type': 'multipart/form-data',
        //   },
        // }).then((response) => {
        //   console.log(response.status);
        // }); // , document.getElementById('isDefault').checked
        // document.getElementById('inputTextToSave').value = 'File saved.';
        // document.getElementById('configNameBox').value = '';
        // document.getElementById('isDefault').checked = false;
        // // not sure how to send the text data back to the server
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
        this.configName = this.$route.params.id;
        alert(this.configName); // says undefined
        axios.get('http://localhost:8000/configs/', this.configName).then((response) => {
          this.inputTextToSave = response;
        });
        document.getElementById('inputTextToSave').value = this.inputTextToSave;
        document.getElementById('configNameBox').value = this.configName;
      },
    },
  };

  // import axios from 'axios';

  // import ConfigEd from '../components/ConfigEditorInput.vue';

  $(document).ready(() => {
    $('input').iCheck({
      checkboxClass: 'icheckbox_minimal-blue',
      radioClass: 'iradio_minimal-blue',
    });
  });
</script>

<style scoped>

</style>
