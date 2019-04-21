<template>
  <tr>
    <th>Sysmon Download Link</th>
    <input v-model="retrievedLink" placeholder="No link found please enter a link" data-toggle="tooltip" :title="retrievedLink">
    <button class="btn btn-secondary pull-right" @click="setDownloadLink()">Save</button>
  </tr>
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
          })
          .catch((e) => {
            this.errors.push(e);
          });
      },
      setDownloadLink() {
        supportAPI.setSysmonDownloadLink(this.link)
          .catch((e) => {
            this.errors.push(e);
          });
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
</style>

<style scoped>
  tr input{
    width:40%;
  }
</style>
