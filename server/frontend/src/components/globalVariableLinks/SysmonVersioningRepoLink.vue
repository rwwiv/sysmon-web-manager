<template>
<tr>
  <th>Sysmon Versioning Repo Link</th>
  <input v-model="retrievedLink" placeholder="No link found please enter a link">
  <button class="btn btn-secondary pull-right" @click="setVersioningLink()">Save</button>
</tr>
</template>

<script>
  import axios from 'axios';

export default {
  name: 'SysmonVersioningRepoLink',
  data() {
    return {
      retrievedLink: '',
    };
  },
  methods: {
    getVersioningLink() {
      axios.get('http://localhost:8000/support/links/sysmon/repo')
        .then((response) => {
          this.retrievedLink = response.data.link;
          console.log(response.data);
        })
        .catch((e) => {
          this.errors.push(e);
        });
    },
    setVersioningLink() {
      axios.post('http://localhost:8000/support/links/sysmon/repo', { link: this.retrievedLink })
        .then((response) => {
          console.log(response.data);
        })
        .catch((e) => {
          this.errors.push(e);
        });
    },
  },
  mounted() {
    this.getVersioningLink();
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
