<template>
  <section class="content">
    <div class="row">
      <div class="col-md-12">
        <ConfigEd></ConfigEd>
      </div>
    </div>
  </section>
</template>

<script>
  import axios from 'axios';

  import ConfigEd from '../components/ConfigEditorInput.vue';

  $(document).ready(() => {
    $('input').iCheck({
      checkboxClass: 'icheckbox_minimal-blue',
      radioClass: 'iradio_minimal-blue',
    });
  });
  export default {
      components: { ConfigEd },
    };
</script>

<style scoped>

</style>
