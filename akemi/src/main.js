import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'

// Axios es un component necesari per establir conexions amb altres servidors

// App.vue declara la nostra aplicació

Vue.config.productionTip = false
Vue.prototype.$http = axios

new Vue({
  render: h => h(App),
}).$mount('#app')
