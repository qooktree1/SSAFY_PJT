<template>
  <div>
    <table class="table table-striped table-hover">
      <tbody>
        <tr v-for="todo in todos" :key="todo.title">
          <td>{{ todo.title }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'WatchListItem',
  computed: {
    ...mapState(['todos']),
  },

}
</script>

<style>

</style>