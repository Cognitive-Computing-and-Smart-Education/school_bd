<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>年级在校人数</span>
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
                        <el-button type="primary" @click="coursesNumSubmit">查询</el-button>
                    </el-form-item>
                </el-form>
                <div class="grade-num-box">
                    <div id="coursesNumCharts"></div>
                    <div id="curriculumChangeCharts"></div>
                </div>
            </div>
        </el-card>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>各课程详细数据</span>
            </div>
            <div class="">
                <el-form :inline="true" :model="tableForm" class="demo-form-inline">
                    <el-form-item label="年级">
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
                    <el-form-item label="班级">
                        <el-select v-model="tableForm.className" placeholder="请选择班级">
                            <el-option
                                    label="全部"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in classNameOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="课程类型">
                        <el-select v-model="tableForm.courseType" placeholder="请选择课程类型">
                            <el-option
                                    label="全校"
                                    value="">
                            </el-option>
                            <el-option
                                    v-for="item in courseTypeOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="课程名称">
                        <el-input v-model="tableForm.courseName" placeholder="请填写课程名称"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmit">查询</el-button>
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
                            prop="curriculumName"
                            align="center"
                            label="课程名称"
                            min-width="180">
                    </el-table-column>
                    <el-table-column
                            prop="curriculumNo"
                            align="center"
                            label="课程编码"
                            min-width="100">
                    </el-table-column>
                    <el-table-column
                            prop="courseType"
                            align="center"
                            label="课程类型"
                            min-width="100">
                    </el-table-column>
                    <el-table-column
                            prop="totalClassHours"
                            align="center"
                            label="总学时"
                            min-width="100">
                    </el-table-column>
                    <el-table-column
                            prop="grade"
                            align="center"
                            label="年级"
                            min-width="100">
                    </el-table-column>
                    <el-table-column
                            prop="className"
                            align="center"
                            label="班级"
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
                form: {
                    grade: ''
                },
                gradeOptions: [
                    {
                        label: '高一年级',
                        value: '高一年级'
                    },{
                        label: '高二年级',
                        value: '高二年级'
                    },{
                        label: '高三年级',
                        value: '高三年级'
                    }
                ],
                classNameOptions: [
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
                courseTypeOptions: [
                    {
                        label: '实践课',
                        value: '实践课'
                    },{
                        label: '理论+实践课',
                        value: '理论+实践课'
                    },{
                        label: '理论课',
                        value: '理论课'
                    }
                ],
                tableForm: {
                    grade: '',
                    className: '',
                    courseType: '',
                    courseName: ''
                },
                result: {
                    data: [
                        {
                          curriculumName: '1111',
                          curriculumNo: '111',
                          courseType: '11',
                          totalClassHours: '1',
                          grade: '1111',
                          className: '11'
                        }
                    ],
                    total:  1000
                },
                currentPage: 1,
                loading: false,
            }
        },
        mounted() {
            this.init()
        },
        methods: {
            init() {
                this.getCoursesNumCharts();
                this.getCurriculumChangeCharts();
                this.getTableData();
            },
            coursesNumSubmit() {

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
            onSubmit() {

            },
            handleClick(row) {
                this.$router.push({
                    path: '/detailsHome/disciplineAnalysis/disciplineOverview/disciplineOverviewDetail',
                })
            },
            getCurriculumChangeCharts() {
                let myChart = this.$echarts.init(document.getElementById('curriculumChangeCharts'))
                myChart.setOption({
                    title: {
                        text: '课程近6学期变化趋势',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['实践课', '理论+实践课', '理论课'],
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
                            name: '实践课',
                            type: 'line',
                            stack: '总量',
                            data: [120, 132, 101, 134, 90, 230, 210]
                        },
                        {
                            name: '理论+实践课',
                            type: 'line',
                            stack: '总量',
                            data: [220, 182, 191, 234, 290, 330, 310]
                        },
                        {
                            name: '理论课',
                            type: 'line',
                            stack: '总量',
                            data: [150, 232, 201, 154, 190, 330, 410]
                        }
                    ]
                })
            },
            getCoursesNumCharts() {
                let myChart = this.$echarts.init(document.getElementById('coursesNumCharts'))
                myChart.setOption({
                    title: {
                        text: '课程数量及占比',
                    },
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
                            name: '课程数量及占比',
                            type: 'pie',
                            top: 10,
                            right: 100,
                            radius: ['50%', '70%'],
                            avoidLabelOverlap: false,
                            data: [
                                {value: 64, name: '理论课',itemStyle: {color: '#13acb5'}},
                                {value: 123, name: '理论+实践课',itemStyle: {color: '#60a8ff'}},
                                {value: 12, name: '实践课',itemStyle: {color: '#e8d83b'}}
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
    #coursesNumCharts,
    #curriculumChangeCharts{
        width: 49%;
        height: 100%;
    }
</style>
