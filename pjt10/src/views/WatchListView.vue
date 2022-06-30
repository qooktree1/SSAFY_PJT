<template>
  <div class="watch">
    <watch-list-form></watch-list-form>
    <watch-list-item></watch-list-item>
  </div>
</template>

<script>
import WatchListForm from '../components/WatchListForm.vue'
import WatchListItem from '../components/WatchListItem.vue'
export default {
  name: 'WatchListView',
  components: {
    WatchListForm, WatchListItem
  },
  

}
</script>

<style>

</style>