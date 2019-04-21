<template>
  <div class="row">
    <div class="col-md-3 flex-container">
      <p class="center-align">Sysmon Download Link</p>
    </div>
    <div class="col-md-8 flex-container">
      <input class="fill-width" v-model="link" placeholder="No link found please enter a link" data-toggle="tooltip" :title="link">
    </div>
    <div class="col-md-1">
      <button class="btn btn-secondary pull-right" @click="setDownloadLink()">Save</button>
    </div>
  </div>
</template>

<script>
  import supportAPI from '../../api/support';

  $(document).ready(() => {
    $('[data-toggle="tooltip"]').tooltip();
  });

  export default {
    name: 'SysmonDownloadLink',
    data() {
      return {
        link: '',
      };
    },
    methods: {
      getDownloadLink() {
        supportAPI.getSysmonDownloadLink()
          .then((response) => {
            this.retrievedLink = response.data.link;
          });
      },
      setDownloadLink() {
        supportAPI.setSysmonDownloadLink(this.link);
      },
    },
    mounted() {
      this.getDownloadLink();
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
  tr input{
    width:40%;
  }
</style>
