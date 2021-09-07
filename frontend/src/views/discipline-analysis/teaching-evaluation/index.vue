<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>考试情况分析</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="form" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="form.grade" placeholder="请选择年级">
                            <el-option
                                    label="全校"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in gradeOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-select v-model="form.class" placeholder="请选择班级">
                            <el-option
                                    label="全部班级"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in classOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-select v-model="form.courseType" placeholder="请选择课程类型">
                            <el-option
                                    label="课程类型"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in courseTypeOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="activityRateCharts"></div>
                </div>
            </div>
        </el-card>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>课堂教学质量</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="teachingQualityForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="teachingQualityForm.grade" placeholder="请选择年级">
                            <el-option
                                    label="全校"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in teachingGradeOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-select v-model="teachingQualityForm.class" placeholder="请选择班级">
                            <el-option
                                    label="全部班级"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in teachingClassOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-select v-model="teachingQualityForm.courseType" placeholder="请选择课程类型">
                            <el-option
                                    label="课程类型"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in teachingCourseTypeOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="teachingQualitySubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="teachingQualityCharts"></div>
                </div>
            </div>
        </el-card>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>课程调代课分析</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="courseAdjustmentForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="courseAdjustmentForm.grade" placeholder="请选择年级">
                            <el-option
                                    label="全校"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in courseAdjustmentGradeOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-select v-model="courseAdjustmentForm.class" placeholder="请选择班级">
                            <el-option
                                    label="全部班级"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in courseAdjustmentClassOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div class="activity-development-box">
                        <div class="activity-development-title">调代课占比</div>
                        <div class="activity-development-progress">
                            <el-progress type="circle" :percentage="25" :format="courseAdjustmentFormat" style="margin-right: 160px" :width="200" :stroke-width="16"></el-progress>
                            <el-progress type="circle" :percentage="25" :format="format" :color="'#67C23A'" :width="200" :stroke-width="16"></el-progress>
                        </div>
                    </div>
                    <div id="courseAdjustmentChart"></div>
                </div>
            </div>
        </el-card>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>课程类别分析</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="courseCategoryForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="courseCategoryForm.grade" placeholder="请选择年级">
                            <el-option
                                    label="全校"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in courseCategoryGradeOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-select v-model="courseCategoryForm.class" placeholder="请选择班级">
                            <el-option
                                    label="全部班级"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in courseCategoryClassOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="courseCategoryChart"></div>
                    <div id="categoryChangeChart"></div>
                </div>
            </div>
        </el-card>
    </div>
</template>

<script>
    export default {
        name: "index",
        data() {
            return {
                form: {
                    grade: '',
                    class: '',
                    courseType: ''
                },
                teachingQualityForm: {
                    grade: '',
                    class: '',
                    courseType: ''
                },
                courseCategoryForm: {
                    grade: '',
                    class: '',
                },
                courseAdjustmentForm: {
                    grade: '',
                    class: '',
                },
                gradeOptions: [
                    {
                        label: '高一',
                        value: '高一'
                    },{
                        label: '高二',
                        value: '高二'
                    },{
                        label: '高三',
                        value: '高三'
                    }
                ],
                classOptions: [
                    {
                        label: '高一（1）班',
                        value: '高一（1）班'
                    },{
                        label: '高一（2）班',
                        value: '高一（2）班'
                    },{
                        label: '高一（3）班',
                        value: '高一（3）班'
                    }
                ],
                courseTypeOptions: [
                    {
                        label: '理论课',
                        value: '理论课'
                    },{
                        label: '理论实践课',
                        value: '理论实践课'
                    },{
                        label: '实践课',
                        value: '实践课'
                    }
                ],
                teachingGradeOptions: [
                    {
                        label: '高一',
                        value: '高一'
                    },{
                        label: '高二',
                        value: '高二'
                    },{
                        label: '高三',
                        value: '高三'
                    }
                ],
                teachingClassOptions: [
                    {
                        label: '高一（1）班',
                        value: '高一（1）班'
                    },{
                        label: '高一（2）班',
                        value: '高一（2）班'
                    },{
                        label: '高一（3）班',
                        value: '高一（3）班'
                    }
                ],
                teachingCourseTypeOptions: [
                    {
                        label: '理论课',
                        value: '理论课'
                    },{
                        label: '理论实践课',
                        value: '理论实践课'
                    },{
                        label: '实践课',
                        value: '实践课'
                    }
                ],
                courseCategoryGradeOptions: [
                    {
                        label: '高一',
                        value: '高一'
                    },{
                        label: '高二',
                        value: '高二'
                    },{
                        label: '高三',
                        value: '高三'
                    }
                ],
                courseCategoryClassOptions: [
                    {
                        label: '高一（1）班',
                        value: '高一（1）班'
                    },{
                        label: '高一（2）班',
                        value: '高一（2）班'
                    },{
                        label: '高一（3）班',
                        value: '高一（3）班'
                    }
                ],
                courseAdjustmentGradeOptions: [
                    {
                        label: '高一',
                        value: '高一'
                    },{
                        label: '高二',
                        value: '高二'
                    },{
                        label: '高三',
                        value: '高三'
                    }
                ],
                courseAdjustmentClassOptions: [
                    {
                        label: '高一（1）班',
                        value: '高一（1）班'
                    },{
                        label: '高一（2）班',
                        value: '高一（2）班'
                    },{
                        label: '高一（3）班',
                        value: '高一（3）班'
                    }
                ],
            }
        },
        mounted() {
            this.init();
        },
        methods: {
            init() {
                this.getActivityRateCharts();
                this.getTeachingQualityCharts();
                this.getCourseAdjustmentChart();
                this.getCourseCategoryChart();
                this.getCategoryChangeChart();
            },
            getCategoryChangeChart() {
                let myChart = this.$echarts.init(document.getElementById('categoryChangeChart'))
                myChart.setOption({
                    title: {
                        text: '调代课近6学期变化趋势'
                    },
                    legend: {
                        data: ['A类', 'B类', 'C类', 'D类'],
                        right: 30
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: true,
                        data: ['2018-2019第一学期', '2018-2019第二学期', '2019-2020第一学期', '2019-2020第二学期', '2020-2021第一学期', '2020-2021第二学期'],
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: 'A类',
                            type: 'line',
                            // stack: '总量',
                            data: [152, 242, 231, 521, 132, 111]
                        },{
                            name: 'B类',
                            type: 'line',
                            // stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        },{
                            name: 'C类',
                            type: 'line',
                            // stack: '总量',
                            data: [311, 141, 214, 152, 22, 51]
                        },{
                            name: 'D类',
                            type: 'line',
                            // stack: '总量',
                            data: [125, 62, 143, 252, 311, 42]
                        }
                    ]
                })
            },
            getCourseCategoryChart() {
                let myChart = this.$echarts.init(document.getElementById('courseCategoryChart'))
                myChart.setOption({
                    title: {
                        text: '课程类别占比'
                    },
                    // legend: {
                    //     data: ['预算分配（Allocated Budget）', '实际开销（Actual Spending）']
                    // },
                    radar: {
                        // shape: 'circle',
                        indicator: [
                            { name: 'A级', max: 300},
                            { name: 'B级', max: 300},
                            { name: 'C级', max: 300},
                            { name: 'D级', max: 300},
                        ]
                    },
                    series: [{
                        name: '课程类别占比',
                        type: 'radar',
                        data: [
                            {
                                value: [245, 111, 145, 73],
                                name: '课程类别占比',
                                areaStyle: {
                                    color: '#3f69cc'
                                },
                                lineStyle: {
                                    color: '#3f69cc'
                                }
                            }
                        ]
                    }]
                })
            },
            getCourseAdjustmentChart() {
                let myChart = this.$echarts.init(document.getElementById('courseAdjustmentChart'))
                myChart.setOption({
                    title: {
                        text: '调代课近6学期变化趋势'
                    },
                    legend: {
                        data: ['调课占比', '代课占比'],
                        right: 30
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: true,
                        data: ['2018-2019第一学期', '2018-2019第二学期', '2019-2020第一学期', '2019-2020第二学期', '2020-2021第一学期', '2020-2021第二学期'],
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '调课占比',
                            type: 'line',
                            // stack: '总量',
                            data: [152, 242, 231, 521, 132, 111]
                        },{
                            name: '代课占比',
                            type: 'line',
                            // stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        }
                    ]
                })
            },
            courseAdjustmentFormat(percentage) {
                return `调课占比${percentage}%`;
            },
            format(percentage) {
                return `代课占比${percentage}%`;
            },
            getTeachingQualityCharts() {
                let myChart = this.$echarts.init(document.getElementById('teachingQualityCharts'))
                myChart.setOption({
                    title: {
                        text: '课程教学质量反馈',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['督导评价得分', '学生评价得分', '总评平均成绩'],
                        textStyle: {
                            color: '#323232'
                        }
                    },
                    xAxis: {
                        type: 'category',
                        // boundaryGap: false,
                        data: ['2018-2019第一学期', '2018-2019第二学期', '2019-2020第一学期', '2019-2020第二学期', '2020-2021第一学期', '2020-2021第二学期'],
                        axisLabel: {
                            color: '#323232'
                        }
                    },
                    yAxis: {
                        type: 'value',
                        splitLine: {
                            lineStyle: {
                                color: '#eee'
                            }
                        },
                        axisLabel: {
                            color: '#323232'
                        }
                    },
                    series: [
                        {
                            name: '督导评价得分',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [320, 302, 301, 421, 123, 214]
                        },{
                            name: '学生评价得分',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [123, 214, 145,321, 132,321]
                        },{
                            name: '总评平均成绩',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [312, 123, 42,125, 214,312]
                        }
                    ]
                })
            },
            teachingQualitySubmit() {

            },
            onSubmit() {

            },
            getActivityRateCharts() {
                let myChart = this.$echarts.init(document.getElementById('activityRateCharts'))
                myChart.setOption({
                    title: {
                        text: '课程资源近6学期变化趋势'
                    },
                    legend: {
                        data: ['考试及格率', '考试优秀率'],
                        right: 30
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: true,
                        data: ['2018-2019第一学期', '2018-2019第二学期', '2019-2020第一学期', '2019-2020第二学期', '2020-2021第一学期', '2020-2021第二学期'],
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '考试及格率',
                            type: 'line',
                            // stack: '总量',
                            data: [152, 242, 231, 521, 132, 111]
                        },{
                            name: '考试优秀率',
                            type: 'line',
                            // stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        }
                    ]
                })
            }
        }
    }
</script>

<style scoped>
    .grade-num-box{
        width: 100%;
        height: 400px;
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
    }
    #activityRateCharts,
    #teachingQualityCharts{
        width: 100%;
        height: 100%;
    }
    .school-overview-card{
        margin-bottom: 30px;
    }
    #courseAdjustmentChart{
        width: 56%;
        height: 100%;
    }
    .activity-development-box{
        width: 42%;
        height: 100%;
    }
    .activity-development-title{
        font-size: 18px;
        font-weight: bolder;
    }
    .activity-development-all{
        font-size: 14px;
        margin-top: 5px;
    }
    .activity-development-all span{
        padding: 1px 5px;
        color: #fff;
        font-weight: bolder;
        background-color: #409EFF;
        margin-right: 5px;
    }
    .activity-development-progress{
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        padding: 0 30px;
    }
    /deep/ .el-progress__text{
        font-size: 18px !important;
        font-weight: bolder;
    }
    #courseCategoryChart{
        width: 42%;
        height: 100%;
    }
    #categoryChangeChart{
        width: 56%;
        height: 100%;
    }
</style>
