<template>
    <div>
        <div class="map-box">
            <center-map></center-map>
        </div>
        <div class="industry-voice-box">
            <div class="courseOverview">
                <div class="current-title finger" @click="goDetail('/detailsHome/disciplineAnalysis/disciplineOverview', 'disciplineOverview')">
                    课程概况
                </div>
                <div class="current-content">
                    <div class="surveyBox1" style="border-bottom: 1px dashed #1e2252">
                        <div class="surveyBox2" style="border-right: 1px dashed #1e2252">
                            <span class="iconfont icon-shu1 surveyFont" style="color: #d7c300"></span>
                            <div class="surveyBox3">
                                <div class="surveyTitle">课程总数</div>
                                <div class="surveyVal">
                                    {{ courseOverview.total }}
                                    <span>门</span>
                                </div>
                            </div>
                        </div>
                        <div class="surveyBox2">
                            <span class="iconfont icon-baogaogongdan surveyFont" style="color: #5ad9fa"></span>
                            <div class="surveyBox3">
                                <div class="surveyTitle">课程种类</div>
                                <div class="surveyVal">
                                    {{ courseOverview.courseType }}
                                    <span>类</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="surveyBox1">
                        <div class="surveyBox2" style="border-right: 1px dashed #1e2252">
                            <span class="iconfont icon-chengxinhezuowoshou surveyFont" style="color: #00c3c3"></span>
                            <div class="surveyBox3">
                                <div class="surveyTitle">在线课程资源</div>
                                <div class="surveyVal">
                                    {{ courseOverview.onLineCourse }}
                                    <span>门</span>
                                </div>
                            </div>
                        </div>
                        <div class="surveyBox2">
                            <span class="iconfont icon-icon_huabanfuben surveyFont" style="color: #60a8ff"></span>
                            <div class="surveyBox3">
                                <div class="surveyTitle">老师公开课数</div>
                                <div class="surveyVal">
                                    {{ courseOverview.openClass }}
                                    <span>门</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="studentProfile">
                <div class="current-title finger" @click="goDetail('/detailsHome/studentAnalysis/studentInformation', 'studentInformation')">
                    学生概况
                </div>
                <div class="current-content">
                    <div class="surveyBox1" style="border-bottom: 1px dashed #1e2252">
                        <div class="surveyBox2" style="border-right: 1px dashed #1e2252">
                            <span class="iconfont icon-baogao surveyFont" style="color: #d7c300"></span>
                            <div class="surveyBox3">
                                <div class="surveyTitle">本科升学率</div>
                                <div class="surveyVal">
                                    {{ studentProfile.enrollmentRate }}
                                    <span>%</span>
                                </div>
                            </div>
                        </div>
                        <div class="surveyBox2">
                            <span class="iconfont icon-huaxueqimin surveyFont" style="color: #5ad9fa"></span>
                            <div class="surveyBox3">
                                <div class="surveyTitle">省级三好学生</div>
                                <div class="surveyVal">
                                    {{ studentProfile.threeGoodStudents }}
                                    <span>个</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="surveyBox1">
                        <div class="surveyBox2" style="border-right: 1px dashed #1e2252">
                            <span class="iconfont icon-jiangbei surveyFont" style="color: #00c3c3"></span>
                            <div class="surveyBox3">
                                <div class="surveyTitle">重点大学人数</div>
                                <div class="surveyVal">
                                    {{ studentProfile.keyUniversities }}
                                    <span>个</span>
                                </div>
                            </div>
                        </div>
                        <div class="surveyBox2">
                            <span class="iconfont icon-fuqian surveyFont" style="color: #60a8ff"></span>
                            <div class="surveyBox3">
                                <div class="surveyTitle">校贫困生数量</div>
                                <div class="surveyVal">
                                    {{ studentProfile.poorNum }}
                                    <span>个</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import '../../../../node_modules/echarts/map/js/china.js'
    import centerMap from './center-map'
    import { getNewsNum, getNewsMap, getAreaNewsIndustry } from '@/api/Home'
    import { mapGetters, mapMutations } from "vuex";

    export default {
        name: "container-center",
        data() {
            return {
                courseOverview: {
                    total: '705',
                    courseType: '58',
                    onLineCourse: '106',
                    openClass: '231'
                },
                studentProfile: {
                    enrollmentRate: '98',
                    threeGoodStudents: '21',
                    keyUniversities: '65',
                    poorNum: '41'
                }
            };
        },
        components: {
            centerMap
        },
        computed: {
            ...mapGetters(["homeAreaName"]),
        },
        watch: {
            homeAreaName() {

            }
        },
        mounted () {
            this.init();
        },
        methods: {
            ...mapMutations(["changeHomeAreaName"]),
            // async
            init() {

            },
            goDetail(path,name) {
                window.localStorage.setItem('activeAside', name)
                this.$router.push({
                    path: path,
                })
            }
        }
    }
</script>

<style scoped>
    .current-title:before{
        content: '';
        display: inline-block;
        width: 4px;
        height: 18px;
        background-color: #e6c23c;
        margin-right: 8px;
    }
    .current-title{
        height: 42px;
        display: flex;
        color: #fff;
        align-items: center;
        justify-content: flex-start;
        width: 100%;
        /*margin-bottom: 10px;*/
        padding: 8px 15px;
        background-image: linear-gradient(to right, rgba(20,107,202,1) , rgba(20,107,202,0));
        /*#146bca*/
    }
    .current-content{
        width: 100%;
        height: calc(100% - 42px);
        border: 1px solid #1e2252;
        border-top: none;
        padding: 10px;
    }
    .map-box{
        width: 100%;
        height: calc(100% - ((100% - 30px) / 3) - 15px);
    }
    .industry-voice-box{
        width: 100%;
        margin-top: 15px;
        height: calc((100% - 30px) / 3);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .courseOverview,
    .studentProfile{
        width: calc((100% - 15px) / 2);
        height: 100%;
    }
    .surveyBox1{
        padding: 15px 10px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .surveyBox2{
        padding: 10px;
        width: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .surveyBox3{
        text-align: left;
    }
    .surveyTitle{
        font-size: 12px;
        color: #146BCA;
    }
    .surveyVal{
        font-size: 24px;
        font-weight: bolder;
        color: #fff;
        margin-top: 4px;
    }
    .surveyVal span{
        font-size: 12px;
        color: #fff;
    }
    .surveyFont{
        font-size: 50px;
        margin-right: 10px;
    }
</style>
