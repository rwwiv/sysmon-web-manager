<template>
  <div class="wrapper">

    <!-- Main Header -->
    <header class="main-header">
      <!-- Logo -->
      <a href="index2.html" class="logo">
        <!-- mini logo for sidebar mini 50x50 pixels -->
        <span class="logo-mini"><b>S</b>Mgr</span>
        <!-- logo for regular state and mobile devices -->
        <span class="logo-lg"><b>Sys</b>Monager</span>
      </a>

      <!-- Header Navbar -->
      <nav class="navbar navbar-static-top" role="navigation">
        <!-- Sidebar toggle button-->
        <a href="#" class="sidebar-toggle" data-toggle="push-menu" role="button">
          <span class="sr-only">Toggle navigation</span>
        </a>
      </nav>
    </header>

    <!-- Left side column. contains the logo and sidebar -->
    <aside class="main-sidebar">
      <!-- sidebar: style can be found in sidebar.less -->
      <section class="sidebar">
        <!-- Sidebar Menu -->
        <ul class="sidebar-menu" data-widget="tree">
          <li class="header">Main Menu</li>
          <!-- Optionally, you can add icons to the links -->
          <router-link tag="li" to="/" exact-active-class="active" exact>
            <a><i class="fa fa-desktop"></i> <span>Monitor</span></a>
          </router-link>

          <li class="treeview">
            <a href="#"><i class="fa fa-cog"></i> <span>Configuration</span>
              <span class="pull-right-container"><i class="fa fa-angle-left pull-right"></i></span>
            </a>
            <ul class="treeview-menu">
              <router-link tag="li" active-class="active" to="enterpriseInstall"><a>Enterprise Install</a></router-link>
              <router-link tag="li" active-class="active" to="management"><a>Management</a></router-link>
            </ul>
          </li>
        </ul>
        <!-- /.sidebar-menu -->
      </section>
      <!-- /.sidebar -->
    </aside>

    <!-- Content Wrapper. Contains page content -->
    <div class="content-wrapper">
      <transition mode="out-in" name="router-anim" enter-active-class="animated slideInLeft" leave-active-class="animated fadeOut">
        <router-view/>
      </transition>
    </div>
    <!-- /.content-wrapper -->


  </div>
</template>

<script>
export default {
  name: 'App',
  methods: {

  },
};
</script>

<style lang="scss">
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
  #nav {
    padding: 30px;
    a {
      font-weight: bold;
      color: #2c3e50;
      &.router-link-exact-active {
        color: #42b983;
      }
    }
  }

.slideInLeft {
  -webkit-animation: slideInLeft 0.25s;
  -moz-animation: slideInLeft 0.25s;
  -o-animation: slideInLeft 0.25s;
  animation: slideInLeft 0.25s;
}

.fadeOut {
  -webkit-animation: fadeOut 0.25s;
  -moz-animation: fadeOut 0.25s;
  -o-animation: fadeOut 0.25s;
  animation: fadeOut 0.25s;
}
</style>
