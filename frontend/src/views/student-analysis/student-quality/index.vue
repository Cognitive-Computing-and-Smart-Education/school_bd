<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>身心素质概况</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="mindBodyForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="mindBodyForm.grade" placeholder="请选择年级">
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
                        <el-select v-model="mindBodyForm.class" placeholder="请选择班级">
                            <el-option
                                    label="全部班级"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in mindBodyClassOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="mindBodySubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="physicalFitnessChart"></div>
                    <div id="psychologyChart"></div>
                </div>
            </div>
        </el-card>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>在校获奖概况</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="awardForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="awardForm.grade" placeholder="请选择年级">
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
                        <el-select v-model="awardForm.class" placeholder="请选择班级">
                            <el-option
                                    label="全部班级"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in awardClassOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="awardSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="awardChart"></div>
                </div>
            </div>
        </el-card>
        <el-card class="current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>社团活动概况</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="associationForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="associationForm.grade" placeholder="请选择年级">
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
                        <el-select v-model="associationForm.class" placeholder="请选择班级">
                            <el-option
                                    label="全部班级"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in associationClassOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="associationSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="associationChart"></div>
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
                mindBodyForm: {
                    grade: '',
                    class: ''
                },
                awardForm: {
                    grade: '',
                    class: ''
                },
                associationForm: {
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
                mindBodyClassOptions: [
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
                awardClassOptions: [
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
                associationClassOptions: [
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
                this.getPhysicalFitnessChart();
                this.getPsychologyChart();
                this.getAwardChart();
                this.getAssociationChart();
            },
            getAssociationChart() {
                let myChart = this.$echarts.init(document.getElementById('associationChart'))
                myChart.setOption({
                    title: {
                        text: '近6学期社团活动概况',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['加入社团数量', '参加各类讲座数量', '参加社团活动数量'],
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
                            name: '加入社团数量',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [320, 302, 301, 320, 302, 295]
                        },{
                            name: '参加各类讲座数量',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [123, 214, 145, 123, 214, 321]
                        },{
                            name: '参加社团活动数量',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [252, 125, 23, 425, 234, 245]
                        }
                    ]
                })
            },
            associationSubmit() {

            },
            getAwardChart() {
                let myChart = this.$echarts.init(document.getElementById('awardChart'))
                myChart.setOption({
                    title: {
                        text: '近6学期在校获奖概况',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['技能比赛获奖', '体育比赛获奖', '学科竞赛获奖', '其他获奖'],
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
                            name: '技能比赛获奖',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [320, 302, 301, 320, 302, 294]
                        },{
                            name: '体育比赛获奖',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [123, 214, 145, 123, 214, 251]
                        },{
                            name: '学科竞赛获奖',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [252, 125, 23, 425, 234, 287]
                        },{
                            name: '其他获奖',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [166, 79, 234, 52, 111, 301]
                        }
                    ]
                })
            },
            awardSubmit() {

            },
            getPsychologyChart() {
                let myChart = this.$echarts.init(document.getElementById('psychologyChart'))
                myChart.setOption({
                    title: {
                        text: '心理素质近6学期变化趋势',
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
                        // boundaryGap: false,
                        data: ['2018-2019第一学期', '2018-2019第二学期', '2019-2020第一学期', '2019-2020第二学期', '2020-2021第一学期', '2020-2021第二学期'],
                        axisLabel: { interval: 0, rotate: 30,color: '#323232' }
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
                            name: '心理素质近6学期变化趋势',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [89, 71, 79, 76 , 69, 80]
                        }
                    ]
                })
            },
            getPhysicalFitnessChart() {
                let myChart = this.$echarts.init(document.getElementById('physicalFitnessChart'))
                myChart.setOption({
                    title: {
                        text: '体能测试近6学期变化趋势'
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
                        axisLabel: { interval: 0, rotate: 30 },
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '体能测试近6学期变化趋势',
                            type: 'line',
                            // stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        }
                    ]
                })
            },
            mindBodySubmit() {

            },
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
    #physicalFitnessChart,
    #psychologyChart{
        width: 49%;
        height: 100%;
    }
    #awardChart,
    #associationChart{
        width: 100%;
        height: 100%
    }
</style>
