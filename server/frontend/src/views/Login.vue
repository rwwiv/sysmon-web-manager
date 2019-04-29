<template>
  <div>
    <div class="login-logo">
      <b>Sys</b>Monager
    </div>
    <div class="login-box-body">
      <p class="login-box-msg">Sign in</p>
      <form @submit="authUser">
        <div class="form-group has-feedback">
          <input type="text" class="form-control" placeholder="Username">
          <span class="glyphicon glyphicon-user form-control-feedback"></span>
        </div>
        <div class="form-group has-feedback">
          <input type="password" class="form-control" placeholder="Password">
          <span class="glyphicon glyphicon-lock form-control-feedback"></span>
        </div>
        <div class="row">
          <div class="col-xs-8">
            <input type="checkbox" class="checkbox" id="rememberMeCheckbox">
            <label for="rememberMeCheckbox">Remember Me</label>
          </div>
          <div class="col-xs-4">
            <button type="submit" class="btn btn-primary btn-block btn-flat">
              Sign In
            </button>
          </div>
        </div>
      </form>
      <div class="text-center">
        <p>- OR -</p>
        <router-link to="/register">
          <a>Register</a>
        </router-link>
      </div>
    </div>
    <div class="callout callout-danger login-failure" v-if="loginSubmitHasFailed">
      <h4>Credentials invalid.</h4>
      <p>Try logging in again</p>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Login',
    data() {
      return {
        loginStatus: this.$store.state.loginStatus,
      };
    },
    computed: {

    },
    beforeCreate() {
      $('body').addClass('login-page');
    },
    destroyed() {
      $('body').removeClass('login-page');
    },
    methods: {
      authenticateUser(username, password) {
        this.$store.dispatch('authUser', username, password)
          .then();
      },
    },
  };
</script>

<style scoped>

</style>
