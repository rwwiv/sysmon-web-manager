<template>
  <section class="content">
    <div class="row">
      <div class="col-md-12">
        <VersionList></VersionList>
      </div>
    </div>
  </section>
</template>

<script>
import VersionList from '../components/VersionList.vue';


export default {
  data() {
    return {
    };
  },
  components: { VersionList },
  methods: {
    mounted() {
      console.log('at Versions');
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
