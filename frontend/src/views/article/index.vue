<template>
    <el-container style="height: 100%">
        <el-header height="80px">
            <current-head :name="'教育文章详情'" :currentTime="currentTime"></current-head>
        </el-header>
        <el-main>
            <div class="map-box">
                <div id="container" style="width:100%; height:100%"></div>
            </div>
            <!--            <el-amap class="amap-box" :vid="'amap-vue'" style="width:500px; height:300px"></el-amap>-->
        </el-main>
    </el-container>
</template>

<script>
    import CurrentHead from '@/components/current-head'
    import '../../../node_modules/echarts/map/js/china.js'
    import 'echarts/extension/bmap/bmap.js'
    import { loadBMap } from '@/lib/map'

    export default {
        name: "index",
        components: {
            CurrentHead
        },
        data() {
            return {
                currentTime: ''
            };
        },
        created() {
            this.getNowTime()
        },
        mounted() {
            this.$nextTick(() => {
                loadBMap("qUqHTO6WiuGIKRaS7UDqFtl6HxbpDqdi").then(() => {
                    this.getMapData()
                })
            })
        },
        methods: {
            timestampToTime(data) {
                let yyyy = data.getFullYear()
                let MM = (data.getMonth() + 1).toString().padStart(2, '0')
                let dd = data.getDate().toString().padStart(2, '0')
                let h = data.getHours().toString().padStart(2, '0')
                let m = data.getMinutes().toString().padStart(2, '0')
                let s = data.getSeconds().toString().padStart(2, '0')
                return yyyy + '年' + MM + '月' + dd + '日 ' + h + ':' + m + ':' + s
            },
            getNowTime() {
                let aData = new Date();

                this.currentTime = this.timestampToTime(aData)
            },
            getData(point) {
                let A = point[0],
                    B = point[1],
                    n = 30,
                    arc = Math.PI / 4,
                    points = [];
                let R = this.getCircleRadio(A, B, arc);
                let Ori = this.getCircleOrigin(A, B, R)
                for (let i=0; i<n; i++) {
                    let angl = arc*i / n,
                        arc0 = Math.asin((A[0]-Ori[0])/R);
                    let x = Ori[0] + Math.sin(arc0 + angl)*R;
                    let y = Ori[1] + Math.cos(arc0 + angl)*R;
                    points.push([x, y]);
                }
                return points;
            },
            getCircleRadio(A, B, arc) {
                return Math.sqrt(Math.pow(B[0]-A[0], 2)+Math.pow(B[1]-A[1], 2)) / (2*Math.sin(arc/2));
            },
            getCircleOrigin(A, B, r) {
                let x0 = 0, y0 = 0;
                if (A[0] == B[0]) {
                    x0 = A[0] - Math.sqrt( r*r - Math.pow((B[1]-A[1]/2), 2));
                    y0 = (A[1] + B[1])/2;
                } else if (A[1] == B[1]) {
                    x0 = (A[0] + B[0])/2;
                    y0 = A[1] + Math.sqrt( r*r - Math.pow((B[0]-A[0]/2), 2));
                } else {
                    let M = [(A[0] + B[0])/2, (A[1] + B[1])/2],
                        k = (A[0]-B[0])/(B[1]-A[1]),
                        a = 1.0 + k * k,
                        b = -2 * M[0] - k * k * (A[0] + B[0]),
                        c = M[0] * M[0] + k * k * (A[0] + B[0]) * (A[0] + B[0]) / 4.0 - (r * r - ((M[0] - A[0]) * (M[0] - A[0]) + (M[1] - A[1]) * (M[1] - A[1])));
                    x0 = (-1.0 * b - Math.sqrt(b * b -4 * a * c)) / (2 * a);
                    y0 = k * x0 - k * M[0] + M[1];
                }
                return [x0, y0];
            },
            getMapData() {
                // let hStep = 300 / (data.length - 1);
                let busLines = [{
                    coords: this.getData([[116.4383, 40.1471], [120.5383, 23.1471]]),
                    lineStyle: {
                        normal: {
                            color: this.$echarts.color.modifyHSL('#5A94DF', Math.round(350))
                        }
                    }
                },
                    {
                        coords: this.getData([[116.4383, 40.1471], [114.5383, 25.1471]]),
                        lineStyle: {
                            normal: {
                                color: this.$echarts.color.modifyHSL('#5A94DF', Math.round(160))
                            }
                        }
                    },
                    {
                        coords: this.getData([[116.4383, 40.1471], [118.5383, 33.1471]]),
                        lineStyle: {
                            normal: {
                                color: this.$echarts.color.modifyHSL('#5A94DF', Math.round(140))
                            }
                        }
                    },
                    {
                        coords: this.getData([[116.4383, 40.1471], [123.5383, 28.1471]]),
                        lineStyle: {
                            normal: {
                                color: this.$echarts.color.modifyHSL('#5A94DF', Math.round(250))
                            }
                        }
                    }];
                let myChart = this.$echarts.init(document.getElementById('container')); //这里是为了获得容器所在位置
                myChart.setOption({
                    bmap: {
                        center: [102.802073,24.99007],
                        zoom: 12,
                        roam: true,
                        mapStyle: {
                            // style: 'midnight'
                            'styleJson': [
                                {
                                    'featureType': 'water',
                                    'elementType': 'all',
                                    'stylers': {
                                        'color': '#031628'
                                    }
                                },
                                {
                                    'featureType': 'land',
                                    'elementType': 'geometry',
                                    'stylers': {
                                        'color': '#000102'
                                    }
                                },
                                {
                                    'featureType': 'highway',
                                    'elementType': 'all',
                                    'stylers': {
                                        'visibility': 'off'
                                    }
                                },
                                {
                                    'featureType': 'arterial',
                                    'elementType': 'geometry.fill',
                                    'stylers': {
                                        'color': '#000000'
                                    }
                                },
                                {
                                    'featureType': 'arterial',
                                    'elementType': 'geometry.stroke',
                                    'stylers': {
                                        'color': '#0b3d51'
                                    }
                                },
                                {
                                    'featureType': 'local',
                                    'elementType': 'geometry',
                                    'stylers': {
                                        'color': '#000000'
                                    }
                                },
                                {
                                    'featureType': 'railway',
                                    'elementType': 'geometry.fill',
                                    'stylers': {
                                        'color': '#000000'
                                    }
                                },
                                {
                                    'featureType': 'railway',
                                    'elementType': 'geometry.stroke',
                                    'stylers': {
                                        'color': '#08304b'
                                    }
                                },
                                {
                                    'featureType': 'subway',
                                    'elementType': 'geometry',
                                    'stylers': {
                                        'lightness': -70
                                    }
                                },
                                {
                                    'featureType': 'building',
                                    'elementType': 'geometry.fill',
                                    'stylers': {
                                        'color': '#000000'
                                    }
                                },
                                {
                                    'featureType': 'all',
                                    'elementType': 'labels.text.fill',
                                    'stylers': {
                                        'color': '#857f7f'
                                    }
                                },
                                {
                                    'featureType': 'all',
                                    'elementType': 'labels.text.stroke',
                                    'stylers': {
                                        'color': '#000000'
                                    }
                                },
                                {
                                    'featureType': 'building',
                                    'elementType': 'geometry',
                                    'stylers': {
                                        'color': '#022338'
                                    }
                                },
                                {
                                    'featureType': 'green',
                                    'elementType': 'geometry',
                                    'stylers': {
                                        'color': '#062032'
                                    }
                                },
                                {
                                    'featureType': 'boundary',
                                    'elementType': 'all',
                                    'stylers': {
                                        'color': '#465b6c'
                                    }
                                },
                                {
                                    'featureType': 'manmade',
                                    'elementType': 'all',
                                    'stylers': {
                                        'color': '#022338'
                                    }
                                },
                                {
                                    'featureType': 'label',
                                    'elementType': 'all',
                                    'stylers': {
                                        'visibility': 'off'
                                    }
                                }
                            ]
                        }
                    },
                    /*geo: { // 这个是重点配置区
                        map: 'china', // 表示中国地图
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
                    },*/
                    series: [{
                        type: 'lines',
                        coordinateSystem: 'bmap',
                        polyline: true,
                        data: busLines,
                        silent: true,
                        lineStyle: {
                            normal: {
                                // color: '#c23531',
                                // color: 'rgb(200, 35, 45)',
                                opacity: 0.3,

                                width: 2
                            }
                        },
                        progressiveThreshold: 500,
                        progressive: 200
                    }, {
                        type: 'lines',
                        coordinateSystem: 'bmap',
                        polyline: true,
                        data: busLines,
                        lineStyle: {
                            normal: {
                                width: 0
                            }
                        },
                        effect: {
                            constantSpeed: 50,
                            show: true,
                            trailLength: 0.5,
                            symbolSize: 2
                        },
                        zlevel: 1
                    }]
                });
            },

    /*$.get('data/asset/data/lines-bus.json', function(data) {
        var hStep = 300 / (data.length - 1);
        var busLines = [{
            coords: getData([[116.4383, 40.1471], [120.5383, 23.1471]]),
            lineStyle: {
                normal: {
                    color: echarts.color.modifyHSL('#5A94DF', Math.round(350))
                }
            }
        },
            {
                coords: getData([[116.4383, 40.1471], [114.5383, 25.1471]]),
                lineStyle: {
                    normal: {
                        color: echarts.color.modifyHSL('#5A94DF', Math.round(160))
                    }
                }
            },
            {
                coords: getData([[116.4383, 40.1471], [118.5383, 33.1471]]),
                lineStyle: {
                    normal: {
                        color: echarts.color.modifyHSL('#5A94DF', Math.round(140))
                    }
                }
            },
            {
                coords: getData([[116.4383, 40.1471], [123.5383, 28.1471]]),
                lineStyle: {
                    normal: {
                        color: echarts.color.modifyHSL('#5A94DF', Math.round(250))
                    }
                }
            }];
        myChart.setOption(option = {
            bmap: {
                center: [116.46, 29.92],
                zoom: 6,
                roam: true,
                mapStyle: {
                    'styleJson': [
                        {
                            'featureType': 'water',
                            'elementType': 'all',
                            'stylers': {
                                'color': '#031628'
                            }
                        },
                        {
                            'featureType': 'land',
                            'elementType': 'geometry',
                            'stylers': {
                                'color': '#000102'
                            }
                        },
                        {
                            'featureType': 'highway',
                            'elementType': 'all',
                            'stylers': {
                                'visibility': 'off'
                            }
                        },
                        {
                            'featureType': 'arterial',
                            'elementType': 'geometry.fill',
                            'stylers': {
                                'color': '#000000'
                            }
                        },
                        {
                            'featureType': 'arterial',
                            'elementType': 'geometry.stroke',
                            'stylers': {
                                'color': '#0b3d51'
                            }
                        },
                        {
                            'featureType': 'local',
                            'elementType': 'geometry',
                            'stylers': {
                                'color': '#000000'
                            }
                        },
                        {
                            'featureType': 'railway',
                            'elementType': 'geometry.fill',
                            'stylers': {
                                'color': '#000000'
                            }
                        },
                        {
                            'featureType': 'railway',
                            'elementType': 'geometry.stroke',
                            'stylers': {
                                'color': '#08304b'
                            }
                        },
                        {
                            'featureType': 'subway',
                            'elementType': 'geometry',
                            'stylers': {
                                'lightness': -70
                            }
                        },
                        {
                            'featureType': 'building',
                            'elementType': 'geometry.fill',
                            'stylers': {
                                'color': '#000000'
                            }
                        },
                        {
                            'featureType': 'all',
                            'elementType': 'labels.text.fill',
                            'stylers': {
                                'color': '#857f7f'
                            }
                        },
                        {
                            'featureType': 'all',
                            'elementType': 'labels.text.stroke',
                            'stylers': {
                                'color': '#000000'
                            }
                        },
                        {
                            'featureType': 'building',
                            'elementType': 'geometry',
                            'stylers': {
                                'color': '#022338'
                            }
                        },
                        {
                            'featureType': 'green',
                            'elementType': 'geometry',
                            'stylers': {
                                'color': '#062032'
                            }
                        },
                        {
                            'featureType': 'boundary',
                            'elementType': 'all',
                            'stylers': {
                                'color': '#465b6c'
                            }
                        },
                        {
                            'featureType': 'manmade',
                            'elementType': 'all',
                            'stylers': {
                                'color': '#022338'
                            }
                        },
                        {
                            'featureType': 'label',
                            'elementType': 'all',
                            'stylers': {
                                'visibility': 'off'
                            }
                        }
                    ]
                }
            },
            series: [{
                type: 'lines',
                coordinateSystem: 'bmap',
                polyline: true,
                data: busLines,
                silent: true,
                lineStyle: {
                    normal: {
                        // color: '#c23531',
                        // color: 'rgb(200, 35, 45)',
                        opacity: 0.3,

                        width: 2
                    }
                },
                progressiveThreshold: 500,
                progressive: 200
            }, {
                type: 'lines',
                coordinateSystem: 'bmap',
                polyline: true,
                data: busLines,
                lineStyle: {
                    normal: {
                        width: 0
                    }
                },
                effect: {
                    constantSpeed: 50,
                    show: true,
                    trailLength: 0.5,
                    symbolSize: 2
                },
                zlevel: 1
            }]
        });
    });*/
        }
    }
</script>

<style scoped>
    /deep/ .el-header, .el-footer {
        text-align: center;
        padding: 0;
    }

    /deep/ .el-main {
        background-color: #0e0f3c;
        color: #333;
        text-align: center;
        height: calc(100% - 120px);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .map-box{
        width: 600px;
        height: 600px;
        padding: 10px;
        border: 1px solid #1e2252;
    }
</style>
