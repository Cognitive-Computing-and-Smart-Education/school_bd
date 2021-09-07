<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>课程基本信息</span>
            </div>
            <div class="">
                <div class="grade-num-box">
                    <el-form :model="form" class="demo-form-inline" :label-width="'70px'">
                        <el-form-item label="课程名称">{{ form.courseName }}</el-form-item>
                        <el-form-item label="课程代码">{{ form.courseNum }}</el-form-item>
                        <el-form-item label="年 级">{{ form.grade }}</el-form-item>
                        <el-form-item label="班 级">{{ form.class }}</el-form-item>
                        <el-form-item label="课程类型">{{ form.courseType }}</el-form-item>
                        <el-form-item label="计划课时">{{ form.classHour }}</el-form-item>
                        <el-form-item label="教学计划">{{ form.teachingPlan || '无' }}</el-form-item>
                        <el-form-item label="课程标准">{{ form.criterionCurriculum || '无' }}</el-form-item>
                        <el-form-item label="课程性质">{{ form.courseNature || '无' }}</el-form-item>
                    </el-form>
                    <div id="courseGroupsCharts"></div>
                </div>
            </div>
        </el-card>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>课程教学资源</span>
            </div>
            <div class="">
                <div class="course-statistics-box">
                    <div>
                        <div class="course-statistics-icon" style="background-color: #8590f6"><i class="iconfont icon-jiugongge"></i></div>
                        <div class="">
                            <div class="course-statistics-title">在线试卷数量</div>
                            <div class="course-statistics-val" style="color: #8590f6">{{ informationForm.onlinePaper }}</div>
                        </div>
                    </div>
                    <div>
                        <div class="course-statistics-icon" style="background-color: #bd8af1"><i class="iconfont icon-ai-book"></i></div>
                        <div class="">
                            <div class="course-statistics-title">在线习题集数量</div>
                            <div class="course-statistics-val" style="color: #bd8af1">{{ informationForm.problemSet }}</div>
                        </div>
                    </div>
                    <div>
                        <div class="course-statistics-icon" style="background-color: #ffa895"><i class="iconfont icon-tupian" style="font-size: 30px"></i></div>
                        <div class="">
                            <div class="course-statistics-title">教学资料</div>
                            <div class="course-statistics-val" style="color: #ffa895">{{ informationForm.resourcesMaterial }}</div>
                        </div>
                    </div>
                    <div>
                        <div class="course-statistics-icon" style="background-color: #00c8ab"><i class="iconfont icon-weibiaoti--" style="font-size: 30px"></i></div>
                        <div class="">
                            <div class="course-statistics-title">知识点数量</div>
                            <div class="course-statistics-val" style="color: #00c8ab">{{ informationForm.knowledgePoints }}</div>
                        </div>
                    </div>
                </div>
                <div class="course-charts-box">
                    <div id="materialNoChart"></div>
                </div>
                <div class="course-statistics-box">
                    <div>
                        <div class="course-statistics-icon" style="background-color: #8590f6"><i class="iconfont icon-jiugongge"></i></div>
                        <div class="">
                            <div class="course-statistics-title">音频数量</div>
                            <div class="course-statistics-val" style="color: #8590f6">{{ dataClassification.audioFrequency }}</div>
                        </div>
                    </div>
                    <div>
                        <div class="course-statistics-icon" style="background-color: #bd8af1"><i class="iconfont icon-ai-book"></i></div>
                        <div class="">
                            <div class="course-statistics-title">视频数量</div>
                            <div class="course-statistics-val" style="color: #bd8af1">{{ dataClassification.video }}</div>
                        </div>
                    </div>
                    <div>
                        <div class="course-statistics-icon" style="background-color: #ffa895"><i class="iconfont icon-tupian" style="font-size: 30px"></i></div>
                        <div class="">
                            <div class="course-statistics-title">文本数量</div>
                            <div class="course-statistics-val" style="color: #ffa895">{{ dataClassification.textNo }}</div>
                        </div>
                    </div>
                    <div>
                        <div class="course-statistics-icon" style="background-color: #00c8ab"><i class="iconfont icon-weibiaoti--" style="font-size: 30px"></i></div>
                        <div class="">
                            <div class="course-statistics-title">图片数量</div>
                            <div class="course-statistics-val" style="color: #00c8ab">{{ dataClassification.pictureNo }}</div>
                        </div>
                    </div>
                </div>
                <div class="course-charts-box">
                    <div id="dataClassification"></div>
                </div>
            </div>
        </el-card>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>课程实训开展情况</span>
            </div>
            <div class="">
                <div class="grade-num-box">
                    <div id="trainingSituationChart"></div>
                    <div id="trainingDevelopmentChart"></div>
                </div>
            </div>
        </el-card>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>课程教学情况</span>
            </div>
            <div class="">
                <div class="grade-num-box" style="margin-bottom: 30px">
                    <div id="operationChart"></div>
                </div>
                <div class="grade-num-box">
                    <div id="classroomSituationChart"></div>
                </div>
            </div>
        </el-card>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>课程教学质量分析评价</span>
            </div>
            <div class="">
                <div class="grade-num-box" style="margin-bottom: 30px">
                    <div id="modulationChart"></div>
                </div>
                <div class="grade-num-box" style="margin-bottom: 30px">
                    <div id="feedbackChart"></div>
                </div>
                <div class="grade-num-box">
                    <div id="teachingEvaluation"></div>
                </div>
            </div>
        </el-card>
    </div>
</template>

<script>
    export default {
        name: "detail",
        data() {
            return {
                form: {
                    courseName: '语文',
                    courseNum: '123',
                    grade: '高一',
                    class: '高一（1）班',
                    courseType: '理论课',
                    classHour: '32',
                    teachingPlan: '',
                    criterionCurriculum: '',
                    courseNature: ''
                },
                informationForm: {
                    onlinePaper: '211',
                    problemSet: '2',
                    resourcesMaterial: '1234',
                    knowledgePoints: '2134'
                },
                dataClassification: {
                    audioFrequency: '214',
                    video: '421',
                    textNo: '5212',
                    pictureNo: '12321'
                }
            }
        },
        mounted() {
            this.init()
        },
        methods: {
            init() {
                this.getCourseGroupsCharts();
                this.getMaterialNoChart();
                this.getDataClassification();
                this.getTrainingSituationChart();
                this.getTrainingDevelopmentChart();
                this.getOperationChart();
                this.getClassroomSituationChart();
                this.getModulationChart();
                this.getFeedbackChart();
                this.getTeachingEvaluation();
            },
            getTeachingEvaluation() {
                let myChart = this.$echarts.init(document.getElementById('teachingEvaluation'))
                myChart.setOption({
                    title: {
                        text: '教学评价',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['督导评价得分', '学生评价得分', '总评评价成绩'],
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
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [320, 302, 301, 421, 123, 214]
                        },{
                            name: '学生评价得分',
                            type: 'bar',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [123, 214, 145,321, 132,321]
                        },{
                            name: '总评评价成绩',
                            type: 'bar',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [123, 214, 145,123, 214,142]
                        }
                    ]
                })
            },
            getFeedbackChart() {
                let myChart = this.$echarts.init(document.getElementById('feedbackChart'))
                myChart.setOption({
                    title: {
                        text: '课程反馈'
                    },
                    legend: {
                        data: ['调课占比', '代课占比']
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
                        boundaryGap: false,
                        data: ['2018-2019第一学期', '2018-2019第二学期', '2019-2020第一学期', '2019-2020第二学期', '2020-2021第一学期', '2020-2021第二学期'],
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '调课占比',
                            type: 'line',
                            stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        },
                        {
                            name: '代课占比',
                            type: 'line',
                            stack: '总量',
                            data: [220, 182, 191, 234, 290, 330]
                        }
                    ]
                })
            },
            getModulationChart() {
                let myChart = this.$echarts.init(document.getElementById('modulationChart'))
                myChart.setOption({
                    title: {
                        text: '课程调代课情况'
                    },
                    legend: {
                        data: ['调课占比', '代课占比']
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
                        boundaryGap: false,
                        data: ['2018-2019第一学期', '2018-2019第二学期', '2019-2020第一学期', '2019-2020第二学期', '2020-2021第一学期', '2020-2021第二学期'],
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '调课占比',
                            type: 'line',
                            stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        },
                        {
                            name: '代课占比',
                            type: 'line',
                            stack: '总量',
                            data: [220, 182, 191, 234, 290, 330]
                        }
                    ]
                })
            },
            getClassroomSituationChart() {
                let myChart = this.$echarts.init(document.getElementById('classroomSituationChart'))
                myChart.setOption({
                    title: {
                        text: '课程情况情况',
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'cross',
                            crossStyle: {
                                color: '#999'
                            }
                        }
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['随堂测验次数', '学生签到率', '学生提问率', '论坛发帖率', '答疑次数', '小组讨论次数']
                    },
                    xAxis: [
                        {
                            type: 'category',
                            data: ['2018-2019第一学期', '2018-2019第二学期', '2019-2020第一学期', '2019-2020第二学期', '2020-2021第一学期', '2020-2021第二学期'],
                            axisPointer: {
                                type: 'shadow'
                            }
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value',
                            interval: 50,
                            axisLabel: {
                                formatter: '{value} 次'
                            }
                        },
                        {
                            type: 'value',
                            interval: 5,
                            axisLabel: {
                                formatter: '{value} %'
                            }
                        }
                    ],
                    series: [
                        {
                            name: '作业布置次数',
                            type: 'bar',
                            barWidth: 35,
                            data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7]
                        },
                        {
                            name: '学生签到率',
                            type: 'line',
                            yAxisIndex: 1,
                            data: [1.3, 2.6, 2.3, 1.2, 2.1, 4.1]
                        },{
                            name: '学生提问率',
                            type: 'line',
                            yAxisIndex: 1,
                            data: [0.8, 1.5, 2.6, 1.4, 5.5, 5.8]
                        },{
                            name: '论坛发帖率',
                            type: 'line',
                            yAxisIndex: 1,
                            data: [3.1, 1.5, 1.1, 8.5, 2.3, 8.2]
                        },{
                            name: '答疑次数',
                            type: 'line',
                            yAxisIndex: 1,
                            data: [5.1, 3.4, 1.1, 2.9, 3.7, 7.1]
                        },{
                            name: '小组讨论次数',
                            type: 'line',
                            yAxisIndex: 1,
                            data: [1.0, 6.2, 2.3, 4.5, 2.3, 5.2]
                        }
                    ]
                })
            },
            getOperationChart() {
                let myChart = this.$echarts.init(document.getElementById('operationChart'))
                myChart.setOption({
                    title: {
                        text: '作业情况',
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'cross',
                            crossStyle: {
                                color: '#999'
                            }
                        }
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['作业布置次数', '作业批改率']
                    },
                    xAxis: [
                        {
                            type: 'category',
                            data: ['2018-2019第一学期', '2018-2019第二学期', '2019-2020第一学期', '2019-2020第二学期', '2020-2021第一学期', '2020-2021第二学期'],
                            axisPointer: {
                                type: 'shadow'
                            }
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value',
                            interval: 50,
                            axisLabel: {
                                formatter: '{value} 次'
                            }
                        },
                        {
                            type: 'value',
                            interval: 5,
                            axisLabel: {
                                formatter: '{value} %'
                            }
                        }
                    ],
                    series: [
                        {
                            name: '作业布置次数',
                            type: 'bar',
                            barWidth: 35,
                            data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7]
                        },
                        {
                            name: '作业批改率',
                            type: 'line',
                            yAxisIndex: 1,
                            data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2]
                        }
                    ]
                })
            },
            getCourseGroupsCharts() {
                let myChart = this.$echarts.init(document.getElementById('courseGroupsCharts'))
                myChart.setOption({
                    title: {
                        text: '课程组/教研组人数',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['正高', '副高', '中级', '初级'],
                        textStyle: {
                            color: '#323232'
                        }
                    },
                    xAxis: {
                        type: 'category',
                        // boundaryGap: false,
                        data: ['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021'],
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
                            name: '正高',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [320, 302, 301, 421, 123]
                        },{
                            name: '副高',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [123, 214, 145,321, 132]
                        },{
                            name: '中级',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [123, 214, 145,123, 214]
                        },{
                            name: '初级',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [123, 214, 145,123, 214]
                        }
                    ]
                })
            },
            getMaterialNoChart() {
                let myChart = this.$echarts.init(document.getElementById('materialNoChart'))
                myChart.setOption({
                    title: {
                        text: '课程资料情况',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['在线试卷数量', '在线习题数量', '教学资料', '知识点数量'],
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
                            name: '在线试卷数量',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 45,
                            data: [320, 302, 301, 421, 123, 214]
                        },{
                            name: '在线习题数量',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 45,
                            data: [123, 214, 145,321, 132,321]
                        },{
                            name: '教学资料',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 45,
                            data: [123, 214, 145,123, 214,142]
                        },{
                            name: '知识点数量',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 45,
                            data: [123, 214, 145,123, 214,321]
                        }
                    ]
                })
            },
            getDataClassification() {
                let myChart = this.$echarts.init(document.getElementById('dataClassification'))
                myChart.setOption({
                    title: {
                        text: '课程资料情况',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['音频数量', '视频数量', '文本数量', '图片数量'],
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
                            name: '在线试卷数量',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 45,
                            data: [320, 302, 301, 421, 123, 214]
                        },{
                            name: '在线习题数量',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 45,
                            data: [123, 214, 145,321, 132,321]
                        },{
                            name: '教学资料',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 45,
                            data: [123, 214, 145,123, 214,142]
                        },{
                            name: '知识点数量',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 45,
                            data: [123, 214, 145,123, 214,321]
                        }
                    ]
                })
            },
            getTrainingSituationChart() {
                let myChart = this.$echarts.init(document.getElementById('trainingSituationChart'))
                myChart.setOption({
                    title: {
                        text: '课程资料情况',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['计划实训', '实际开展实训'],
                        textStyle: {
                            color: '#323232'
                        }
                    },
                    xAxis: {
                        type: 'category',
                        // boundaryGap: false,
                        data: ['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021'],
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
                            name: '计划实训',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [320, 302, 301, 421, 123, 214]
                        },{
                            name: '实际开展实训',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [123, 214, 145,321, 132,321]
                        }
                    ]
                })
            },
            getTrainingDevelopmentChart() {
                let myChart = this.$echarts.init(document.getElementById('trainingDevelopmentChart'))
                myChart.setOption({
                    title: {
                        text: '实训今年开展情况',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 30,
                        bottom: 10,
                        containLabel: true
                    },
                    xAxis: {
                        type: 'category',
                        data: ['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021']
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [{
                        data: [820, 932, 901, 934, 1290],
                        type: 'line',
                        smooth: true
                    }],
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
        align-items: center;
        justify-content: space-between;
    }
    .demo-form-inline{
        width: 30%;
    }
    #courseGroupsCharts{
        width: 68%;
        height: 100%;
    }
    /deep/ .el-form-item{
        margin-bottom: 0;
    }
    /deep/ .el-form-item__label{
        margin-right: 10px;
    }
    .school-overview-card{
        margin-bottom: 30px;
    }
    .course-statistics-box{
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .course-statistics-box>div{
        width: 25%;
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }
    .course-statistics-icon{
        width: 50px;
        height: 50px;
        border-radius: 50%;
        color: #fff;
        margin-right: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .course-statistics-icon i{
        font-size: 22px;
    }
    .course-statistics-title{
        font-size: 14px;
    }
    .course-statistics-val{
        font-size: 18px;
        font-weight: bolder;
    }
    .course-charts-box{
        width: 100%;
        margin-top: 30px;
        margin-bottom: 30px;
        height: 400px;
    }
    #materialNoChart,
    #dataClassification,
    #operationChart,
    #classroomSituationChart,
    #modulationChart,
    #feedbackChart,
    #teachingEvaluation{
        width: 100%;
        height: 100%;
    }
    #trainingSituationChart,
    #trainingDevelopmentChart{
        width: 49%;
        height: 100%;
    }
</style>
