<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>课堂作业情况分析</span>
            </div>
            <div class="">
                <div class="grade-num-box">
                    <div id="homeworkCharts"></div>
                </div>
            </div>
        </el-card>
        <el-card class="current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>课后活动情况分析</span>
            </div>
            <div class="">
                <div class="grade-num-box">
                    <div id="activitiesChart"></div>
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

            }
        },
        mounted() {
            this.init()
        },
        methods: {
            init() {
                this.getHomeworkCharts();
                this.getActivitiesChart();
            },
            getActivitiesChart() {
                let myChart = this.$echarts.init(document.getElementById('activitiesChart'))
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
                            name: '随堂测试次数',
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
            getHomeworkCharts() {
                let myChart = this.$echarts.init(document.getElementById('homeworkCharts'))
                myChart.setOption({
                    title: {
                        text: '作业情况分析',
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
            }
        }
    }
</script>

<style scoped>
    .grade-num-box{
        width: 100%;
        height: 400px;
    }
    .school-overview-card{
        margin-bottom: 30px;
    }
    #homeworkCharts,
    #activitiesChart{
        width: 100%;
        height: 100%;
    }
</style>
