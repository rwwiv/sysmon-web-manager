<template>
  <section class="content">
    <div class="container">

      <div class="box">
        <div class="box-header with-border">
          <div class="row">
            <div class="col-lg-4">
              <div class="input-group">
                <span class="input-group-addon">
                  Default?
                  <input type="checkbox" id="makeDefault" @click="makeDefault()" :checked="this.defaultCheck">
                </span>
                <input
                  type="text"
                  class="form-control"
                  id="configNameBox"
                  width="auto"
                  v-model="configName"
                  placeholder="Configuration name"
                >
                <span class="input-group-addon">.xml</span>
              </div>
            </div>
          </div>
        </div>
        <div class="box-body">
          <codemirror
            v-model="inputTextToSave"
            @change="didValidate = false"
            :options="cmOptions"></codemirror>
        </div>
        <div class="box-footer">
          <label class="btn btn-default btn-file">
            Browse for file <input type="file" style="display: none;" @input="loadConfig()" id="file">
          </label>
          <button class="btn btn-default pull-right" type="submit" @click="submitConfig()">Save Configuration</button>
        </div>
      </div>
      <div class="alert alert-warning alert-dismissible" role="alert" v-if="isValidConfig && didValidate">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <strong>Warning!</strong> There are errors in your xml.
      </div>
      <!-- End of currently used html -->
      <div class="modal fade" id="confirm-modal" tabindex="-1" role="dialog" aria-labelledby="confirm-modal-label">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true"></span></button>
              <h3>Confirm Save Configuration</h3>
              <h4 class="modal-title"><b>Name: </b> {{this.configName}}</h4>
            </div>
            <div class="modal-body">
              <h5 v-if="existingConfig">
                You are about to make changes to an existing configuration.
                Press OK to proceed. To make a new configuration instead, cancel and then change the configuration name.
              </h5>
              <h5 v-else>
                You are about to save this new configuration. Press OK to proceed or cancel to make changes.
              </h5>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-primary" @click="saveConfig()">OK</button>
              <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>
            </div>
          </div>
        </div>
      </div>

      <div class="modal fade" id="validate-modal" tabindex="-1" role="dialog" aria-labelledby="validate-modal-label">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true"></span></button>
              <h3>Validate Configuration</h3>
              <h4 class="modal-title"><b>Name:</b> {{this.configName}}</h4>
            </div>
            <div class="modal-body">
              <h5>Please validate the configuration before saving.</h5>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-default" data-dismiss="modal">Ok</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>


<script>
  import axios from 'axios';
  import { codemirror } from 'vue-codemirror';
  import 'codemirror/mode/xml/xml';
  import 'codemirror/lib/codemirror.css';

  export default {
    components: {
      codemirror,
    },
    name: 'ConfigEditorInput.vue',
    data() {
      return {
        cmOptions: {
          tabSize: 4,
          mode: {
            name: 'xml',
            matchClosing: true,
          },
          lineNumbers: true,
        },
        configName: '',
        defaultCheck: false,
        didValidate: false,
        existingConfig: false,
        inputTextToSave: '',
      };
    },
    computed: {
      isValidConfig() { // check encoding?
        const oParser = new DOMParser();
        const oDOM = oParser.parseFromString(this.inputTextToSave, 'text/xml');
        return oDOM.documentElement.nodeName !== 'parsererror';
      },
    },
    mounted() {
      if (this.$route.params.id !== undefined) {
        this.configName = this.$route.params.id;
        document.getElementById('configNameBox').value = this.configName;
        axios.get(`http://localhost:8000/configs/${this.configName}`)
          .then((response) => {
            this.inputTextToSave = atob(response.data.content);
            this.defaultCheck = response.data.default;
            this.existingConfig = true;
            console.log(this.existingConfig);
          });
      }
    },
    beforeDestroy() {},
    destroy() {},

    methods: {
      makeDefault() {
        this.defaultCheck = $('#makeDefault').is(':checked');
      },
      submitConfig() {
        if (this.isValidConfig) {
          this.saveConfig();
        }
      },
      loadConfig() {
        const fr = new FileReader();
        const file = document.getElementById('file').files[0];
          fr.onload = (inputFile => (e) => {
            this.inputTextToSave = e.target.result;
            [this.configName] = inputFile.name.split('.xml');
          })(file);
          fr.readAsText(file);
      },
      didNotValidate() {
        this.didValidate = 0;
      },
      saveConfig() {
        const data = {
          name: this.configName,
          content: btoa(this.inputTextToSave),
          default: this.defaultCheck,
        };
        console.log(this.existingConfig);
        if (!this.existingConfig) {
          axios.post('http://localhost:8000/configs/', data);
        } else {
          axios.put('http://localhost:8000/configs/', data);
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
  .btn-file {
    position: relative;
    overflow: hidden;
  }
  .btn-file input[type=file] {
    position: absolute;
    top: 0;
    right: 0;
    min-width: 100%;
    min-height: 100%;
    font-size: 100px;
    text-align: right;
    filter: alpha(opacity=0);
    opacity: 0;
    outline: none;
    background: white;
    cursor: inherit;
    display: block;
  }
</style>
