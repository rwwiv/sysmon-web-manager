<template>
  <section class="content">
    <div class="row">
      <div class="col-md-12">
        <div class="box">
          <div class="box-header with-border">
            <h4 class="box-title">
              Global Variables
            </h4>
          </div>
          <!-- /.box-header -->
          <div class="box-body">
            <table class="table no-margin">
              <thead>
              <tr>
                <th>Variable Name</th>
                <th>Variable Value</th>
              </tr>
              </thead>
              <tbody>
              <SysmonVersioningRepoLink></SysmonVersioningRepoLink>
              <SysmonDownloadLink></SysmonDownloadLink>
              <InitialConfigRepoLink></InitialConfigRepoLink>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  import SysmonVersioningRepoLink from '../components/globalVariableLinks/SysmonVersioningRepoLink.vue';
  import SysmonDownloadLink from '../components/globalVariableLinks/SysmonDownloadLink.vue';
  import InitialConfigRepoLink from '../components/globalVariableLinks/InitialConfigRepoLink.vue';

  $(document).ready(() => {
    // $('input').iCheck({
    //   checkboxClass: 'icheckbox_minimal-blue',
    //   radioClass: 'iradio_minimal-blue',
    // });
  });
  export default {
    components: { SysmonVersioningRepoLink, SysmonDownloadLink, InitialConfigRepoLink },
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
