<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>学校舆情信息量</span>
            </div>
            <div class="school-overview">
                <div class="school-overview-box" style="background-image: linear-gradient(to bottom right, #eda472 , #e6762b);">
                    <div class="school-overview-title">累计监控总量</div>
                    <div class="school-overview-val">{{ overview.ljjkzl }}<span>人</span></div>
                </div>
                <div class="school-overview-box" style="background-image: linear-gradient(to bottom right, #8ea8d8 , #233d6d);">
                    <div class="school-overview-title">今日监控总量</div>
                    <div class="school-overview-val">{{ overview.jrjkzl }}<span>人</span></div>
                </div>
                <div class="school-overview-box" style="background-image: linear-gradient(to bottom right, #a2a2a2 , #585858);">
                    <div class="school-overview-title">敏感信息总量</div>
                    <div class="school-overview-val">{{ overview.mgxxzl }}<span>本</span></div>
                </div>
                <div class="school-overview-box" style="background-image: linear-gradient(to bottom right, #f8d15b , #896700);">
                    <div class="school-overview-title">信息源总量</div>
                    <div class="school-overview-val">{{ overview.xxyzl }}<span>㎡</span></div>
                </div>
            </div>
        </el-card>
        <div class="current-half-box school-overview-card">
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>学校舆情信息来源</span>
                </div>
                <div  class="current-half-height">
                    <div id="sourcesCharts"></div>
                </div>
            </el-card>
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>学校舆情热门词云</span>
                </div>
                <div  class="current-half-height">
                    <word-cloud-chart v-if="labelList.length" :data="labelList" width="100%" height="100%" @callback="wordCallback" />
                </div>
            </el-card>
        </div>
        <el-card class="current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>学校网站影响力</span>
            </div>
            <div class="grade-num-box">
                <div id="effectChart"></div>
            </div>
        </el-card>
    </div>
</template>

<script>
    import WordCloudChart from "@/components/word-cloud-chart";

    export default {
        name: "index",
        data() {
            return {
                overview: {
                    ljjkzl: '',
                    jrjkzl: '',
                    mgxxzl: '',
                    xxyzl: ''
                },
                labelList: []
            }
        },
        components: {
            WordCloudChart
        },
        mounted() {
            this.init();
        },
        methods: {
            init() {
                this.getLabelList();
                this.getSourcesCharts();
                this.getEffectChart();
            },
            getEffectChart() {
                let myChart = this.$echarts.init(document.getElementById('effectChart'))
                myChart.setOption({
                    title: {
                        text: '学校网站近5年影响力变化',
                    },
                    grid: {
                        right: 20,
                        left: 10,
                        top: 50,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['学校网站规模', '学校网站被连接数量', '学校网站显示度', '学校网站内容丰富度'],
                        textStyle: {
                            color: '#323232'
                        }
                    },
                    xAxis: {
                        type: 'category',
                        // boundaryGap: false,
                        data: ['2017', '2018', '2019', '2020', '2021'],
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
                            name: '学校网站规模',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [565, 611, 632, 621, 599]
                        },{
                            name: '学校网站被连接数量',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [123, 214, 145, 123, 214]
                        },{
                            name: '学校网站显示度',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [252, 125, 23, 425, 234]
                        },{
                            name: '学校网站内容丰富度',
                            type: 'bar',
                            // stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [166, 79, 234, 52, 111]
                        }
                    ]
                })
            },
            getSourcesCharts() {
                let myChart = this.$echarts.init(document.getElementById('sourcesCharts'))
                myChart.setOption({
                    title: {
                        text: '学校舆情信息来源',
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
                            name: '学校舆情信息来源',
                            type: 'pie',
                            top: 10,
                            right: 260,
                            radius: ['40%', '60%'],
                            avoidLabelOverlap: false,
                            data: [
                                {value: 134, name: '微信公众号',itemStyle: {color: '#13acb5'}},
                                {value: 421, name: '新闻网站',itemStyle: {color: '#60a8ff'}},
                                {value: 213, name: '论坛',itemStyle: {color: '#e8d83b'}},
                                {value: 123, name: '微博',itemStyle: {color: '#e66b42'}},
                                {value: 24, name: '贴吧',itemStyle: {color: '#6ae665'}}
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
            getLabelList(Area_name) {
                // getAreaHotWord({ Area_name: Area_name || '' }).then(res => {
                //     // console.log(res)
                //     for(let i in res.data.date) {
                //         res.data.date[i].value = res.data.date[i].value * 10
                //     }
                //     this.labelList = res.data.date;
                //
                // })
                this.labelList = [{name: '毛泽东思想', value: 2},
                    {name: '邓小平理论', value: 3},
                    {name: '三会一课', value: 4},
                    {name: '驻村工作队', value: 2},
                    {name: '党务公开', value: 2},
                    {name: '习近平系列讲话', value: 3},
                    {name: '志愿服务', value: 5},
                    {name: '支部规范化', value: 4},
                    {name: '毛泽东思想', value: 2},
                    {name: '邓小平理论', value: 3},
                    {name: '三会一课', value: 4},
                    {name: '驻村工作队', value: 1},
                    {name: '党务公开', value: 3}];
            },
            wordCallback() {

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
    .school-overview-card{
        margin-bottom: 30px;
    }
    #sourcesCharts,
    #effectChart{
        width: 100%;
        height: 100%;
    }
    .grade-num-box{
        width: 100%;
        height: 400px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
</style>
