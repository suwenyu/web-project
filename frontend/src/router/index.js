import Vue from 'vue';
import Router from 'vue-router';

import home from '@/views/home';
import signup from '@/views/signup'
import login from '@/views/login'
import store from '../store'


const ifNotAuthenticated = (to, from, next) => {
  if (!store.state.isAuthenticated) {
    next()
    return
  }
  next('/')
}

const ifAuthenticated = (to, from, next) => {
  console.log(store);
  if (store.state.isAuthenticated) {
    next()
    return
  }
  next('/login')
}

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
    {
        path: '/',
        name: 'home',
        component: home,
        beforeEnter: ifAuthenticated,
    },
    {
        path: '/signup',
        name: 'signup',
        component: signup
    },
    {
        path: '/login',
        name: 'login',
        component: login,
        beforeEnter: ifNotAuthenticated,
    }
    ],
});
