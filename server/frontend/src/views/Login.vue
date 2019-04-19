<template>
	<section class="content">
    <div id="loginContainer">
      <div class="alert alert-warning alert-dismissible" role="alert" v-if="loginFailed">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <strong>Warning!</strong> There are errors in your xml.
      </div>
      <div class="box" id="loginBox">
        <div class="box-header with-border">
          <h5>Login</h5>
        </div>
        <div class="box-body">
          <form class="form-inline" @submit="authUser">
            <div class="form-group">
              <label for="userNameInput" class="sr-only"></label>
              <input
                type="text"
                class="form-control"
                id="userNameInput"
                placeholder="Username"
              >
            </div>
            <div class="form-group">
              <label for="passwordInput" class="sr-only"></label>
              <input
                type="password"
                class="form-control"
                id="passwordInput"
                placeholder="Password"
              >
            </div>
            <button type="submit" class="btn btn-default"></button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'Login',
    data() {
      return {
        loginFailed: false,
      };
    },
    methods: {
      authUser(event) {
        event.preventDefault();
        axios.post('http://localhost:8000/users/auth')
          .then(() => {
            this.$router.push({ name: 'monitor' });
          })
          .catch(() => {
            this.loginFailed = true;
          });
      },
    },
  };
</script>

<style scoped>

</style>
