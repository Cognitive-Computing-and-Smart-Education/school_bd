import index from "@/views/layout/index"
import login from '@/views/login/index'

export default [
    {
        path: '/login',
        name: 'login',
        component: login
    },
    {
        path: '/',
        component: index,
        children:[
            ]
    },

]
