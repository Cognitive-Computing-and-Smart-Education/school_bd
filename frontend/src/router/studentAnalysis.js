const studentAnalysis = [
    {
        path: 'studentInformation',
        name: 'studentInformation',
        component: () => import('@/views/student-analysis/student-information/index'),
        meta: {title: '学生基本信息',type:'menu', showBreadcrumb: true},
    },{
        path: 'studentInformation/studentInformationDetail',
        name: 'studentInformationDetail',
        component: () => import('@/views/student-analysis/student-information/detail'),
        meta: {title: '学生基本信息详情',type:'detail', showBreadcrumb: true},
        children: [
            {
                path: 'information',
                name: 'information',
                component: () => import('@/views/student-analysis/student-information/content/information'),
                meta: {title: '基本信息',type:'menu', showBreadcrumb: true},
            },{
                path: 'lawLife',
                name: 'lawLife',
                component: () => import('@/views/student-analysis/student-information/content/lawLife'),
                meta: {title: '生活规律',type:'menu', showBreadcrumb: true},
            },{
                path: 'consumption',
                name: 'consumption',
                component: () => import('@/views/student-analysis/student-information/content/consumption'),
                meta: {title: '消费水平',type:'menu', showBreadcrumb: true},
            },{
                path: 'socialContact',
                name: 'socialContact',
                component: () => import('@/views/student-analysis/student-information/content/social-contact'),
                meta: {title: '社交关系',type:'menu', showBreadcrumb: true},
            },{
                path: 'library',
                name: 'library',
                component: () => import('@/views/student-analysis/student-information/content/library'),
                meta: {title: '图书馆',type:'menu', showBreadcrumb: true},
            },{
                path: 'study',
                name: 'study',
                component: () => import('@/views/student-analysis/student-information/content/study'),
                meta: {title: '学习成绩',type:'menu', showBreadcrumb: true},
            },{
                path: 'whereabouts',
                name: 'whereabouts',
                component: () => import('@/views/student-analysis/student-information/content/whereabouts'),
                meta: {title: '毕业去向预测',type:'menu', showBreadcrumb: true},
            }
        ]
    },{
        path: 'studentStudies',
        name: 'studentStudies',
        component: () => import('@/views/student-analysis/student-studies/index'),
        meta: {title: '学生学业发展',type:'menu', showBreadcrumb: true},
    },{
        path: 'studentQuality',
        name: 'studentQuality',
        component: () => import('@/views/student-analysis/student-quality/index'),
        meta: {title: '身心与发展性素质',type:'menu', showBreadcrumb: true},
    },{
        path: 'lifeState',
        name: 'lifeState',
        component: () => import('@/views/student-analysis/life-state/index'),
        meta: {title: '生活状态',type:'menu', showBreadcrumb: true},
    },{
        path: 'behaviorHabit',
        name: 'behaviorHabit',
        component: () => import('@/views/student-analysis/behavior-habit/index'),
        meta: {title: '行为习惯',type:'menu', showBreadcrumb: true},
    }
]

export default studentAnalysis;
