<template>
    <div class="current-main-box">
        <el-form :inline="true" :model="searchFrom" class="demo-form-inline">
            <el-form-item label="学年">
                <el-select v-model="searchFrom.schoolYear" placeholder="活动学年">
                    <el-option label="全部" value=""></el-option>
                    <el-option label="2021学年" value="shanghai"></el-option>
                    <el-option label="2022学年" value="beijing"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="年级">
                <el-select v-model="searchFrom.grade" placeholder="请选择年级">
                    <el-option label="全部" value=""></el-option>
                    <el-option label="高一" value="shanghai"></el-option>
                    <el-option label="高二" value="beijing"></el-option>
                    <el-option label="高三" value="beijing"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="班级">
                <el-select v-model="searchFrom.class" placeholder="请选择班级">
                    <el-option label="全部" value=""></el-option>
                    <el-option label="一班" value="shanghai"></el-option>
                    <el-option label="二班" value="beijing"></el-option>
                    <el-option label="三班" value="beijing"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit">查询</el-button>
            </el-form-item>
        </el-form>
        <div class="students-overview-box">
            <div>
                <div class="students-overview-title">报到人数（人）</div>
                <div class="students-overview-val">{{ studentsOverview.registerNo }}</div>
            </div>
            <div>
                <div class="students-overview-title">全校占比</div>
                <div class="students-overview-val">{{ studentsOverview.proportion }}</div>
            </div>
            <div>
                <div class="students-overview-title">男女比例</div>
                <div class="students-overview-val">{{ studentsOverview.genderRatio }}</div>
            </div>
        </div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>学生生源地</span>
            </div>
            <div class="origin-place-box">
                <div class="students-source-map">
                    <div id="studentsSource"></div>
                </div>
                <div id="originPlaceCharts"></div>
            </div>
        </el-card>
        <div class="current-half-box marginTop20">
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>生源类型比例</span>
                </div>
                <div  class="current-half-height">
                    <div id="originPlaceRatioCharts"></div>
                </div>
            </el-card>
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>招生情况</span>
                </div>
                <div  class="current-half-height">
                    <div id="recruitStudentsCharts"></div>
                </div>
            </el-card>
        </div>
        <div class="current-half-box marginTop20">
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>招考平均成绩</span>
                </div>
                <div  class="current-half-height">
                    <div id="recruitmentResultsCharts"></div>
                </div>
            </el-card>
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>家庭背景</span>
                </div>
                <div  class="current-half-height">
                    <div id="familyCharts"></div>
                </div>
            </el-card>
        </div>
        <div class="current-half-box marginTop20">
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>心理素质评分</span>
                </div>
                <div  class="current-half-height">
                    <div id="psychologicalCharts"></div>
                </div>
            </el-card>
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>体能测试</span>
                </div>
                <div  class="current-half-height">
                    <div id="physicalFitnessCharts"></div>
                </div>
            </el-card>
        </div>
    </div>
</template>

<script>
    import 'echarts/map/js/china.js'
    import kunming from '@/lib/kunming.json'

    export default {
        name: "index",
        data() {
            return {
                searchFrom: {
                    schoolYear: '',
                    grade: '',
                    class: ''
                },
                studentsOverview: {
                    registerNo: 600,
                    proportion: '100%',
                    genderRatio: '2:1'
                }
            }
        },
        mounted() {
            this.init()
        },
        methods: {
            init() {
                this.getMapData();
                this.getOriginPlaceCharts();
                this.getOriginPlaceRatioCharts();
                this.getRecruitStudentsCharts();
                this.getRecruitmentResultsCharts();
                this.getFamilyCharts();
                this.getPsychologicalCharts();
                this.getPhysicalFitnessCharts();
            },
            onSubmit() {

            },
            getPhysicalFitnessCharts() {
                let myChart = this.$echarts.init(document.getElementById('physicalFitnessCharts'));
                myChart.setOption({
                    tooltip: {
                        trigger: 'item',
                        transitionDuration: 0,
                    },
                    legend: {
                        type: 'scroll',
                        orient: 'vertical',
                        top: 'center',
                        right: 40,
                        textStyle: {
                            color: '#323232',
                            fontSize: 12
                        },
                    },
                    series: [
                        {
                            name: '家庭背景',
                            type: 'pie',
                            top: 10,
                            right: 100,
                            radius: ['40%', '70%'],
                            avoidLabelOverlap: false,
                            labelLine: {
                                show: false
                            },
                            label: {
                                show: false,
                                position: 'center'
                            },
                            data: [
                                {value: 64, name: '优',itemStyle: {color: '#13acb5'}},
                                {value: 123, name: '良',itemStyle: {color: '#60a8ff'}},
                                {value: 12, name: '中',itemStyle: {color: '#e8d83b'}},
                                {value: 23, name: '差',itemStyle: {color: '#e6823f'}},
                            ]
                        }
                    ]
                })
            },
            getPsychologicalCharts() {
                let myChart = this.$echarts.init(document.getElementById('psychologicalCharts'));
                myChart.setOption({
                    tooltip: {
                        trigger: 'item',
                        transitionDuration: 0,
                    },
                    legend: {
                        type: 'scroll',
                        orient: 'vertical',
                        top: 'center',
                        right: 40,
                        textStyle: {
                            color: '#323232',
                            fontSize: 12
                        },
                    },
                    series: [
                        {
                            name: '心理测试评分',
                            type: 'pie',
                            top: 10,
                            right: 100,
                            radius: ['40%', '70%'],
                            avoidLabelOverlap: false,
                            labelLine: {
                                show: false
                            },
                            label: {
                                show: false,
                                position: 'center'
                            },
                            data: [
                                {value: 64, name: '60分以下',itemStyle: {color: '#13acb5'}},
                                {value: 123, name: '60-70分',itemStyle: {color: '#60a8ff'}},
                                {value: 12, name: '70-80分',itemStyle: {color: '#e8d83b'}},
                                {value: 23, name: '80-90分',itemStyle: {color: '#e6823f'}},
                                {value: 23, name: '90-100分',itemStyle: {color: '#e62b2f'}},
                            ]
                        }
                    ]
                })
            },
            getFamilyCharts() {
                let myChart = this.$echarts.init(document.getElementById('familyCharts'));
                myChart.setOption({
                    tooltip: {
                        trigger: 'item',
                        transitionDuration: 0,
                    },
                    legend: {
                        type: 'scroll',
                        orient: 'vertical',
                        top: 'center',
                        right: 40,
                        textStyle: {
                            color: '#323232',
                            fontSize: 12
                        },
                    },
                    series: [
                        {
                            name: '家庭背景',
                            type: 'pie',
                            top: 10,
                            right: 100,
                            radius: ['40%', '70%'],
                            avoidLabelOverlap: false,
                            labelLine: {
                                show: false
                            },
                            label: {
                                show: false,
                                position: 'center'
                            },
                            data: [
                                {value: 64, name: '非经济困难',itemStyle: {color: '#13acb5'}},
                                {value: 123, name: '一般经济困难',itemStyle: {color: '#60a8ff'}},
                                {value: 12, name: '特困',itemStyle: {color: '#e8d83b'}},
                                {value: 23, name: '建档立卡户',itemStyle: {color: '#e6823f'}},
                            ]
                        }
                    ]
                })
            },
            getRecruitmentResultsCharts() {
                let myChart = this.$echarts.init(document.getElementById('recruitmentResultsCharts'));
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
                        data: ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
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
            },
            getRecruitStudentsCharts() {
                let myChart = this.$echarts.init(document.getElementById('recruitStudentsCharts'));
                myChart.setOption({
                    tooltip: {
                        trigger: 'item',
                        transitionDuration: 0,
                    },
                    legend: {
                        type: 'scroll',
                        orient: 'vertical',
                        top: 'center',
                        right: 40,
                        textStyle: {
                            color: '#323232',
                            fontSize: 12
                        },
                    },
                    series: [
                        {
                            name: '招生情况',
                            type: 'pie',
                            top: 10,
                            right: 100,
                            radius: ['40%', '70%'],
                            avoidLabelOverlap: false,
                            labelLine: {
                                show: false
                            },
                            label: {
                                show: false,
                                position: 'center'
                            },
                            data: [
                                {value: 64, name: '计划招生数',itemStyle: {color: '#13acb5'}},
                                {value: 123, name: '实际招生数',itemStyle: {color: '#60a8ff'}},
                                {value: 12, name: '实际报到数',itemStyle: {color: '#e8d83b'}},
                            ]
                        }
                    ]
                })
            },
            getOriginPlaceRatioCharts() {
                let myChart = this.$echarts.init(document.getElementById('originPlaceRatioCharts'));
                myChart.setOption({
                    tooltip: {
                        trigger: 'item',
                        transitionDuration: 0,
                    },
                    legend: {
                        type: 'scroll',
                        orient: 'vertical',
                        top: 'center',
                        right: 40,
                        textStyle: {
                            color: '#323232',
                            fontSize: 12
                        },
                    },
                    series: [
                        {
                            name: '生源类型',
                            type: 'pie',
                            top: 10,
                            right: 100,
                            radius: ['40%', '70%'],
                            avoidLabelOverlap: false,
                            labelLine: {
                                show: false
                            },
                            label: {
                                show: false,
                                position: 'center'
                            },
                            data: [
                                {value: 64, name: '普通招考',itemStyle: {color: '#13acb5'}},
                                {value: 123, name: '自主招考',itemStyle: {color: '#60a8ff'}},
                                {value: 12, name: '特长类',itemStyle: {color: '#e8d83b'}},
                                {value: 23, name: '特殊',itemStyle: {color: '#e6823f'}},
                            ]
                        }
                    ]
                })
            },
            getOriginPlaceCharts() {
                let myChart = this.$echarts.init(document.getElementById('originPlaceCharts'));
                myChart.setOption({
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    yAxis: {
                        type: 'category',
                        // boundaryGap: false,
                        data: ['盘龙区', '五华区', '官渡区', '西山区', '安宁市', '晋宁市', '呈贡区', '宜良县', '石林县', '嵩明县', '富民县', '寻甸县', '禄劝县', '东川区'],
                        axisLabel: {
                            color: '#323232'
                        }
                    },
                    xAxis: {
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
                            name: '生源人数',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 20,
                            data: [320, 302, 301, 334, 390,320, 302, 301, 334, 390,320, 302, 301, 334]
                        }
                    ]
                })
            },
            getMapData() {
                let myChart = this.$echarts.init(document.getElementById('studentsSource')); //这里是为了获得容器所在位置
                // window.onresize = myChart.resize;
                this.$echarts.registerMap("kunming",kunming)
                myChart.setOption({
                    backgroundColor: "#fff",
                    tooltip: {}, // 鼠标移到图里面的浮动提示框
                    dataRange: {
                        show: false,
                        min: 0,
                        max: 100,
                        text: ['High', 'Low'],
                        realtime: true,
                        calculable: true,
                        color: ['orangered', 'yellow', 'lightskyblue']
                    },
                    geo: { // 这个是重点配置区
                        map: 'kunming', // 表示中国地图
                        roam: true,
                        label: {
                            normal: {
                                show: true, // 是否显示对应地名
                                textStyle: {
                                    color: 'rgba(0,0,0,0.4)'
                                }
                            }
                        },
                        itemStyle: {
                            normal: {
                                borderColor: 'rgba(0, 0, 0, 0.2)'
                            },
                            emphasis: {
                                areaColor: null,
                                shadowOffsetX: 0,
                                shadowOffsetY: 0,
                                shadowBlur: 20,
                                borderWidth: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    },
                    series: [{
                        type: 'scatter',
                        coordinateSystem: 'geo' // 对应上方配置
                    },
                        {
                            name: '舆情数量', // 浮动框的标题
                            type: 'map',
                            geoIndex: 0,
                            data: [
                                {name: '昆明市', value: 201}
                            ]
                        }
                    ]
                })
            },
        }
    }
</script>

<style scoped>
    .students-source-map{
        width: 700px;
        height: 600px;
    }
    #studentsSource{
        width: 100%;
        height: 100%;
    }
    .origin-place-box{
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    #originPlaceCharts{
        width: 850px;
        height: 600px;
    }
    #originPlaceRatioCharts,
    #recruitStudentsCharts,
    #recruitmentResultsCharts,
    #familyCharts,
    #psychologicalCharts,
    #physicalFitnessCharts
    {
        width: 100%;
        height: 100%;
    }
    .students-overview-box{
        width: 100%;
        background: #fff;
        height: 120px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
        margin: 10px 0 30px;
    }
    .students-overview-box>div{
        width: 33.3333%;
        text-align: center;
    }
    .students-overview-box>div:nth-child(2){
        border-left: 1px solid #eee;
        border-right: 1px solid #eee;
    }
</style>
