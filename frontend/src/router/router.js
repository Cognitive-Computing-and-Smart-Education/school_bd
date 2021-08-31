import index from "@/views/layout/index"
import login from '@/views/login/index'
import home from '@/views/detailsHome/index'
import homeManage from './homeManage.js'

export default [
    {
        path: '/login',
        name: 'login',
        component: login
    },
    {
        path: '/',
        name: 'home',
        component: index,
    },
    {
        path: '/detailsHome',
        name: 'detailsHome',
        component: home,
        children: homeManage
    }

]
