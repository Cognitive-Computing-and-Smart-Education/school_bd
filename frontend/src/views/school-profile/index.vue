<template>
    <div class="current-main-box">
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>学校简介</span>
            </div>
            <div  class="text item">
                <div class="school-overview">
                    <div class="school-overview-box" style="background-image: linear-gradient(to bottom right, #eda472 , #e6762b);">
                        <div class="school-overview-title">在校人数</div>
                        <div class="school-overview-val">{{ overview.studentsNo }}<span>人</span></div>
                    </div>
                    <div class="school-overview-box" style="background-image: linear-gradient(to bottom right, #8ea8d8 , #233d6d);">
                        <div class="school-overview-title">教师人数</div>
                        <div class="school-overview-val">{{ overview.teacherNo }}<span>人</span></div>
                    </div>
                    <div class="school-overview-box" style="background-image: linear-gradient(to bottom right, #a2a2a2 , #585858);">
                        <div class="school-overview-title">图书馆藏</div>
                        <div class="school-overview-val">{{ overview.bookNo }}<span>本</span></div>
                    </div>
                    <div class="school-overview-box" style="background-image: linear-gradient(to bottom right, #f8d15b , #896700);">
                        <div class="school-overview-title">占地面积</div>
                        <div class="school-overview-val">{{ overview.area }}<span>㎡</span></div>
                    </div>
                    <div class="school-overview-box" style="background-image: linear-gradient(to bottom right, #9fc884 , #3e6027);">
                        <div class="school-overview-title">多媒体教室</div>
                        <div class="school-overview-val">{{ overview.classroom }}<span>间</span></div>
                    </div>
                </div>
                <div class="school-synopsis">
                    <div class="school-name">{{ school.name }}</div>
                    <div class="school-text">{{ school.text }}</div>
                </div>
            </div>
        </el-card>
        <div class="current-half-box marginTop20">
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>学生人数</span>
                </div>
                <div  class="current-half-height">
                    <div id="studentsCharts"></div>
                </div>
            </el-card>
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>教职工人数</span>
                </div>
                <div  class="current-half-height">
                    <div id="facultyCharts"></div>
                </div>
            </el-card>
        </div>
        <div class="current-half-box marginTop20">
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>图书总量</span>
                </div>
                <div  class="current-half-height">
                    <div id="bookCharts"></div>
                </div>
            </el-card>
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>师生总数</span>
                </div>
                <div  class="current-half-height">
                    <div id="shiShengCharts"></div>
                </div>
            </el-card>
        </div>
    </div>
</template>

<script>
    export default {
        name: "index",
        data() {
            return {
                overview: {
                    studentsNo: '1234',
                    teacherNo: '129',
                    bookNo: '2222',
                    area: '1222',
                    classroom: '123'
                },
                school: {
                    name: '云南师范大学附属中学',
                    text: '云南师大附中是一所历史悠久、治学严谨、学风浓厚、人才辈出、在省内外基础教育界享有盛名的省属一级一等完' +
                        '全中学，是云南省科技教育的示范学校，是国家基础教育重点科研课题基地学校，是全国现代教育技术实验学校，是中' +
                        '国教育学会高中教育专业委员会、全国部分大学附中协作体、全国知名中学科研联合体的理事单位，是全国民族团结先' +
                        '进单位、全国教育系统先进集体。'
                }
            }
        },
        mounted() {
            this.init()
        },
        methods: {
            init() {
                this.getStudentsCharts();
                this.getFacultyCharts();
                this.getBookCharts();
                this.getShiShengCharts();
            },
            getShiShengCharts() {
                let myChart = this.$echarts.init(document.getElementById('shiShengCharts'))
                myChart.setOption({
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['学生人数', '教师人数'],
                        textStyle: {
                            color: '#323232'
                        }
                    },
                    yAxis: {
                        type: 'category',
                        // boundaryGap: false,
                        data: ['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021'],
                        axisLabel: {
                            color: '#323232'
                        }
                    },
                    xAxis: {
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
                            name: '学生人数',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 25,
                            data: [320, 302, 301, 334, 390]
                        },
                        {
                            name: '教师人数',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 25,
                            data: [120, 132, 101, 134, 90]
                        }
                    ]
                })
            },
            getBookCharts() {
                let myChart = this.$echarts.init(document.getElementById('bookCharts'))
                myChart.setOption({
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['纸质图书', '电子资源'],
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
                                color: '#142852'
                            }
                        },
                        axisLabel: {
                            color: '#323232'
                        }
                    },
                    series: [
                        {
                            name: '纸质图书',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 25,
                            data: [320, 302, 301, 334, 390]
                        },
                        {
                            name: '电子资源',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 25,
                            data: [120, 132, 101, 134, 90]
                        }
                    ]
                })
            },
            getFacultyCharts() {
                let myChart = this.$echarts.init(document.getElementById('facultyCharts'))
                myChart.setOption({
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['工勤人员', '专职任教', '行政人员', '教辅人员'],
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
                                color: '#142852'
                            }
                        },
                        axisLabel: {
                            color: '#323232'
                        }
                    },
                    series: [
                        {
                            name: '工勤人员',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 25,
                            data: [320, 302, 301, 334, 390]
                        },
                        {
                            name: '专职任教',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 25,
                            data: [120, 132, 101, 134, 90]
                        },
                        {
                            name: '行政人员',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 25,
                            data: [220, 182, 191, 234, 290]
                        },
                        {
                            name: '教辅人员',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 25,
                            data: [150, 212, 201, 154, 190]
                        }
                    ]
                })
            },
            getStudentsCharts() {
                let myChart = this.$echarts.init(document.getElementById('studentsCharts'))
                myChart.setOption({
                    grid: {
                        right: 20,
                        left: 10,
                        top: 30,
                        bottom: 10,
                        containLabel: true
                    },
                    xAxis: {
                        type: 'category',
                        data: ['2014-2015', '2015-2016', '2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021']
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [{
                        data: [820, 932, 901, 934, 1290, 1330, 1320],
                        type: 'line',
                        smooth: true
                    }]
                })
            }
        }
    }
</script>

<style scoped>
    .school-overview{
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }
    .school-overview-box{
        width: 160px;
        padding: 14px 0;
        background-color: #000;
        border-radius: 8px;
        margin-right: 40px;
    }
    .school-overview-title{
        font-size: 20px;
        color: #fff;
        width: 100%;
        text-align: center;
    }
    .school-overview-val{
        font-size: 18px;
        color: #fff;
        margin-top: 5px;
        width: 100%;
        text-align: center;
        font-weight: bolder;
    }
    .school-overview-val span{
        font-weight: normal;
    }
    .school-synopsis{
        width: 100%;
        margin-top: 30px;
    }
    .school-name{
        font-size: 24px;
        font-weight: bolder;
    }
    .school-text{
        margin-top: 15px;
        font-size: 14px;
        line-height: 20px;
    }
    .school-text p{
        font-size: 14px;
        line-height: 20px;
    }
    .school-text img{
        width: 80%;
        display: block;
        margin: 10px 0;
    }
    #studentsCharts,
    #facultyCharts,
    #bookCharts,
    #shiShengCharts{
        width: 100%;
        height: 100%;
    }
</style>
