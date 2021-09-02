import gradeAnalysis from './gradeAnalysis'
import disciplineAnalysis from './disciplineAnalysis'


const memberManage = [
    {
        path: 'schoolProfile',
        name: 'schoolProfile',
        component: () => import('@/views/school-profile/index'),
        meta: {title: '学校概况',type:'menu',icon:'el-icon-location'}
    },
    {
        path: 'studentsSource',
        name: 'studentsSource',
        component: () => import('@/views/students-source/index'),
        meta: {title: '生源分析',type:'menu',icon:'el-icon-location'}
    },
    {
        path: 'gradeAnalysis',
        name: 'gradeAnalysis',
        children: gradeAnalysis,
        component: () => import('@/views/grade-analysis/index'),
        meta: {title: '年级分析',type:'menu',icon:'el-icon-location'}
    },
    {
        path: 'disciplineAnalysis',
        name: 'disciplineAnalysis',
        children: disciplineAnalysis,
        component: () => import('@/views/discipline-analysis/index'),
        meta: {title: '学科分析',type:'menu',icon:'el-icon-location'}
    },
]

export default memberManage;
