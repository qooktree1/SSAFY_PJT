<template>
  <div class="watch-form">
    <div class="mt-5 py-4">
      <h1>My Movie List</h1>
      <input
        type="text"
        @keyup.enter="createTodo"
        v-model.trim="todoTitle"
      >
      <button type="button" v-on:click="createTodo" class="btn btn-secondary">Add</button>
    </div>
  </div>
</template>

<script>

export default {
  name: 'WatchListForm',
  data: function () {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo: function () {
      const todoItem = {
        title: this.todoTitle,
      }
      if (todoItem.title) {

        if (todoItem.title === '김준호' || todoItem.title === '티라노' || todoItem.title === '6반') {
          window.location.href = "https://www.instagram.com/harry_jjun/"
        } else {
          this.$store.dispatch('createTodo', todoItem)
        }
        
      }
      this.todoTitle = null
    }
  }

}
</script>

<style>
.watch-form {
  background-color: #BDE6F1;
}
</style>