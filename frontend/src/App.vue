<template>
  <div>
    <NavBar />
    <Main />
    <hr>
    <Footer />
  </div>
</template>


<script>
import NavBar from './components/NavBar.vue'
import Main from './components/Main.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    Main,
    Footer,
  }
}
</script>

<style src="./css/style.css">

</style>

