<template>
  <router-view/>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'App',
    beforeCreate() {
      axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
      const token = document.head.querySelector('meta[name="csrf-token"]');
      if (token) {
        axios.defaults.headers.common['X-CSRF-TOKEN'] = token.content;
      }
    },
  };
</script>

<style lang="scss">
</style>
