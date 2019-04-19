<template>
  <section class="content">
    <div class="row">
      <div class="col-md-12">
        <ConfigsList></ConfigsList>
      </div>
    </div>
  </section>
</template>

<script>
import ConfigsList from '../components/ConfigsList.vue';

$(document).ready(() => {
  // $('input').iCheck({
  //   checkboxClass: 'icheckbox_minimal-blue',
  //   radioClass: 'iradio_minimal-blue',
  // });
});
export default {
  components: { ConfigsList },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
