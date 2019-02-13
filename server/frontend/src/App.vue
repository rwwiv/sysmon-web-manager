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
          <li class="active"><router-link to="/"><i class="fa fa-desktop"></i> <span>Monitor</span></router-link></li>
          <li class="treeview">
            <a href="#"><i class="fa fa-cog"></i> <span>Configuration</span>
              <span class="pull-right-container"><i class="fa fa-angle-left pull-right"></i></span>
            </a>
            <ul class="treeview-menu">
              <li><router-link to="enterpriseInstall">Enterprise Install</a></router-link>
              <li><router-link to="management">Management</router-link></li>
            </ul>
          </li>
        </ul>
        <!-- /.sidebar-menu -->
      </section>
      <!-- /.sidebar -->
    </aside>

    <!-- Content Wrapper. Contains page content -->

    <div class="content-wrapper">


      <router-view/>
    </div>
    <!-- /.content-wrapper -->

    
  </div>
</template>

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
</style>
