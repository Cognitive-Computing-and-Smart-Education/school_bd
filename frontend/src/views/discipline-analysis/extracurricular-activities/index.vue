<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>课程资源/资料分析</span>
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
                        <el-button type="primary" @click="onSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div class="activity-development-box">
                        <div class="activity-development-title">课外活动数量分析</div>
                        <div class="activity-development-all">课外活动预计开展总数： <span v-for="(item,index) in developmentList" :key="index">{{ item }}</span>个</div>
                        <div class="activity-development-progress">
                            <el-progress type="circle" :percentage="25" :width="270" :stroke-width="22" :show-text="false"></el-progress>
                            <div class="activity-development-progress-text">
                                <div>{{ developmentData }}</div>
                                <div>活动开展数</div>
                            </div>
                        </div>
                    </div>
                    <div id="developmentChangeChart"></div>
                </div>
            </div>
        </el-card>
        <el-card class="current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>课外活动的开展率</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="activityForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="activityForm.grade" placeholder="请选择年级">
                            <el-option
                                    label="全校"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in activityGradeOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-select v-model="activityForm.class" placeholder="请选择班级">
                            <el-option
                                    label="全部班级"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in activityClassOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="activitySubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="activityRateCharts"></div>
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
                activityForm: {
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
                activityGradeOptions: [
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
                activityClassOptions: [
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
                developmentList: [1,2,0],
                developmentData: 107
            }
        },
        mounted() {
            this.init()
        },
        methods: {
            init() {
                this.getDevelopmentChangeChart();
                this.getActivityRateCharts();
            },
            activitySubmit() {

            },
            onSubmit() {

            },
            getActivityRateCharts() {
                let myChart = this.$echarts.init(document.getElementById('activityRateCharts'))
                myChart.setOption({
                    title: {
                        text: '课外活动的开展率'
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
                            name: '课外活动的开展率',
                            type: 'line',
                            // stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        }
                    ]
                })
            },
            getDevelopmentChangeChart() {
                let myChart = this.$echarts.init(document.getElementById('developmentChangeChart'))
                myChart.setOption({
                    title: {
                        text: '课外活动开展近6个学期变化趋势',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['计划课外活动总数', '实际开展数量'],
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
                            name: '计划课外活动总数',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [320, 302, 301, 421, 123, 214]
                        },{
                            name: '实际开展数量',
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
            }
        }
    }
</script>

<style scoped>
    .grade-num-box {
        width: 100%;
        height: 400px;
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
    }
    #activityRateCharts {
        width: 100%;
        height: 100%;
    }
    .school-overview-card{
        margin-bottom: 30px;
    }
    #developmentChangeChart{
        width: 60%;
        height: 100%;
    }
    .activity-development-box{
        width: 38%;
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
    }
    .activity-development-progress-text{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    .activity-development-progress-text>div{
        font-size: 24px;
        text-align: center;
        color: #409EFF;
    }
    .activity-development-progress-text>div:first-child{
        margin-bottom: 10px;
        font-weight: bolder;
    }
</style>
