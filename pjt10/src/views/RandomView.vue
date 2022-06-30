<template>
  <div class="random d-flex justify-content-center mt-5">


<!-- 여기가 문제!!!  -->
    <div class="card" style="width: 18rem;"> 

      <button class="btn btn-success" @click="randomPick">Pick</button>

      <img :src="imageUrl" class="card-img-top" alt="">
      
      <div class="card-body">
        <h5 class="card-title" alt="#"></h5>
        <h1 v-if="imageUrl === ''">Pick a MOVIE</h1>
        <p>{{ selectedMovie.title }}</p>
      </div>
    </div>



  </div>
</template>

<script>
import _ from 'lodash'
import { mapState } from 'vuex'
export default {
  name: 'RandomView',
  data: function () {
    return {
      selectedMovie: [],
      imageUrl: '',
    }
  },
  computed: {
    ...mapState(['movielist']),
  },
  methods: {
    randomPick: function () {
      this.selectedMovie = _.sample(this.movielist[0])
      this.imageUrl = "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/" + this.selectedMovie.poster_path
    }
  },
}

</script>

<style>
</style>