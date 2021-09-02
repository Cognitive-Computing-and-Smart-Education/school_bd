<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>年级在校人数</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="form" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="form.schoolYear" placeholder="请选择学年">
                            <el-option
                                    v-for="item in schoolYearOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="gradeBarCharts"></div>
                    <div id="gradeCharts"></div>
                </div>
            </div>
        </el-card>
        <el-card class="current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>班级在校人数</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="formClass" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="formClass.schoolYear" placeholder="请选择学年">
                            <el-option
                                    v-for="item in schoolYearOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-select v-model="formClass.grade" placeholder="请选择年级">
                            <el-option
                                    v-for="item in gradeOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="classCharts"></div>
                </div>
            </div>
        </el-card>
    </div>
</template>

<script>
    import { mapGetters, mapMutations } from "vuex";

    export default {
        name: "index",
        data() {
            return {
                form: {
                    schoolYear: '1',
                    grade: '1'
                },
                formClass: {
                    schoolYear: '1',
                    grade: '1'
                },
                schoolYearOptions: [
                    {
                        value: '1',
                        label: '2018-2019学年'
                    },{
                        value: '2',
                        label: '2019-2020学年'
                    },{
                        value: '3',
                        label: '2020-2021学年'
                    }
                ],
                gradeOptions: [
                    {
                        value: '1',
                        label: '高一年级'
                    },{
                        value: '2',
                        label: '高二年级'
                    },{
                        value: '3',
                        label: '高三年级'
                    }
                ]
            }
        },
        created() {

        },
        mounted() {
            this.init()
        },
        methods: {
            ...mapMutations(["changeClassName"]),
            init() {
                this.getGradeBarCharts();
                this.getGradeCharts();
                this.getClassCharts();
            },
            getClassCharts() {
                let myChart = this.$echarts.init(document.getElementById('classCharts'))
                myChart.setOption({
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['男', '女'],
                        textStyle: {
                            color: '#323232'
                        }
                    },
                    xAxis: {
                        type: 'category',
                        // boundaryGap: false,
                        data: ['高一（1）班', '高一（2）班', '高一（3）班', '高一（4）班', '高一（5）班', '高一（6）班'],
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
                            name: '男',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [320, 302, 301, 320, 302, 301]
                        },{
                            name: '女',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [123, 214, 145, 123, 214, 145]
                        }
                    ]
                })
                myChart.on('click', function (params) {
                    let _that = this
                    let obj = {
                        className: params.name,
                        schoolYear: this.formClass.schoolYear,
                        grade: this.formClass.grade
                    }
                    _that.changeClassName(obj)
                    // schoolYear
                    // grade
                })
            },
            getGradeCharts() {
                let myChart = this.$echarts.init(document.getElementById('gradeCharts'))
                myChart.setOption({
                    tooltip: {
                        trigger: 'item',
                        transitionDuration: 0,
                    },
                    legend: {
                        type: 'scroll',
                        orient: 'vertical',
                        top: 'center',
                        right: 80,
                        textStyle: {
                            color: '#323232',
                            fontSize: 12
                        },
                    },
                    series: [
                        {
                            name: '家庭背景',
                            type: 'pie',
                            top: 10,
                            right: 100,
                            radius: ['50%', '70%'],
                            avoidLabelOverlap: false,
                            data: [
                                {value: 64, name: '高一年级',itemStyle: {color: '#13acb5'}},
                                {value: 123, name: '高二年级',itemStyle: {color: '#60a8ff'}},
                                {value: 12, name: '高三年级',itemStyle: {color: '#e8d83b'}},
                                {value: 23, name: '复读',itemStyle: {color: '#e6823f'}},
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
            getGradeBarCharts() {
                let myChart = this.$echarts.init(document.getElementById('gradeBarCharts'))
                myChart.setOption({
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['男', '女'],
                        textStyle: {
                            color: '#323232'
                        }
                    },
                    xAxis: {
                        type: 'category',
                        // boundaryGap: false,
                        data: ['高一年级', '高二年级', '高三年级'],
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
                            name: '男',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [320, 302, 301]
                        },{
                            name: '女',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [123, 214, 145]
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
        align-items: center;
        justify-content: space-between;
    }
    .school-overview-card{
        margin-bottom: 30px;
    }
    #gradeCharts,
    #gradeBarCharts{
        width: 49%;
        height: 100%;
    }
    #classCharts{
        width: 100%;
        height: 100%;
    }
</style>
