const gradeAnalysis = [
    {
        path: 'disciplineOverview',
        name: 'disciplineOverview',
        component: () => import('@/views/discipline-analysis/discipline-overview/index'),
        meta: {title: '学科概况',type:'menu'},
    },
    {
        path: 'disciplineOverview/detail',
        name: 'disciplineOverviewDetail',
        component: () => import('@/views/discipline-analysis/discipline-overview/detail'),
        meta: {title: '课程详情',type:'detail'}
    },
    {
        path: 'curriculumResources',
        name: 'curriculumResources',
        component: () => import('@/views/discipline-analysis/curriculum-resources/index'),
        meta: {title: '课程资源',type:'menu'}
    },
    {
        path: 'extracurricularActivities',
        name: 'extracurricularActivities',
        component: () => import('@/views/discipline-analysis/extracurricular-activities/index'),
        meta: {title: '课外活动',type:'menu'}
    },
    {
        path: 'classroomTeaching',
        name: 'classroomTeaching',
        component: () => import('@/views/discipline-analysis/classroom-teaching/index'),
        meta: {title: '课堂教学',type:'menu'}
    },
    {
        path: 'teachingEvaluation',
        name: 'teachingEvaluation',
        component: () => import('@/views/discipline-analysis/teaching-evaluation/index'),
        meta: {title: '课程教学评价',type:'menu'}
    },
]

export default gradeAnalysis;
