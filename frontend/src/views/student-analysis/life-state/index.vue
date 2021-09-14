<template>
    <div>
        <div class="current-half-box school-overview-card">
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>获得助学金概况</span>
                </div>
                <div  class="current-half-height">
                    <el-select v-model="schoolYear" placeholder="请选择学年" style="margin-bottom: 10px">
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
                    <div id="grantCharts"></div>
                </div>
            </el-card>
            <el-card class="current-card-box" shadow="always">
                <div slot="header" class="clearfix current-card-head">
                    <span>贷款概况</span>
                </div>
                <div  class="current-half-height">
                    <div id="loanCharts"></div>
                </div>
            </el-card>
        </div>
        <el-card class="current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>一卡通消费情况</span>
            </div>
            <div class="grade-num-box">
                <div id="cardChart"></div>
            </div>
        </el-card>
    </div>
</template>

<script>
    export default {
        name: "index",
        data() {
            return {
                schoolYear: '0',
                schoolYearOptions: [
                    {
                        label: '2020-2021学年',
                        value: '0'
                    },{
                        label: '2019-2020学年',
                        value: '1'
                    },{
                        label: '2018-2019学年',
                        value: '2'
                    }
                ]
            }
        },
        mounted() {
            this.init()
        },
        methods:{
            init() {
                this.getGrantCharts();
                this.getLoanCharts();
                this.getCardChart();
            },
            getCardChart() {
                let myChart = this.$echarts.init(document.getElementById('cardChart'))
                myChart.setOption({
                    title: {
                        text: '一卡通消费近6学期变化趋势'
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
                        // axisLabel: { interval: 0, rotate: 30 },
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '一卡通消费近6学期变化趋势',
                            type: 'line',
                            // stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        }
                    ]
                })
            },
            getLoanCharts() {
                let myChart = this.$echarts.init(document.getElementById('loanCharts'))
                myChart.setOption({
                    title: {
                        text: '贷款金额近5学年变化趋势',
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
                        data: ['2016-2017学年', '2017-2018学年', '2018-2019学年', '2019-2020学年', '2020-2021学年'],
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
                            name: '贷款金额近5学年变化趋势',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 35,
                            data: [89, 71, 79, 76 , 69]
                        }
                    ]
                })
            },
            getGrantCharts() {
                let myChart = this.$echarts.init(document.getElementById('grantCharts'))
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
            }
        }
    }
</script>

<style scoped>
    .school-overview-card{
        margin-bottom: 30px;
    }
    #loanCharts,
    #cardChart{
        width: 100%;
        height: 100%;
    }
    #grantCharts{
        width: 100%;
        height: calc(100% - 50px);
    }
    .grade-num-box{
        width: 100%;
        height: 400px;
    }
</style>
