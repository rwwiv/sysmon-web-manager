<template>
  <tr>
    <th>Sysmon Download Link</th>
    <input v-model="retrievedLink" placeholder="No link found please enter a link">
    <button class="btn btn-secondary pull-right" @click="setDownloadLink()">Save</button>
  </tr>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'SysmonDownloadLink',
    data() {
      return {
        retrievedLink: '',
      };
    },
    methods: {
      getDownloadLink() {
        axios.get('http://localhost:8000/support/links/sysmon/download')
          .then((response) => {
            this.retrievedLink = response.data.link;
            console.log(response.data);
          })
          .catch((e) => {
            this.errors.push(e);
          });
      },
      setDownloadLink() {
        axios.post('http://localhost:8000/support/links/sysmon/download', { link: this.retrievedLink })
          .then((response) => {
            console.log(response.data);
          })
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
