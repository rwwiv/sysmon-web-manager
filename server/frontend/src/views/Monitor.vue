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
  import axios from 'axios';

  $(document).ready(() => {
    $('input').iCheck({
      checkboxClass: 'icheckbox_minimal-blue',
      radioClass: 'iradio_minimal-blue',
    });
  });
  export default {
    data(){
      return {
        hosts: [],
        errors: []
      }
    },
    created(){
      axios.get('http://127.0.0.1:8000/agents', { crossdomain: true })
      .then(response => {
        this.hosts = response.data;
        console.log(response.data);
      })
      .catch(e => {
        this.errors.push(e)
      })
    },
    components: { AgentList },
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
