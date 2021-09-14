<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>奖学金概况</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="scholarshipForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="scholarshipForm.schoolYear" placeholder="请选择学年">
                            <el-option
                                    label="全校"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in schoolYearOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="scholarshipSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="scholarshipChart"></div>
                    <div id="scholarshipChangeChart"></div>
                </div>
            </div>
        </el-card>
        <div class="current-half-box marginTop20">
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>经济困难学生</span>
                </div>
                <el-form :inline="true" :model="economicsForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="economicsForm.schoolYear" placeholder="请选择学年">
                            <el-option
                                    label="全校"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in schoolYearOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="scholarshipSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div  class="current-half-height">
                    <div id="economicsCharts"></div>
                </div>
            </el-card>
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>体能测试</span>
                </div>
                <el-form :inline="true" :model="physicalFitnessForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="physicalFitnessForm.schoolYear" placeholder="请选择学年">
                            <el-option
                                    label="全校"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in schoolYearOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="scholarshipSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div  class="current-half-height">
                    <div id="physicalFitnessCharts"></div>
                </div>
            </el-card>
        </div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>教师基本信息表</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="tableForm" class="demo-form-inline">
                    <el-form-item>
                        <el-select v-model="tableForm.grade" placeholder="请选择年级">
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
                        <el-select v-model="tableForm.class" placeholder="请选择班级">
                            <el-option
                                    label="全部班级"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in tableClassOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="学生名称">
                        <el-input v-model="tableForm.studentName" placeholder="请填写学生名称"></el-input>
                    </el-form-item>
                    <el-form-item label="学生学号">
                        <el-input v-model="tableForm.studentNum" placeholder="请填写学生学号"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="tableSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <el-table
                        :data="result.data"
                        border
                        v-loading="loading"
                        style="width: 100%">
                    <el-table-column
                            type="index"
                            align="center"
                            width="50">
                    </el-table-column>
                    <el-table-column
                            prop="studentName"
                            align="center"
                            label="姓名"
                            min-width="180">
                    </el-table-column>
                    <el-table-column
                            prop="studentNum"
                            align="center"
                            label="学号"
                            min-width="100">
                    </el-table-column>
                    <el-table-column
                            prop="grade"
                            align="center"
                            label="年级"
                            min-width="100">
                    </el-table-column>
                    <el-table-column
                            prop="class"
                            align="center"
                            label="班级"
                            min-width="100">
                    </el-table-column>
                    <el-table-column
                            prop="gender"
                            align="center"
                            label="性别"
                            min-width="100">
                    </el-table-column>
                    <el-table-column
                            prop="health"
                            align="center"
                            label="健康状况"
                            min-width="100">
                    </el-table-column>
                    <el-table-column
                            fixed="right"
                            align="center"
                            label="操作"
                            width="100">
                        <template slot-scope="scope">
                            <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
                        </template>
                    </el-table-column>
                </el-table>
                <div class="current-pagination-box">
                    <el-pagination
                            background
                            @size-change="handleSizeChange"
                            @current-change="handleCurrentChange"
                            :current-page="currentPage"
                            :page-size="10"
                            layout="total, prev, pager, next"
                            :total="result.total">
                    </el-pagination>
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
                scholarshipForm: {
                    schoolYear: ''
                },
                schoolYearOptions: [
                    {
                        label: '2020-2021第一学期',
                        value: '2020-2021第一学期'
                    },{
                        label: '2019-2020第二学期',
                        value: '2019-2020第二学期'
                    },{
                        label: '2019-2020第一学期',
                        value: '2019-2020第一学期'
                    }
                ],
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
                tableClassOptions: [
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
                economicsForm: {
                    schoolYear: ''
                },
                physicalFitnessForm: {
                    schoolYear: ''
                },
                tableForm: {
                    grade: '',
                    class: '',
                    studentName: '',
                    studentNum: ''
                },
                result: {
                    data: [
                        {
                            studentName: '1111',
                            studentNum: '1241',
                            grade: '1421',
                            class: '1255',
                            gender: '1111',
                            health: '5122'
                        }
                    ],
                    total:  1000
                },
                currentPage: 1,
                loading: false,
            }
        },
        mounted() {
            this.init();
        },
        methods: {
            init() {
                this.getScholarshipChart();
                this.getScholarshipChangeChart();
                this.getEconomicsCharts();
                this.getPhysicalFitnessCharts();
            },
            handleClick(row) {
                this.$router.push({
                    path: '/detailsHome/studentAnalysis/studentInformation/studentInformationDetail/information',
                })
            },
            handleSizeChange(val) {
                console.log(`每页 ${val} 条`);
            },
            handleCurrentChange(val) {
                this.currentPage = val
                this.getTableData()
                // console.log(this.currentPage)
            },
            getTableData() {

            },
            tableSubmit() {

            },
            getPhysicalFitnessCharts() {
                let myChart = this.$echarts.init(document.getElementById('physicalFitnessCharts'))
                myChart.setOption({
                    title: {
                        text: '体能测试',
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
                                case "合格":
                                    return params + "   " + 134;
                                    break;
                                case "不合格":
                                    return params + "   " + 421;
                                    break;
                                default:
                                    return "";
                            }
                        }
                    },
                    series: [
                        {
                            name: '体能测试',
                            type: 'pie',
                            top: 10,
                            right: 260,
                            radius: ['40%', '60%'],
                            avoidLabelOverlap: false,
                            data: [
                                {value: 134, name: '合格',itemStyle: {color: '#13acb5'}},
                                {value: 421, name: '不合格',itemStyle: {color: '#60a8ff'}}
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
            getEconomicsCharts() {
                let myChart = this.$echarts.init(document.getElementById('economicsCharts'))
                myChart.setOption({
                    title: {
                        text: '经济困难学生占比',
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
                                case "一般困难":
                                    return params + "   " + 134;
                                    break;
                                case "特困":
                                    return params + "   " + 421;
                                    break;
                                case "建档立卡":
                                    return params + "   " + 213;
                                    break;
                                case "非经济困难":
                                    return params + "   " + 123;
                                    break;
                                default:
                                    return "";
                            }
                        }
                    },
                    series: [
                        {
                            name: '经济困难学生占比',
                            type: 'pie',
                            top: 10,
                            right: 260,
                            radius: ['40%', '60%'],
                            avoidLabelOverlap: false,
                            data: [
                                {value: 134, name: '一般困难',itemStyle: {color: '#13acb5'}},
                                {value: 421, name: '特困',itemStyle: {color: '#60a8ff'}},
                                {value: 213, name: '建档立卡',itemStyle: {color: '#e8d83b'}},
                                {value: 123, name: '非经济困难',itemStyle: {color: '#e66b42'}}
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
            getScholarshipChangeChart() {
                let myChart = this.$echarts.init(document.getElementById('scholarshipChangeChart'))
                myChart.setOption({
                    title: {
                        text: '奖学金人数变化趋势'
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
                        data: ['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021'],
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '奖学金人数变化趋势',
                            type: 'line',
                            // stack: '总量',
                            data: [120, 132, 101, 134, 90]
                        }
                    ]
                })
            },
            getScholarshipChart() {
                let myChart = this.$echarts.init(document.getElementById('scholarshipChart'))
                myChart.setOption({
                    title: {
                        text: '各奖学金占比',
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
                                case "学校奖学金":
                                    return params + "   " + 134;
                                    break;
                                case "国家奖学金":
                                    return params + "   " + 421;
                                    break;
                                case "其他奖学金":
                                    return params + "   " + 213;
                                    break;
                                default:
                                    return "";
                            }
                        }
                    },
                    series: [
                        {
                            name: '各奖学金占比',
                            type: 'pie',
                            top: 10,
                            right: 260,
                            radius: ['40%', '60%'],
                            avoidLabelOverlap: false,
                            data: [
                                {value: 134, name: '学校奖学金',itemStyle: {color: '#13acb5'}},
                                {value: 421, name: '国家奖学金',itemStyle: {color: '#60a8ff'}},
                                {value: 213, name: '其他奖学金',itemStyle: {color: '#e8d83b'}}
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
            scholarshipSubmit() {

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
    #scholarshipChart{
        width: 42%;
        height: 100%;
    }
    #scholarshipChangeChart{
        width: 56%;
        height: 100%;
    }
    #economicsCharts,
    #physicalFitnessCharts{
        width: 100%;
        height: 100%;
    }
</style>
