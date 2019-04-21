<template>
<tr>
  <th>Sysmon Versioning Repo Link</th>
  <input v-model="link" placeholder="No link found please enter a link" data-toggle="tooltip" :title="link">
  <button class="btn btn-secondary pull-right" @click="setVersioningLink()">Save</button>
</tr>
</template>

<script>
  import supportAPI from '../../api/support';

  $(document).ready(() => {
    $('[data-toggle="tooltip"]').tooltip();
  });

  export default {
  name: 'SysmonVersioningRepoLink',
  data() {
    return {
      link: '',
    };
  },
  methods: {
    getVersioningLink() {
      supportAPI.getSysmonVersionRepoLink()
        .then((response) => {
          this.link = response.data.link;
        })
        .catch((e) => {
          this.errors.push(e);
        });
    },
    setVersioningLink() {
      supportAPI.setSysmonVersionRepoLink(this.link)
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

<style scoped>
  tr input{
    width:40%;
  }
</style>
