<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>行为习惯</span>
            </div>
            <div class="grade-num-box">
                <div id="behaviorHabitChart"></div>
            </div>
        </el-card>
        <el-card class="current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>日均上网时长</span>
            </div>
            <div class="grade-num-box">
                <div id="internetChart"></div>
            </div>
        </el-card>
    </div>
</template>

<script>
    export default {
        name: "index",
        data() {
            return {

            }
        },
        mounted() {
            this.init()
        },
        methods: {
            init() {
                this.getBehaviorHabitChart();
                this.getInternetChart()
            },
            getInternetChart() {
                let myChart = this.$echarts.init(document.getElementById('internetChart'))
                myChart.setOption({
                    title: {
                        text: '日均上网时长近6个月变化趋势'
                    },
                    // legend: {
                    //     data: ['夜不归宿次数', '宿舍卫生通报次数']
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
                        data: ['2021年3月', '2021年4月', '2021年5月', '2021年6月', '2021年7月', '2021年8月'],
                        // axisLabel: { interval: 0, rotate: 30 },
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '日均上网时长近6个月变化趋势',
                            type: 'line',
                            // stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        }
                    ]
                })
            },
            getBehaviorHabitChart() {
                let myChart = this.$echarts.init(document.getElementById('behaviorHabitChart'))
                myChart.setOption({
                    title: {
                        text: '行为习惯近6个月变化趋势'
                    },
                    legend: {
                        data: ['夜不归宿次数', '宿舍卫生通报次数']
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
                        data: ['2021年3月', '2021年4月', '2021年5月', '2021年6月', '2021年7月', '2021年8月'],
                        // axisLabel: { interval: 0, rotate: 30 },
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '夜不归宿次数',
                            type: 'line',
                            // stack: '总量',
                            data: [120, 132, 101, 134, 90, 230]
                        },{
                            name: '宿舍卫生通报次数',
                            type: 'line',
                            // stack: '总量',
                            data: [142, 89, 137, 99, 111, 201]
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
    .grade-num-box{
        width: 100%;
        height: 400px;
    }
    #behaviorHabitChart,
    #internetChart{
        width: 100%;
        height: 100%;
    }
</style>
