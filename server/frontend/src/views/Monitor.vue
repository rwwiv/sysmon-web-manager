<template>
  <section class="content">
    <div class="row">
      <div class="col-md-12">
        <AgentList></AgentList>
      </div>
    </div>
  </section>
</template>

<script>
  import AgentList from '../components/AgentList.vue';


  export default {
    data() {
      return {
      };
    },
    components: { AgentList },
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
