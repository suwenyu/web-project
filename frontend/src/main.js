import Vue from 'vue'
import App from './App.vue'

import router from './router'
import store from './store'

import axios from 'axios'
import VueAxios from 'vue-axios'


Vue.config.productionTip = false

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

Vue.use(VueAxios, axios)
// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)



// Vue.prototype.$axios = axios;
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-fromurlencodeed'

// app.js
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
