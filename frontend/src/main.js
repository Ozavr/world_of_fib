import Vue from 'vue'
import App from './App.vue'
import VueSocketIO from 'vue-socket.io'
import VueMaterial from 'vue-material'
import Vuelidate from 'vuelidate'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'


Vue.use(Vuelidate)
Vue.use(VueMaterial)


Vue.use(new VueSocketIO({
  debug: true,
  connection: 'localhost:8000/fib',
}))


new Vue({
  el: '#app',
  render: h => h(App)
})
