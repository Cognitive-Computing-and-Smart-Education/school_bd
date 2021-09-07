<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>师资概况</span>
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
                                    v-for="item in teachersFormClassOptions"
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
                    <div id="teachersChangeChart"></div>
                </div>
            </div>
        </el-card>
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
                                    v-for="item in teachersFormClassOptions"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="教师名称">
                        <el-input v-model="tableForm.teacherName" placeholder="请填写教师名称"></el-input>
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
                            prop="teacherName"
                            align="center"
                            label="教师名称"
                            min-width="180">
                    </el-table-column>
                    <el-table-column
                            prop="teacherGender"
                            align="center"
                            label="教师性别"
                            min-width="100">
                    </el-table-column>
                    <el-table-column
                            prop="teacherAge"
                            align="center"
                            label="教师年龄"
                            min-width="100">
                    </el-table-column>
                    <el-table-column
                            prop="teachingCourses"
                            align="center"
                            label="教授课程"
                            min-width="100">
                    </el-table-column>
                    <el-table-column
                            prop="education"
                            align="center"
                            label="学历"
                            min-width="100">
                    </el-table-column>
                    <el-table-column
                            prop="technicalTitle"
                            align="center"
                            label="职称"
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
                teachersForm: {
                    grade: '',
                    class: ''
                },
                tableForm: {
                    grade: '',
                    class: '',
                    teacherName: ''
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
                teachersFormClassOptions: [
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
                result: {
                    data: [
                        {
                            teacherName: '1111',
                            teacherGender: '1241',
                            teacherAge: '1421',
                            teachingCourses: '1255',
                            education: '1111',
                            technicalTitle: '5122'
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
                this.getTeachersChart();
                this.getTeachersChangeChart();
                this.getTableData();
            },
            handleClick(row) {

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
            getTeachersChangeChart() {
                let myChart = this.$echarts.init(document.getElementById('teachersChangeChart'))
                myChart.setOption({
                    title: {
                        text: '教师重要职称分类历年变化趋势',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['校内专任教师', '校内兼课教师', '校外兼课教师', '校外兼职教师'],
                        textStyle: {
                            color: '#323232'
                        },
                        right: 10
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
                            name: '校内专任教师',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 30,
                            data: [320, 302, 301, 320, 302]
                        },{
                            name: '校内兼课教师',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 30,
                            data: [123, 214, 145, 123, 214]
                        },{
                            name: '校外兼课教师',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 30,
                            data: [252, 125, 23, 425, 234]
                        },{
                            name: '校外兼职教师',
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
            getTeachersChart() {
                let myChart = this.$echarts.init(document.getElementById('teachersChart'))
                myChart.setOption({
                    title: {
                        text: '教师重要职称分类数量',
                    },
                    tooltip: {
                        trigger: 'item',
                        transitionDuration: 0,
                    },
                    legend: {
                        type: 'scroll',
                        orient: 'vertical',
                        top: 'center',
                        right: 100,
                        textStyle: {
                            color: '#323232',
                            fontSize: 12
                        },
                        formatter(params) {
                            switch (params) {
                                case "校内专任教师":
                                    return params + "   " + 134;
                                    break;
                                case "校内兼课教师":
                                    return params + "   " + 421;
                                    break;
                                case "校外兼课教师":
                                    return params + "   " + 213;
                                    break;
                                case "校外兼职教师":
                                    return params + "   " + 123;
                                    break;
                                default:
                                    return "";
                            }
                        }
                    },
                    series: [
                        {
                            name: '教师重要职称分类数量',
                            type: 'pie',
                            top: 10,
                            right: 200,
                            radius: ['40%', '60%'],
                            avoidLabelOverlap: false,
                            data: [
                                {value: 134, name: '校内专任教师',itemStyle: {color: '#13acb5'}},
                                {value: 421, name: '校内兼课教师',itemStyle: {color: '#60a8ff'}},
                                {value: 213, name: '校外兼课教师',itemStyle: {color: '#e8d83b'}},
                                {value: 123, name: '校外兼职教师',itemStyle: {color: '#e66b42'}}
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
            teachersSubmit() {

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
    #teachersChart{
        width: 42%;
        height: 100%;
    }
    #teachersChangeChart{
        width: 56%;
        height: 100%;
    }
</style>
