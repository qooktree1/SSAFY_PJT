<template>
    <div class="col">
      <div class="card">
        <img :src="imageUrl" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">{{ card.title }}</h5>
          <p class="card-text">{{ card.overview }}</p>
        </div>
      </div>
    </div>
</template>

  
<script>
export default {
  name: 'MovieCard',
  props: {
    card: Object,
  },
  data: function () {
    return {
      imageUrl: "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/" + this.card.poster_path
    }
  }
}
</script>

<style>
  .card-text {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 4; 
    -webkit-box-orient: vertical;
  }
</style>