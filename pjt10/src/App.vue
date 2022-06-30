<template>
  <div id="app">
    <nav class="d-flex justify-content-between">
      <div class="">
        <img src = "@/assets/images/youngtyrano.png" style="width:80px; height:100px;">
      </div>


      <div class="my-auto">
        <router-link :to="{ name: 'home' }" class="text-decoration-none">Home</router-link>
        <router-link :to="{ name: 'random' }" class="mx-5 text-decoration-none">Random</router-link>
        <router-link :to="{ name: 'watch' }" class="text-decoration-none">MyMovieList</router-link>
      </div>
    </nav>
    <router-view/>
  </div>
</template>






<script>
import axios from 'axios'

export default {
  name: 'App',
  data: function () {
    return {
      movieInfo: [],
    }
  },

  created () {
    axios({
      method: 'get',
      url: 'https://api.themoviedb.org/3/movie/popular',
      params: {
        api_key: '1f4e35b537297dc83bf23024d8160334',
        language: 'ko-KR'
      }
    })
      .then(response => {
        this.movieInfo = response.data.results
        this.$store.dispatch('allMovie', this.movieInfo)
      })
  },
}



</script>






<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
  background-color: #BDE6F1;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
