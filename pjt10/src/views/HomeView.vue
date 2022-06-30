<template>
  <div class="d-flex">
    <div class="home row row-cols-1 row-cols-sm-2 row-cols-md-4 justify-content-center">
      <movie-card 
        v-for="card in movielist[0]" :key="card.id"
        :card="card"
      ></movie-card>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import { mapState } from 'vuex'

export default {
  name: 'HomeView',
  computed : {
    ...mapState(['movielist']),
  },
  components: {
    MovieCard
  },
}
</script>
