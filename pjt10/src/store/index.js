import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    todos: [],
    movielist: [],
  },
  getters: {
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      state.todos.push(todoItem)
    },
    ALL_MOVIE: function (state, movieInfo) {
      state.movielist.push(movieInfo)
    },
  },
  actions: {
    createTodo: function ({ commit }, todoItem) {
      commit('CREATE_TODO', todoItem)
    },
    allMovie: function ({ commit }, movieInfo) {
      
      commit('ALL_MOVIE', movieInfo)
    },
  },
})
