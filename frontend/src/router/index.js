import Vue from 'vue';
import Router from 'vue-router';

import home from '@/views/home';
import signup from '@/views/signup'

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
    {
        path: '/',
        name: 'home',
        component: home
    },
    {
        path: '/signup',
        name: 'signup',
        component: signup
    }
    ],
});
