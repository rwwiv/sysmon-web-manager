<template>
  <div class="row">
    <div class="col-md-3 flex-container">
      <p class="center-align">Sysmon Versioning Repo Link</p>
    </div>
    <div class="col-md-8 flex-container">
      <input class="fill-width" v-model="link" placeholder="No link found please enter a link" data-toggle="tooltip" :title="link">
    </div>
    <div class="col-md-1">
      <button class="btn btn-secondary pull-right" @click="setVersioningLink()">Save</button>
    </div>
  </div>
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
        });
    },
    setVersioningLink() {
      supportAPI.setSysmonVersionRepoLink(this.link);
    },
  },
  mounted() {
    this.getVersioningLink();
  },
};
</script>

<style scoped>
  .row {
    display: flex;
  }
  .fill-width {
    flex: 1
  }
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
