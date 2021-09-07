const teacherAnalysis = [
    {
        path: 'teacherProfile',
        name: 'teacherProfile',
        component: () => import('@/views/teacher-analysis/teacher-profile/index'),
        meta: {title: '师资概况',type:'menu'},
    },
    {
        path: 'teacherInformation',
        name: 'teacherInformation',
        component: () => import('@/views/teacher-analysis/teacher-information/index'),
        meta: {title: '教师基本信息',type:'menu'}
    },
    {
        path: 'careerDevelopment',
        name: 'careerDevelopment',
        component: () => import('@/views/teacher-analysis/career-development/index'),
        meta: {title: '教师职业发展',type:'menu'}
    },
    {
        path: 'teachingAbility',
        name: 'teachingAbility',
        component: () => import('@/views/teacher-analysis/teaching-ability/index'),
        meta: {title: '教师教学能力',type:'menu'}
    }
]

export default teacherAnalysis;
