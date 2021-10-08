<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> 
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  display: flex;  
}

#nav a {
  font-weight: bold;
  color:gray;
  padding: 20px;
}

#nav a.router-link-exact-active {
  color: white;
}

body {
  background-image: url("https://i.imgur.com/stbdVjS.jpg");
  width: 100vw;
  -webkit-background-size:cover ;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  background-repeat: no-repeat;
}
</style>
