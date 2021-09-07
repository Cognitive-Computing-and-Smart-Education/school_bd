<template>
    <div>
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: item.path }" v-for="(item,index) in breadList" :key="item.path">{{ item.meta.title }}</el-breadcrumb-item>
        </el-breadcrumb>
    </div>
</template>

<script>
    export default {
        name: "homeBreadcrumb",
        data() {
            return {
                breadList: []
            }
        },
        watch: {
            $route() {
                this.getBreadcrumb()
            }
        },
        methods: {
            isHome(router) {
                return router.name === 'home'
            },
            getBreadcrumb() {
                let _that = this
                let matched = _that.$route.matched;
                console.log('matched',_that.$route)
                if(!this.isHome(matched[0])) {
                    for(let i in matched) {
                        if(matched[i].name == 'detailsHome') {
                            matched.splice(i,1)
                            i = i - 1
                        }
                    }
                    if(matched[matched.length - 1].meta.type !== 'menu' && _that.breadList.length > 0) {
                        matched = _that.breadList.concat(matched)
                    }else {
                        matched = [{path: '/', meta: {title: '首页'}}].concat(matched)
                    }
                }
                _that.breadList = matched
                for(let i in _that.breadList) {
                    if(_that.breadList[i].name == 'gradeAnalysis' || _that.breadList[i].name == 'disciplineAnalysis' || _that.breadList[i].name == 'teacherAnalysis') {
                        _that.breadList.splice(i,1)
                        i = i - 1
                    }
                }

                // window.localStorage.setItem('breadList', )
                // console.log('breadList',_that.breadList)
            }
        },
        mounted() {
            let _that = this
            // console.log(_that.$route.matched)
            this.getBreadcrumb()
        }
    }
</script>

<style scoped>

</style>
