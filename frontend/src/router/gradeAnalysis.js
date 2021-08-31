const gradeAnalysis = [
    {
        path: '/detailsHome/gradeAnalysis/gradeOverview',
        name: 'gradeOverview',
        component: () => import('@/views/grade-analysis/grade-overview/index'),
        meta: {title: '年级概况',type:'menu'}
    },
    {
        path: '/detailsHome/gradeAnalysis/classEvaluation',
        name: 'classEvaluation',
        component: () => import('@/views/grade-analysis/class-evaluation/index'),
        meta: {title: '班级评估',type:'menu'}
    },
]

export default gradeAnalysis;
