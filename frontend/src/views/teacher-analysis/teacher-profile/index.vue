<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>职称等级分布</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="titleGradeForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="titleGradeForm.grade" placeholder="请选择年级">
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
                        <el-select v-model="titleGradeForm.class" placeholder="请选择班级">
                            <el-option
                                    label="全部班级"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in titleGradeClassOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="titleGradeSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="technicalTitleChart"></div>
                    <div id="titleChangeChart"></div>
                </div>
            </div>
        </el-card>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>高层次人才流动</span>
            </div>
            <div class="grade-num-box">
                <div id="talentFlowChart"></div>
                <div id="talentChangeChart"></div>
            </div>
        </el-card>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>年龄分布</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="ageForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="ageForm.grade" placeholder="请选择年级">
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
                        <el-select v-model="ageForm.class" placeholder="请选择班级">
                            <el-option
                                    label="全部班级"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in ageClassOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="ageSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="ageDistributionChart"></div>
                    <div id="ageChangeChart"></div>
                </div>
            </div>
        </el-card>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>学历分布</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="educationForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="educationForm.grade" placeholder="请选择年级">
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
                        <el-select v-model="educationForm.class" placeholder="请选择班级">
                            <el-option
                                    label="全部班级"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in educationClassOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="educationSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="educationChart"></div>
                    <div id="educationChangeChart"></div>
                </div>
            </div>
        </el-card>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>师生比例</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="teachersForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="teachersForm.grade" placeholder="请选择年级">
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
                        <el-select v-model="teachersForm.class" placeholder="请选择班级">
                            <el-option
                                    label="全部班级"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in teachersClassOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="teachersSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="teachersChart"></div>
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
                titleGradeForm: {
                    grade: '',
                    class: ''
                },
                ageForm: {
                    grade: '',
                    class: ''
                },
                educationForm: {
                    grade: '',
                    class: ''
                },
                teachersForm: {
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
                titleGradeClassOptions: [
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
                ageClassOptions: [
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
                educationClassOptions: [
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
                teachersClassOptions: [
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
                this.getTechnicalTitleChart();
                this.getTitleChangeChart();
                this.getTalentFlowChart();
                this.getTalentChangeChart();
                this.getAgeDistributionChart();
                this.getAgeChangeChart();
                this.getEducationChart();
                this.getEducationChangeChart();
                this.getTeachersChart();
            },
            getTeachersChart() {
                let myChart = this.$echarts.init(document.getElementById('teachersChart'))
                myChart.setOption({
                    title: {
                        text: '师生历年占比变化趋势',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['教师', '学生'],
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
                            name: '学生',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 45,
                            data: [564, 645, 555, 613, 710]
                        },{
                            name: '教师',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 45,
                            data: [55, 67, 53, 49, 71]
                        }
                    ]
                })
            },
            teachersSubmit() {

            },
            getEducationChangeChart() {
                let myChart = this.$echarts.init(document.getElementById('educationChangeChart'))
                myChart.setOption({
                    title: {
                        text: '教师学历分布历年变化趋势',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['大专', '本科', '研究生', '博士'],
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
                            name: '大专',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 30,
                            data: [320, 302, 301, 320, 302]
                        },{
                            name: '本科',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 30,
                            data: [123, 214, 145, 123, 214]
                        },{
                            name: '研究生',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 30,
                            data: [252, 125, 23, 425, 234]
                        },{
                            name: '博士',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 30,
                            data: [132, 111, 99, 213, 126]
                        }
                    ]
                })
            },
            getEducationChart() {
                let myChart = this.$echarts.init(document.getElementById('educationChart'))
                myChart.setOption({
                    title: {
                        text: '教师学历分布数量及占比',
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
                            name: '教师学历分布数量及占比',
                            type: 'pie',
                            top: 10,
                            right: 260,
                            radius: ['40%', '60%'],
                            avoidLabelOverlap: false,
                            data: [
                                {value: 134, name: '大专',itemStyle: {color: '#13acb5'}},
                                {value: 421, name: '本科',itemStyle: {color: '#60a8ff'}},
                                {value: 213, name: '研究生',itemStyle: {color: '#e8d83b'}},
                                {value: 213, name: '博士',itemStyle: {color: '#e66b42'}}
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
            educationSubmit() {

            },
            ageSubmit() {

            },
            getAgeChangeChart() {
                let myChart = this.$echarts.init(document.getElementById('ageChangeChart'))
                myChart.setOption({
                    title: {
                        text: '教师年龄分布历年变化趋势',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['35岁及以下', '36-60岁', '60岁以上'],
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
                            name: '35岁及以下',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 30,
                            data: [320, 302, 301, 320, 302]
                        },{
                            name: '36-60岁',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 30,
                            data: [123, 214, 145, 123, 214]
                        },{
                            name: '60岁以上',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 30,
                            data: [252, 125, 23, 425, 234]
                        }
                    ]
                })
            },
            getAgeDistributionChart() {
                let myChart = this.$echarts.init(document.getElementById('ageDistributionChart'))
                myChart.setOption({
                    title: {
                        text: '教师年龄分布数量及占比',
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
                            name: '教师年龄分布数量及占比',
                            type: 'pie',
                            top: 10,
                            right: 260,
                            radius: ['40%', '60%'],
                            avoidLabelOverlap: false,
                            data: [
                                {value: 134, name: '35岁及以下',itemStyle: {color: '#13acb5'}},
                                {value: 421, name: '36-60岁',itemStyle: {color: '#60a8ff'}},
                                {value: 213, name: '60岁以上',itemStyle: {color: '#e8d83b'}}
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
            getTalentChangeChart() {
                let myChart = this.$echarts.init(document.getElementById('talentChangeChart'))
                myChart.setOption({
                    title: {
                        text: '教师人才流动趋势'
                    },
                    legend: {
                        data: ['引进人才数量', '流失人才数量', '高层次人才数量'],
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
                        data: ['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021'],
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '引进人才数量',
                            type: 'line',
                            // stack: '总量',
                            data: [152, 242, 231, 521, 132]
                        },{
                            name: '流失人才数量',
                            type: 'line',
                            // stack: '总量',
                            data: [120, 132, 101, 134, 90]
                        },{
                            name: '高层次人才数量',
                            type: 'line',
                            // stack: '总量',
                            data: [142, 52, 211, 165, 98]
                        }
                    ]
                })
            },
            getTalentFlowChart() {
                let myChart = this.$echarts.init(document.getElementById('talentFlowChart'))
                myChart.setOption({
                    title: {
                        text: '高层次人才情况',
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
                            name: '教师职称分类数量及占比',
                            type: 'pie',
                            top: 10,
                            right: 260,
                            radius: ['40%', '60%'],
                            avoidLabelOverlap: false,
                            data: [
                                {value: 134, name: '引进人才数量',itemStyle: {color: '#13acb5'}},
                                {value: 421, name: '流失人才数量',itemStyle: {color: '#60a8ff'}},
                                {value: 213, name: '高层次人才数量',itemStyle: {color: '#e8d83b'}}
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
            getTitleChangeChart() {
                let myChart = this.$echarts.init(document.getElementById('titleChangeChart'))
                myChart.setOption({
                    title: {
                        text: '教师职称分类历年变化趋势',
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
                            data: [320, 302, 301, 320, 302]
                        },{
                            name: '副高',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [123, 214, 145, 123, 214]
                        },{
                            name: '中级',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [252, 125, 23, 425, 234]
                        },{
                            name: '初级',
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
            },
            getTechnicalTitleChart() {
                let myChart = this.$echarts.init(document.getElementById('technicalTitleChart'))
                myChart.setOption({
                    title: {
                        text: '教师职称分类数量及占比',
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
                        },
                        formatter(params) {
                            switch (params) {
                                case "正高":
                                    return params + "   " + 134;
                                    break;
                                case "副高":
                                    return params + "   " + 421;
                                    break;
                                case "中级":
                                    return params + "   " + 213;
                                    break;
                                case "初级":
                                    return params + "   " + 123;
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
                                {value: 134, name: '正高',itemStyle: {color: '#13acb5'}},
                                {value: 421, name: '副高',itemStyle: {color: '#60a8ff'}},
                                {value: 213, name: '中级',itemStyle: {color: '#e8d83b'}},
                                {value: 123, name: '初级',itemStyle: {color: '#e66b42'}}
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
            titleGradeSubmit() {

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
    #technicalTitleChart,
    #talentFlowChart,
    #ageDistributionChart,
    #educationChart{
        width: 42%;
        height: 100%;
    }
    #titleChangeChart,
    #talentChangeChart,
    #ageChangeChart,
    #educationChangeChart{
        width: 56%;
        height: 100%;
    }
    .school-overview-card{
        margin-bottom: 30px;
    }
    #teachersChart{
        width: 100%;
        height: 100%;
    }
</style>
