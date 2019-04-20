<template>
  <tr>
    <th>Sysmon Versioning Repo Link</th>
    <input v-model="retrievedLink" placeholder="No link found please enter a link">
    <button class="btn btn-secondary pull-right" @click="setConfigLink()">Save</button>
  </tr>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'InitialConfigRepoLink',
    data() {
      return {
        retrievedLink: '',
      };
    },
    methods: {
      getConfigLink() {
        axios.get('http://localhost:8000/support/links/configs/download')
          .then((response) => {
            this.retrievedLink = response.data.link;
            console.log(response.data);
          })
          .catch((e) => {
            this.errors.push(e);
          });
      },
      setConfigLink() {
        axios.post('http://localhost:8000/support/links/configs/download', { link: this.retrievedLink })
          .then((response) => {
            console.log(response.data);
          })
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
