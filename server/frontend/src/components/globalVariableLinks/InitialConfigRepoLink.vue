<template>
  <tr>
    <th>Sysmon Versioning Repo Link</th>
    <input v-model="retrievedLink" placeholder="No link found please enter a link" data-toggle="tooltip" :title="retrievedLink">
    <button class="btn btn-secondary pull-right" @click="setConfigLink()">Save</button>
  </tr>
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
          })
          .catch((e) => {
            this.errors.push(e);
          });
      },
      setConfigLink() {
        supportAPI.setDefaultConfigDownloadLink(this.link)
          .catch((e) => {
            this.errors.push(e);
          });
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
</style>

<style scoped>
  tr input{
    width:40%;
  }
</style>
