import gradeAnalysis from './gradeAnalysis'
import disciplineAnalysis from './disciplineAnalysis'
import teacherAnalysis from './teacherAnalysis'
import studentAnalysis from './studentAnalysis'


const memberManage = [
    {
        path: 'schoolProfile',
        name: 'schoolProfile',
        component: () => import('@/views/school-profile/index'),
        meta: {title: '学校概况',type:'menu',icon:'el-icon-location', showBreadcrumb: true}
    },
    {
        path: 'studentsSource',
        name: 'studentsSource',
        component: () => import('@/views/students-source/index'),
        meta: {title: '生源分析',type:'menu',icon:'el-icon-location', showBreadcrumb: true}
    },
    {
        path: 'gradeAnalysis',
        name: 'gradeAnalysis',
        children: gradeAnalysis,
        component: () => import('@/views/grade-analysis/index'),
        meta: {title: '年级分析',type:'menu',icon:'el-icon-location', showBreadcrumb: false}
    },
    {
        path: 'disciplineAnalysis',
        name: 'disciplineAnalysis',
        children: disciplineAnalysis,
        component: () => import('@/views/discipline-analysis/index'),
        meta: {title: '学科分析',type:'menu',icon:'el-icon-location', showBreadcrumb: false}
    },{
        path: 'teacherAnalysis',
        name: 'teacherAnalysis',
        children: teacherAnalysis,
        component: () => import('@/views/teacher-analysis/index'),
        meta: {title: '教师分析',type:'menu',icon:'el-icon-location', showBreadcrumb: false}
    },{
        path: 'studentAnalysis',
        name: 'studentAnalysis',
        children: studentAnalysis,
        component: () => import('@/views/student-analysis/index'),
        meta: {title: '学生分析',type:'menu',icon:'el-icon-location', showBreadcrumb: false}
    }
]

export default memberManage;
