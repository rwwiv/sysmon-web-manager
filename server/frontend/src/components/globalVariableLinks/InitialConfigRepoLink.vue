<template>
  <div class="row">
    <div class="col-md-3 flex-container">
      <p class="center-align">Initial Config Repo Link</p>
    </div>
    <div class="col-md-8 flex-container">
      <input class="fill-width" v-model="retrievedLink" placeholder="No link found please enter a link" data-toggle="tooltip" :title="retrievedLink">
    </div>
    <div class="col-md-1">
      <button class="btn btn-secondary pull-right" @click="setConfigLink()">Save</button>
    </div>
  </div>
</template>

<script>
  import supportAPI from '../../api/support';

  $(document).ready(() => {
    $('[data-toggle="tooltip"]').tooltip();
  });

  export default {
    name: 'InitialConfigRepoLink',
    data() {
      return {
        link: '',
      };
    },
    methods: {
      getConfigLink() {
        supportAPI.getDefaultConfigDownloadLink()
          .then((response) => {
            this.retrievedLink = response.data.link;
          });
      },
      setConfigLink() {
        supportAPI.setDefaultConfigDownloadLink(this.link);
      },
    },
    mounted() {
      this.getConfigLink();
    },
  };
</script>

<style scoped>
  td a {
    cursor:pointer;
  }
  .center-text {
    text-align:center;
  }
  .icon-column{
    width:10%;
  }
</style>

<style scoped>
  td a {
    cursor:pointer;
  }
  .center-text {
    text-align:center;
  }
  .icon-column{
    width:10%;
  }
  .flex-container {
    display: flex;
  }
  .fill-width {
    flex: 1
  }
  .center-align {
    align-content: center;
  }
  tr input{
    width:40%;
  }
</style>
