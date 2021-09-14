const teacherAnalysis = [
    {
        path: 'teacherProfile',
        name: 'teacherProfile',
        component: () => import('@/views/teacher-analysis/teacher-profile/index'),
        meta: {title: '师资概况',type:'menu', showBreadcrumb: true},
    },
    {
        path: 'teacherInformation',
        name: 'teacherInformation',
        component: () => import('@/views/teacher-analysis/teacher-information/index'),
        meta: {title: '教师基本信息',type:'menu', showBreadcrumb: true}
    },
    {
        path: 'careerDevelopment',
        name: 'careerDevelopment',
        component: () => import('@/views/teacher-analysis/career-development/index'),
        meta: {title: '教师能力与发展',type:'menu', showBreadcrumb: true}
    },
    // {
    //     path: 'teachingAbility',
    //     name: 'teachingAbility',
    //     component: () => import('@/views/teacher-analysis/teaching-ability/index'),
    //     meta: {title: '教师教学能力',type:'menu'}
    // }
]

export default teacherAnalysis;
