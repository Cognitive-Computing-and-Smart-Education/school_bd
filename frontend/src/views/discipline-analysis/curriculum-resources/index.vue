<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>在线课程趋势</span>
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
                        <el-button type="primary" @click="onlineCourseSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="onlineCourseCharts"></div>
                </div>
            </div>
        </el-card>
        <el-card class="current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>课程资源/资料分析</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="courseResourcesForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="courseResourcesForm.grade" placeholder="请选择年级">
                            <el-option
                                    label="全校"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in courseGradeOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-select v-model="courseResourcesForm.class" placeholder="请选择班级">
                            <el-option
                                    label="全部班级"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in courseClassOptions"
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
                    <div id="courseResourcesChart"></div>
                    <div id="resourceChangeChart"></div>
                </div>
                <div class="grade-num-box" style="margin-top: 20px">
                    <div id="resourcesMaterialChart"></div>
                    <div id="dataChangeChart"></div>
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
                    class: ''
                },
                courseResourcesForm: {
                    grade: '',
                    class: ''
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
                courseGradeOptions: [
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
                courseClassOptions: [
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
                ]
            }
        },
        mounted() {
            this.init()
        },
        methods: {
            init() {
                this.getOnlineCourseCharts();
                this.getCourseResourcesChart();
                this.getResourceChangeChart();
                this.getResourcesMaterialChart();
                this.getDataChangeChart();
            },
            onSubmit() {

            },
            onlineCourseSubmit() {

            },
            getDataChangeChart() {
                let myChart = this.$echarts.init(document.getElementById('dataChangeChart'))
                myChart.setOption({
                    title: {
                        text: '教学资料近6学期变化趋势'
                    },
                    legend: {
                        data: ['音频数量', '视频数量', '文本数量', '图片数量'],
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
                            name: '音频数量',
                            type: 'line',
                            stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        },{
                            name: '视频数量',
                            type: 'line',
                            stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        },{
                            name: '文本数量',
                            type: 'line',
                            stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        },{
                            name: '图片数量',
                            type: 'line',
                            stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        }
                    ]
                })
            },
            getResourcesMaterialChart() {
                let myChart = this.$echarts.init(document.getElementById('resourcesMaterialChart'))
                myChart.setOption({
                    title: {
                        text: '教学资料数量',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['教学资料数量'],
                        textStyle: {
                            color: '#323232'
                        }
                    },
                    xAxis: {
                        type: 'category',
                        // boundaryGap: false,
                        data: ['音频数量', '视频数量', '文本数量', '图片数量'],
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
                            name: '教学资料数量',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [320, 302, 301, 421]
                        }
                    ]
                })
            },
            getResourceChangeChart() {
                let myChart = this.$echarts.init(document.getElementById('resourceChangeChart'))
                myChart.setOption({
                    title: {
                        text: '课程资源近6学期变化趋势'
                    },
                    legend: {
                        data: ['在线试卷数量', '在线习题集数量', '教学资料', '知识点数量'],
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
                            name: '在线试卷数量',
                            type: 'line',
                            stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        },{
                            name: '在线习题集数量',
                            type: 'line',
                            stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        },{
                            name: '教学资料',
                            type: 'line',
                            stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        },{
                            name: '知识点数量',
                            type: 'line',
                            stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        }
                    ]
                })
            },
            getCourseResourcesChart() {
                let myChart = this.$echarts.init(document.getElementById('courseResourcesChart'))
                myChart.setOption({
                    title: {
                        text: '课程资源分布',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['课程资源分布'],
                        textStyle: {
                            color: '#323232'
                        }
                    },
                    xAxis: {
                        type: 'category',
                        // boundaryGap: false,
                        data: ['在线试卷数量', '在线习题数量', '教学资料', '知识点数量'],
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
                            name: '课程资源分布',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [320, 302, 301, 421]
                        }
                    ]
                })
            },
            getOnlineCourseCharts() {
                let myChart = this.$echarts.init(document.getElementById('onlineCourseCharts'))
                myChart.setOption({
                    title: {
                        text: '课程反馈'
                    },
                    // legend: {
                    //     data: ['调课占比', '代课占比']
                    // },
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
                            data: [120, 132, 101, 134, 90, 230]
                        }
                    ]
                })
            }
        }
    }
</script>

<style scoped>
    .grade-num-box {
        width: 100%;
        height: 400px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    #onlineCourseCharts {
        width: 100%;
        height: 100%;
    }
    .school-overview-card{
        margin-bottom: 30px;
    }
    #courseResourcesChart,
    #resourceChangeChart,
    #resourcesMaterialChart,
    #dataChangeChart{
        width: 49%;
        height: 100%;
    }
</style>
