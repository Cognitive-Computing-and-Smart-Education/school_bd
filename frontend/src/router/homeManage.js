import gradeAnalysis from './gradeAnalysis'

const memberManage = [
    {
        path: '/detailsHome/schoolProfile',
        name: 'schoolProfile',
        component: () => import('@/views/school-profile/index'),
        meta: {title: '学校概况',type:'menu',icon:'el-icon-location'}
    },
    {
        path: '/detailsHome/studentsSource',
        name: 'studentsSource',
        component: () => import('@/views/students-source/index'),
        meta: {title: '生源分析',type:'menu',icon:'el-icon-location'}
    },
    {
        path: '/detailsHome/gradeAnalysis',
        name: 'gradeAnalysis',
        children: gradeAnalysis,
        meta: {title: '年级分析',type:'menu',icon:'el-icon-location'}
    },
]

export default memberManage;
