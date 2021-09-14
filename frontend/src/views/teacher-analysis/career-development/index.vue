<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>教师教学能力</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="teachingForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="teachingForm.grade" placeholder="请选择年级">
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
                        <el-select v-model="teachingForm.class" placeholder="请选择班级">
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
                        <el-button type="primary" @click="teachingSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="teachingChart"></div>
                </div>
            </div>
        </el-card>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>继续教育与培训</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="developmentForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="developmentForm.grade" placeholder="请选择年级">
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
                        <el-select v-model="developmentForm.class" placeholder="请选择班级">
                            <el-option
                                    label="全部班级"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in developmentClassOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="teachingSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="developmentChart"></div>
                    <div id="developmentChangeChart"></div>
                </div>
            </div>
        </el-card>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>证书获取人数</span>
            </div>
            <div class="">
                <div class="grade-num-box">
                    <div id="certificateChart"></div>
                    <div id="certificateChartTwo"></div>
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
                teachingForm: {
                    grade: '',
                    class: ''
                },
                developmentForm: {
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
                developmentClassOptions: [
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
            this.init();
        },
        methods: {
            init() {
                this.getTeachingChart();
                this.getDevelopmentChart();
                this.getDevelopmentChangeChart();
                this.getCertificateChart();
                this.getCertificateChartTwo();
            },
            getCertificateChartTwo() {
                let myChart = this.$echarts.init(document.getElementById('certificateChartTwo'))
                myChart.setOption({
                    title: {
                        text: '职业资格证',
                    },
                    series: [{
                        name: 'Pressure',
                        type: 'gauge',
                        progress: {
                            show: true,
                            color: '#409EFF'
                        },
                        detail: {
                            valueAnimation: true,
                            formatter: '{value}人'
                        },
                        data: [{
                            value: 123,
                            name: ''
                        }],
                        max: 265,
                        axisLine: {
                            show: true,
                            roundCap: true,
                            lineStyle: {
                                // color: [[1, '#E6EBF8']],
                                width: 18
                            }
                        },
                        splitLine: {
                            length: 18
                        },
                        pointer: {
                            length: '60%'
                        }
                    }]
                })
            },
            getCertificateChart() {
                let myChart = this.$echarts.init(document.getElementById('certificateChart'))
                myChart.setOption({
                    title: {
                        text: '教师资格证',
                    },
                    series: [{
                        name: 'Pressure',
                        type: 'gauge',
                        progress: {
                            show: true,
                            color: '#409EFF'
                        },
                        detail: {
                            valueAnimation: true,
                            formatter: '{value}人'
                        },
                        data: [{
                            value: 123,
                            name: ''
                        }],
                        max: 265,
                        axisLine: {
                            show: true,
                            roundCap: true,
                            lineStyle: {
                                // color: [[1, '#E6EBF8']],
                                width: 18
                            }
                        },
                        splitLine: {
                            length: 18
                        },
                        pointer: {
                            length: '60%'
                        }
                    }]
                })
            },
            getDevelopmentChangeChart() {
                let myChart = this.$echarts.init(document.getElementById('developmentChangeChart'))
                myChart.setOption({
                    title: {
                        text: '教师培训分类人次历年变化趋势',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['学历提升', '培训', '进修', '企业事件', '其他'],
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
                            name: '学历提升',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [320, 302, 301, 320, 302]
                        },{
                            name: '培训',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [123, 214, 145, 123, 214]
                        },{
                            name: '进修',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [252, 125, 23, 425, 234]
                        },{
                            name: '企业事件',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [166, 79, 234, 52, 111]
                        },{
                            name: '其他',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [123, 97, 164, 98, 188]
                        }
                    ]
                })
            },
            getDevelopmentChart() {
                let myChart = this.$echarts.init(document.getElementById('developmentChart'))
                myChart.setOption({
                    title: {
                        text: '教师培训分类人次及占比',
                    },
                    tooltip: {
                        trigger: 'item',
                        transitionDuration: 0,
                    },
                    legend: {
                        type: 'scroll',
                        orient: 'vertical',
                        top: 'center',
                        right: 140,
                        textStyle: {
                            color: '#323232',
                            fontSize: 12
                        },
                        formatter(params) {
                            switch (params) {
                                case "学历提升":
                                    return params + "   " + 134;
                                    break;
                                case "培训":
                                    return params + "   " + 421;
                                    break;
                                case "进修":
                                    return params + "   " + 213;
                                    break;
                                case "企业事件":
                                    return params + "   " + 123;
                                    break;
                                case "其他":
                                    return params + "   " + 233;
                                    break;
                                default:
                                    return "";
                            }
                        }
                    },
                    series: [
                        {
                            name: '教师职称分类数量及占比',
                            type: 'pie',
                            top: 10,
                            right: 260,
                            radius: ['40%', '60%'],
                            avoidLabelOverlap: false,
                            data: [
                                {value: 134, name: '学历提升',itemStyle: {color: '#13acb5'}},
                                {value: 421, name: '培训',itemStyle: {color: '#60a8ff'}},
                                {value: 213, name: '进修',itemStyle: {color: '#e8d83b'}},
                                {value: 123, name: '企业事件',itemStyle: {color: '#e66b42'}},
                                {value: 233, name: '其他',itemStyle: {color: '#37e83c'}}
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
            getTeachingChart() {
                let myChart = this.$echarts.init(document.getElementById('teachingChart'))
                myChart.setOption({
                    // title: {
                    //     text: '教师教学评价'
                    // },
                    legend: {
                        data: ['学生评价', '督导评价']
                    },
                    radar: {
                        // shape: 'circle',
                        indicator: [
                            { name: '语文', max: 100},
                            { name: '数学', max: 100},
                            { name: '英语', max: 100},
                            { name: '政治', max: 100},
                            { name: '生物', max: 100},
                            { name: '化学', max: 100}
                        ]
                    },
                    series: [{
                        name: '教师教学评价',
                        type: 'radar',
                        data: [
                            {
                                value: [87, 75, 61, 91, 88, 90],
                                name: '学生评价'
                            },
                            {
                                value: [85, 97, 72, 85, 81, 79],
                                name: '督导评价'
                            }
                        ]
                    }]
                })
            },
            teachingSubmit() {

            },
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
    #teachingChart{
        width: 100%;
        height: 100%;
    }
    #developmentChart{
        width: 42%;
        height: 100%;
    }
    #developmentChangeChart{
        width: 56%;
        height: 100%;
    }
    #certificateChart{
        width: 50%;
        height: 100%;
    }
    #certificateChartTwo{
        width: 50%;
        height: 100%;
    }
</style>
