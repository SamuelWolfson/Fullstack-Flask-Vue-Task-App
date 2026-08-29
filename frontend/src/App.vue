<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script setup>
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  max-width: 100vw;
  overflow-x: hidden;
  box-sizing: border-box;
}

*, *::before, *::after {
  box-sizing: inherit;
}

#app {
  min-height: 100vh;
  font-family: Arial, sans-serif;
}
</style>