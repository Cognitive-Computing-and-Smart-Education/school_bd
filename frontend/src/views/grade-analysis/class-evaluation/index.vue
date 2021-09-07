<template>
    <div>
        <el-form :inline="true" ref="searchFrom" :model="searchFrom" :size="'medium'" class="demo-form-inline">
            <el-form-item label="学年" required>
                <el-select v-model="searchFrom.schoolYear"  placeholder="活动学年">
                    <el-option label="全部" value=""></el-option>
                    <el-option label="2021学年" value="shanghai"></el-option>
                    <el-option label="2022学年" value="beijing"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="年级" required>
                <el-select v-model="searchFrom.grade" placeholder="请选择年级">
                    <el-option label="全部" value=""></el-option>
                    <el-option label="高一" value="shanghai"></el-option>
                    <el-option label="高二" value="beijing"></el-option>
                    <el-option label="高三" value="beijing"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="班级" required>
                <el-select v-model="searchFrom.className" placeholder="请选择班级">
                    <el-option label="全部" value=""></el-option>
                    <el-option label="一班" value="shanghai"></el-option>
                    <el-option label="二班" value="beijing"></el-option>
                    <el-option label="三班" value="beijing"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit('searchFrom')">查询</el-button>
            </el-form-item>
        </el-form>
        <div class="school-overview">
            <div class="school-overview-box" style="background-image: linear-gradient(to right, #3f85e7 , #9fc8f9);">
                <div>
                    <div class="school-overview-title">班会</div>
                    <div class="school-overview-val">{{ classActivity.classMeeting }}<span>次</span></div>
                    <div class="school-overview-contrast">
                        同比去年
                        <span v-if="classActivity.classMeetingStart == 0">
                        上升&nbsp;
                        <i class="el-icon-top-right" style="font-size: 12px;color: limegreen"></i>
                    </span>
                        <span v-else>
                        下降&nbsp;
                        <i class="el-icon-bottom-right" style="font-size: 12px;color: red"></i>
                    </span>
                        {{ classActivity.classMeetingContrast }}
                    </div>
                </div>
                <div class="school-overview-icon">
                    <i class="iconfont icon-wenjian" style="color: #7ebaf8"></i>
                </div>
            </div>
            <div class="school-overview-box" style="background-image: linear-gradient(to right, #ebb53c , #fcdd95);">
                <div>
                    <div class="school-overview-title">班级交流</div>
                    <div class="school-overview-val">{{ classActivity.classCommunication }}<span>次</span></div>
                    <div class="school-overview-contrast">
                        同比去年
                        <span v-if="classActivity.classCommunicationStart == 0">
                        上升&nbsp;
                        <i class="el-icon-top-right" style="font-size: 12px;color: limegreen"></i>
                    </span>
                        <span v-else>
                        下降&nbsp;
                        <i class="el-icon-bottom-right" style="font-size: 12px;color: red"></i>
                    </span>
                        {{ classActivity.classCommunicationContrast }}
                    </div>
                </div>
                <div class="school-overview-icon">
                    <i class="iconfont icon-jiaoliu" style="color: #f3c16f"></i>
                </div>
            </div>
            <div class="school-overview-box" style="background-image: linear-gradient(to right, #fe7f48 , #fba684);">
                <div>
                    <div class="school-overview-title">宿舍走访</div>
                    <div class="school-overview-val">{{ classActivity.dormitoryVisit }}<span>次</span></div>
                    <div class="school-overview-contrast">
                        同比去年
                        <span v-if="classActivity.dormitoryVisitStart == 0">
                        上升&nbsp;
                        <i class="el-icon-top-right" style="font-size: 12px;color: limegreen"></i>
                    </span>
                        <span v-else>
                        下降&nbsp;
                        <i class="el-icon-bottom-right" style="font-size: 12px;color: red"></i>
                    </span>
                        {{ classActivity.dormitoryVisitContrast }}
                    </div>
                </div>
                <div class="school-overview-icon">
                    <i class="iconfont icon-sushe" style="font-size: 36px;color: #fa9265"></i>
                </div>
            </div>
        </div>
        <div class="class-macroscopic-box">
            <div>
                <div class="class-macroscopic-title">学生人数</div>
                <div class="class-macroscopic-val">{{ classMacroscopic.studentNo }}</div>
            </div>
            <div>
                <div class="class-macroscopic-title">学生健康指数</div>
                <div class="class-macroscopic-val">{{ classMacroscopic.studentHealth }}</div>
            </div>
            <div>
                <div class="class-macroscopic-title">班级管理指数</div>
                <div class="class-macroscopic-val">{{ classMacroscopic.classAdministration }}</div>
            </div>
            <div>
                <div class="class-macroscopic-title">班级健康指数</div>
                <div class="class-macroscopic-val">{{ classMacroscopic.classHealth }}</div>
            </div>
        </div>
        <el-card class="current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>班级学生成绩</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="achievementForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="achievementForm.subject" placeholder="请选择学科">
                            <el-option
                                    v-for="item in subjectOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-select v-model="achievementForm.examinationTime" placeholder="请选择考试时间">
                            <el-option
                                    v-for="item in examinationTimeOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="achievementSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="achievement-box">
                    <div id="achievementCharts"></div>
                </div>
            </div>
        </el-card>
        <div class="current-half-box marginTop20">
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>学生健康情况</span>
                </div>
                <div  class="current-half-height">
                    <div id="healthCharts"></div>
                </div>
            </el-card>
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>学生奖惩情况</span>
                </div>
                <div  class="current-half-height">
                    <div id="rewardCharts"></div>
                </div>
            </el-card>
        </div>
    </div>
</template>

<script>
    import { mapGetters, mapMutations } from "vuex";

    export default {
        name: "index",
        data() {
            return {
                searchFrom: {
                    schoolYear: '',
                    grade: '',
                    className: ''
                },
                classMacroscopic: {
                    studentNo: '1234',
                    studentHealth: '3214',
                    classAdministration: '1523',
                    classHealth: '5212'
                },
                classActivity: {
                    classMeeting: '1421',
                    classMeetingStart: '0',
                    classMeetingContrast: '50%',
                    classCommunication: '2332',
                    classCommunicationStart: '1',
                    classCommunicationContrast: '100%',
                    dormitoryVisit: '1111',
                    dormitoryVisitStart: '0',
                    dormitoryVisitContrast: '100%'
                },
                achievementForm: {
                    subject: '',
                    examinationTime: ''
                },
                subjectOptions: [
                    {
                        label: '数学',
                        value: '数学'
                    },{
                        label: '语文',
                        value: '语文'
                    },{
                        label: '英语',
                        value: '英语'
                    }
                ],
                examinationTimeOptions: [
                    {
                        label: '2021-10-10临时测试',
                        value: '2021-10-10临时测试'
                    },{
                        label: '2021-06-21期末考试',
                        value: '2021-06-21期末考试'
                    },{
                        label: '2021-06-22期末考试',
                        value: '2021-06-22期末考试'
                    }
                ]
            }
        },
        computed: {
            ...mapGetters(["className"]),
        },
        watch: {
            className() {
                this.init(this.className)
            }
        },
        mounted() {
            this.init()
        },
        methods: {
            ...mapMutations(["changeClassName"]),
            onSubmit(formName) {
                let _that = this
                _that.$refs[formName].validate((valid) => {
                    if (valid) {
                        _that.changeClassName(_that.searchFrom)
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            achievementSubmit() {

            },
            init(className) {
                this.getAchievementCharts(className);
                this.getHealthCharts(className);
                this.getRewardCharts(className);
            },
            getRewardCharts() {
                let myChart = this.$echarts.init(document.getElementById('rewardCharts'))
                myChart.setOption({
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['男','女'],
                        textStyle: {
                            color: '#323232'
                        }
                    },
                    xAxis: {
                        type: 'category',
                        // boundaryGap: false,
                        data: ['年级三好学生', '校级三好学生', '班级三好学生', '比赛获奖学生', '市级三好学生', '学校记过'],
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
                            barWidth: 45,
                            data: [320, 302, 301, 320, 302, 301]
                        },{
                            name: '女',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 45,
                            data: [123, 421, 231, 532, 213, 421]
                        }
                    ]
                })
            },
            getHealthCharts() {
                let myChart = this.$echarts.init(document.getElementById('healthCharts'))
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
                            name: '健康状况',
                            type: 'pie',
                            top: 10,
                            right: 100,
                            radius: ['40%', '70%'],
                            avoidLabelOverlap: false,
                            data: [
                                {value: 64, name: '患病',itemStyle: {color: '#13acb5'}},
                                {value: 123, name: '残疾',itemStyle: {color: '#60a8ff'}},
                                {value: 12, name: '正常',itemStyle: {color: '#e8d83b'}},
                                {value: 23, name: '精神疾病',itemStyle: {color: '#e6823f'}},
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
            getAchievementCharts() {
                let myChart = this.$echarts.init(document.getElementById('achievementCharts'))
                myChart.setOption({
                    grid: {
                        right: 20,
                        left: 10,
                        top: 20,
                        bottom: 10,
                        containLabel: true
                    },
                    xAxis: {
                        type: 'category',
                        // boundaryGap: false,
                        data: ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100'],
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
                            name: '分数',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 45,
                            data: [320, 302, 301, 320, 302, 301, 302, 301, 320, 302, 301]
                        }
                    ]
                })
            }
        }
    }
</script>

<style scoped>
    .class-macroscopic-box{
        width: 100%;
        background: #fff;
        height: 120px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
        margin: 30px 0;
    }
    .class-macroscopic-box>div{
        width: 33.3333%;
        text-align: center;
        border-right: 1px solid #eee;
    }
    .class-macroscopic-box>div:last-child{
        border-right: none;
    }
    .class-macroscopic-title{
        font-size: 16px;
    }
    .class-macroscopic-val{
        font-size: 20px;
        font-weight: bolder;
        margin-top: 5px;
    }
    .school-overview{
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }
    .school-overview-box{
        width: 280px;
        padding: 18px 0;
        background-color: #000;
        border-radius: 5px;
        margin-right: 40px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .school-overview-title{
        font-size: 20px;
        color: #fff;
        width: 160px;
        text-align: left;
        padding-left: 10px;
    }
    .school-overview-val{
        font-size: 18px;
        color: #fff;
        margin-top: 5px;
        width: 160px;
        text-align: left;
        padding-left: 10px;
        font-weight: bolder;
    }
    .school-overview-val span{
        font-weight: normal;
    }
    .school-overview-contrast{
        font-size: 12px;
        color: #fff;
        margin-top: 5px;
        padding-left: 10px;
    }
    .school-overview-icon{
        width: 70px;
        height: 70px;
        background-color: #fff;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 20px;
    }
    .school-overview-icon i{
        font-size: 26px;
    }
    .achievement-box{
        width: 100%;
        height: 400px;
    }
    #achievementCharts,
    #healthCharts,
    #rewardCharts{
        width: 100%;
        height: 100%;
    }
</style>
