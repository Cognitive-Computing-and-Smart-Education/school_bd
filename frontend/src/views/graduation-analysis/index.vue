<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>升学概况</span>
            </div>
            <div class="grade-num-box">
                <div id="enrollmentChart"></div>
                <div id="enrollmentRateChart"></div>
            </div>
        </el-card>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>升学去向</span>
            </div>
            <el-form-item>
                <el-select v-model="particularYear" placeholder="请选择年份">
                    <el-option
                            v-for="item in particularYearOptions"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <div class="grade-num-box">
                <div id="whereaboutsChart"></div>
                <div id="studyAreaChart"></div>
            </div>
        </el-card>
        <el-card class="current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>班级升学概况</span>
            </div>
            <div class="">
                <el-form-item>
                    <el-select v-model="particularYearTwo" placeholder="请选择年份">
                        <el-option
                                v-for="item in particularYearOptions"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                        </el-option>
                    </el-select>
                </el-form-item>
                <div class="grade-num-box">
                    <div id="classEnrollmentChart"></div>
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
                particularYear: '2021年',
                particularYearTwo: '2021年',
                particularYearOptions: [
                    {
                        label: '2021年',
                        value: '2021年'
                    },{
                        label: '2020年',
                        value: '2020年'
                    },{
                        label: '2019年',
                        value: '2019年'
                    }
                ]
            }
        },
        mounted() {
            this.init();
        },
        methods: {
            init() {
                this.getEnrollmentChart();
                this.getEnrollmentRateChart();
                this.getWhereaboutsChart();
                this.getStudyAreaChart();
                this.getClassEnrollmentChart();
            },
            getClassEnrollmentChart() {
                let myChart = this.$echarts.init(document.getElementById('classEnrollmentChart'))
                myChart.setOption({
                    title: {
                        text: this.particularYearTwo + '班级升学概况',
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
                        data: ['升学人数', '升学率']
                    },
                    xAxis: [
                        {
                            type: 'category',
                            data: ['高三（1）班', '高三（2）班', '高三（3）班', '高三（4）班', '高三（5）班', '高三（6）班'],
                            axisPointer: {
                                type: 'shadow'
                            }
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value',
                            interval: 30,
                            axisLabel: {
                                formatter: '{value} 个'
                            }
                        },
                        {
                            type: 'value',
                            interval: 50,
                            axisLabel: {
                                formatter: '{value} %'
                            }
                        }
                    ],
                    series: [
                        {
                            name: '升学人数',
                            type: 'bar',
                            barWidth: 35,
                            data: [53, 49, 61, 57, 55, 54]
                        },
                        {
                            name: '升学率',
                            type: 'line',
                            yAxisIndex: 1,
                            data: [98, 99, 96, 97, 99, 92]
                        }
                    ]
                })
            },
            getStudyAreaChart() {
                let myChart = this.$echarts.init(document.getElementById('studyAreaChart'))
                myChart.setOption({
                    title: {
                        text: this.particularYear + '升学地区分布',
                    },
                    tooltip: {
                        trigger: 'item',
                        transitionDuration: 0,
                    },
                    legend: {
                        type: 'scroll',
                        orient: 'vertical',
                        top: 'center',
                        right: 160,
                        textStyle: {
                            color: '#323232',
                            fontSize: 12
                        }
                    },
                    series: [
                        {
                            name: this.particularYear + '升学地区分布',
                            type: 'pie',
                            top: 10,
                            right: 260,
                            radius: ['40%', '60%'],
                            avoidLabelOverlap: false,
                            data: [
                                {value: 134, name: '省内',itemStyle: {color: '#13acb5'}},
                                {value: 421, name: '省外',itemStyle: {color: '#60a8ff'}},
                                {value: 213, name: '国外',itemStyle: {color: '#e8d83b'}}
                            ],
                            emphasis: {
                                itemStyle: {
                                    shadowBlur: 10,
                                    shadowOffsetX: 0,
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                            }
                        }
                    ]
                })
            },
            getWhereaboutsChart() {
                let myChart = this.$echarts.init(document.getElementById('whereaboutsChart'))
                myChart.setOption({
                    title: {
                        text: this.particularYear + '升学去向',
                    },
                    tooltip: {
                        trigger: 'item',
                        transitionDuration: 0,
                    },
                    legend: {
                        type: 'scroll',
                        orient: 'vertical',
                        top: 'center',
                        right: 160,
                        textStyle: {
                            color: '#323232',
                            fontSize: 12
                        }
                    },
                    series: [
                        {
                            name: this.particularYear + '升学去向',
                            type: 'pie',
                            top: 10,
                            right: 260,
                            radius: ['40%', '60%'],
                            avoidLabelOverlap: false,
                            data: [
                                {value: 134, name: '普通',itemStyle: {color: '#13acb5'}},
                                {value: 421, name: '重点',itemStyle: {color: '#60a8ff'}},
                                {value: 213, name: '985',itemStyle: {color: '#e8d83b'}},
                                {value: 123, name: '211',itemStyle: {color: '#e66b42'}},
                                {value: 24, name: '留学',itemStyle: {color: '#6ae665'}}
                            ],
                            emphasis: {
                                itemStyle: {
                                    shadowBlur: 10,
                                    shadowOffsetX: 0,
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                            }
                        }
                    ]
                })
            },
            getEnrollmentRateChart() {
                let myChart = this.$echarts.init(document.getElementById('enrollmentRateChart'))
                myChart.setOption({
                    title: {
                        text: '学校近5年升学率变化'
                    },
                    // legend: {
                    //     data: ['引进人才数量', '流失人才数量', '高层次人才数量'],
                    //     right: 30
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
                        data: ['2017', '2018', '2019', '2020', '2021'],
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '学校近5年升学率变化',
                            type: 'line',
                            // stack: '总量',
                            data: [152, 242, 231, 521, 132]
                        }
                    ]
                })
            },
            getEnrollmentChart() {
                let myChart = this.$echarts.init(document.getElementById('enrollmentChart'))
                myChart.setOption({
                    title: {
                        text: '学校升学近5年概况',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['毕业人数', '本科', '专科', '留学'],
                        textStyle: {
                            color: '#323232'
                        }
                    },
                    xAxis: {
                        type: 'category',
                        // boundaryGap: false,
                        data: ['2017', '2018', '2019', '2020', '2021'],
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
                            name: '毕业人数',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [565, 611, 632, 621, 599]
                        },{
                            name: '本科',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [123, 214, 145, 123, 214]
                        },{
                            name: '专科',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [252, 125, 23, 425, 234]
                        },{
                            name: '留学',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [166, 79, 234, 52, 111]
                        }
                    ]
                })
            }
        }
    }
</script>

<style scoped>
    .school-overview-card{
        margin-bottom: 30px;
    }
    .grade-num-box{
        width: 100%;
        height: 400px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    #enrollmentChart,
    #enrollmentRateChart,
    #whereaboutsChart,
    #studyAreaChart{
        width: 49%;
        height: 100%;
    }
    #classEnrollmentChart{
        width: 100%;
        height: 100%;
    }
</style>
