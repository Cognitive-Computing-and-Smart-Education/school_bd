<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>学科平均成绩概况</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="subjectForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="subjectForm.grade" placeholder="请选择年级">
                            <el-option
                                    v-for="item in gradeOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-select v-model="subjectForm.subject" placeholder="请选择学科">
                            <el-option
                                    v-for="item in subjectOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-select v-model="subjectChangeForm.time" placeholder="请选择考试场次">
                            <el-option
                                    v-for="item in timeOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="subjectSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="subjectChart"></div>
                </div>
            </div>
        </el-card>
        <el-card class="current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>学科平均成绩概况</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="subjectChangeForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="subjectChangeForm.grade" placeholder="请选择年级">
                            <el-option
                                    v-for="item in gradeOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-select v-model="subjectChangeForm.subject" placeholder="请选择学科">
                            <el-option
                                    v-for="item in subjectChangeOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-select v-model="subjectChangeForm.time" placeholder="请选择学期">
                            <el-option
                                    v-for="item in timeChangeOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="subjectSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="subjectChangeChart"></div>
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
                subjectForm: {
                    grade: '高一',
                    subject: '语文',
                    time: '0'
                },
                subjectChangeForm: {
                    grade: '高一',
                    subject: '语文',
                    time: '0'
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
                timeOptions: [
                    {
                        label: '期中',
                        value: '0'
                    },{
                        label: '期末',
                        value: '1'
                    },{
                        label: '月中',
                        value: '2'
                    }
                ],
                timeChangeOptions: [
                    {
                        label: '2019-2020第一学期',
                        value: '0'
                    },{
                        label: '2020-2021第二学期',
                        value: '1'
                    },{
                        label: '2020-2021第一学期',
                        value: '2'
                    }
                ],
                subjectOptions: [
                    {
                        label: '语文',
                        value: '语文'
                    },{
                        label: '数学',
                        value: '数学'
                    },{
                        label: '英语',
                        value: '英语'
                    }
                ],
                subjectChangeOptions: [
                    {
                        label: '语文',
                        value: '语文'
                    },{
                        label: '数学',
                        value: '数学'
                    },{
                        label: '英语',
                        value: '英语'
                    }
                ],
            }
        },
        mounted() {
            this.init()
        },
        methods: {
            init() {
                this.getSubjectChart();
                this.getSubjectChangeChart();
            },
            getSubjectChangeChart() {
                let myChart = this.$echarts.init(document.getElementById('subjectChangeChart'))
                myChart.setOption({
                    title: {
                        text: '学科考试平均分变化趋势'
                    },
                    legend: {
                        data: ['高一（1）班', '高一（2）班', '高一（3）班', '高一（4）班'],
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
                        data: ['月中', '月末', '一模', '二模', '期中', '期末'],
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '高一（1）班',
                            type: 'line',
                            // stack: '总量',
                            data: [89, 91, 78, 87, 90, 84]
                        },{
                            name: '高一（2）班',
                            type: 'line',
                            // stack: '总量',
                            data: [76, 89, 75, 81, 90, 71]
                        },{
                            name: '高一（3）班',
                            type: 'line',
                            // stack: '总量',
                            data: [71, 81, 79, 90, 81, 69]
                        },{
                            name: '高一（4）班',
                            type: 'line',
                            // stack: '总量',
                            data: [80, 68, 61, 90, 87, 79]
                        }
                    ]
                })
            },
            getSubjectChart() {
                let myChart = this.$echarts.init(document.getElementById('subjectChart'))
                myChart.setOption({
                    title: {
                        text: '学科成绩平均概况',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['学科成绩平均概况'],
                        textStyle: {
                            color: '#323232'
                        }
                    },
                    xAxis: {
                        type: 'category',
                        // boundaryGap: false,
                        data: ['高一（1）班', '高一（2）班', '高一（3）班', '高一（4）班', '高一（5）班', '高一（6）班', '高一（7）班'],
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
                            data: [89, 71, 79, 76 , 69, 80, 72]
                        }
                    ]
                })
            },
            subjectSubmit() {

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
    #subjectChart,
    #subjectChangeChart{
        width: 100%;
        height: 100%;
    }
</style>
