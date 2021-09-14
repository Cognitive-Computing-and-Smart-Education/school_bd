<template>
    <div>
        <el-tabs v-model="activeName" @tab-click="handleClick" type="card">
            <el-tab-pane v-for="(item,index) in tabList" :label="item.label" :name="item.path" :key="`tabList-${item.path}`"></el-tab-pane>
        </el-tabs>
        <router-view></router-view>
    </div>
</template>

<script>
    import Information from './content/information'
    import LawLife from './content/lawLife'
    import Consumption from './content/consumption'
    import SocialContact from './content/social-contact'
    import Library from './content/library'
    import Study from './content/study'
    import Whereabouts from './content/whereabouts'

    export default {
        name: "detail",
        components: {
            Information,
            LawLife,
            Consumption,
            SocialContact,
            Library,
            Study,
            Whereabouts
        },
        data() {
            return {
                activeName: '',
                tabList: [
                    {
                        label: '基本信息',
                        name: '0',
                        path: '/detailsHome/studentAnalysis/studentInformation/studentInformationDetail/information'
                    },{
                        label: '生活规律',
                        name: '1',
                        path: '/detailsHome/studentAnalysis/studentInformation/studentInformationDetail/lawLife'
                    },{
                        label: '消费水平',
                        name: '2',
                        path: '/detailsHome/studentAnalysis/studentInformation/studentInformationDetail/consumption'
                    },{
                        label: '社交关系',
                        name: '3',
                        path: '/detailsHome/studentAnalysis/studentInformation/studentInformationDetail/socialContact'
                    },{
                        label: '图书馆',
                        name: '4',
                        path: '/detailsHome/studentAnalysis/studentInformation/studentInformationDetail/library'
                    },{
                        label: '学习成绩',
                        name: '5',
                        path: '/detailsHome/studentAnalysis/studentInformation/studentInformationDetail/study'
                    },{
                        label: '毕业去向预测',
                        name: '6',
                        path: '/detailsHome/studentAnalysis/studentInformation/studentInformationDetail/whereabouts'
                    }
                ]
            };
        },
        methods: {
            handleClick(tab, event) {
                this.$router.push({
                    path: tab.name,
                })
            }
        },
        created() {
            let _that = this
            let routerPath = _that.$route.path
            if(!_that.activeName) {
                _that.activeName = routerPath
            }
        }
    }
</script>

<style scoped>
    /deep/ .el-tabs__content{
        overflow: initial;
    }
</style>
