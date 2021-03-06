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
                  <input type="radio" id="makeDefault" @click="makeDefault()" :checked="this.defaultCheck">
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
          <button class="btn btn-default pull-right" type="submit" data-toggle="modal" data-target="#confirm-modal" @click="configExists">Save Configuration</button>
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
              <div class="row-no-gutters">
                <div v-if="!configFound" class="col-sm-11" style="display: flex; justify-content: flex-start">
                  <h4 v-if="!configFound">Update configuration {{this.configName}}?</h4>
                  <h4 v-else>Save new configuration {{this.configName}}?</h4>
                </div>
                <div v-else class="col-sm-11" style="display: flex; justify-content: flex-start">
                  <h4>Configuration with name {{this.configName}} already exists.</h4>
                </div>
                <div class="col-sm-1" style="display: flex; justify-content: flex-end">
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
              </div>
            </div>
            <div v-if="!configFound" class="modal-footer">
              <button type="button" class="btn btn-primary" @click="submitConfig()" data-dismiss="modal">OK</button>
              <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>
            </div>
            <div v-else class="modal-footer">
              <button type="button" class="btn btn-default" data-dismiss="modal">OK</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  import { codemirror } from 'vue-codemirror';
  import 'codemirror/mode/xml/xml';
  import 'codemirror/lib/codemirror.css';
  import configAPI from '../api/configs';

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
        initConfigName: '',
        configName: '',
        defaultCheck: false,
        didValidate: false,
        inputTextToSave: '',
        configFound: false,
      };
    },
    computed: {
      isValidConfig() { // check encoding?
        const oParser = new DOMParser();
        const oDOM = oParser.parseFromString(this.inputTextToSave, 'text/xml');
        return oDOM.documentElement.nodeName !== 'parsererror';
      },
      existingConfig() {
        return this.initConfigName === this.configName;
      },
    },
    mounted() {
      if (this.$route.params.id !== undefined) {
        this.initConfigName = this.$route.params.id;
        this.configName = this.initConfigName;
        document.getElementById('configNameBox').value = this.configName;
        configAPI.getSingleConfig(this.configName)
          .then((response) => {
            this.inputTextToSave = atob(response.data.content);
            this.defaultCheck = response.data.default;
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
            if (this.configName === '') {
              [this.configName] = inputFile.name.split('.xml');
            }
          })(file);
          fr.readAsText(file);
      },
      configExists() {
        if (this.initConfigName !== '' && this.initConfigName !== this.configName) {
          console.log('Ran check');
          configAPI.getSingleConfig(this.configName)
            .then(() => {
              this.configFound = true;
            })
            .catch(() => {
              this.configFound = false;
            });
        } else this.configFound = false;
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
        if (!this.existingConfig || this.initConfigName !== this.configName) {
          configAPI.createConfig(data);
        } else {
          configAPI.updateConfig(data);
        }
        this.$router.push({ name: 'config-manager' });
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
  h4>span {
    text-decoration: underline;
    font-weight: lighter;
  }
</style>
