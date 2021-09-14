<template>
    <div>
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: item.path }" v-for="(item,index) in breadList" :key="item.path">{{ item.meta.title }}</el-breadcrumb-item>
        </el-breadcrumb>
    </div>
</template>

<script>
    import homeManage from '@/router/homeManage.js'

    export default {
        name: "homeBreadcrumb",
        data() {
            return {
                breadList: [],
                routerList: [],
                routerNowList: []
            }
        },
        created() {
            this.routerList = homeManage
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
                    if(_that.breadList.length === 0) {
                        for(let j in _that.routerList) {
                            let obj = _that.routerList[j]
                            if(_that.$route.path.indexOf(obj.name) !== -1) {
                                // console.log(obj)
                                let objOnePath = '/detailsHome/' + obj.name
                                _that.routerNowList.push({path: '/', meta: {title: '首页',showBreadcrumb: true}})
                                _that.routerNowList.push({path: objOnePath, meta: obj.meta, name: obj.name})
                                if(obj.children && obj.children.length > 0) {
                                    for(let k in obj.children) {
                                        let objTwo = obj.children[k]
                                        if(_that.$route.path.indexOf(objTwo.name) !== -1) {
                                            let objTwoPath = objOnePath + '/' + objTwo.name
                                            _that.routerNowList.push({path: objTwoPath, meta: objTwo.meta, name: objTwo.name})
                                        }
                                    }
                                    matched = _that.routerNowList
                                }else {
                                    matched = _that.routerNowList
                                    break;
                                }
                            }
                        }
                    }else if(matched[matched.length - 1].meta.type !== 'menu' && _that.breadList.length > 0) {
                        matched = _that.breadList.concat(matched)
                    }else {
                        matched = [{path: '/', meta: {title: '首页',showBreadcrumb: true}}].concat(matched)
                    }
                }
                _that.breadList = matched
                for(let i in _that.breadList) {
                    if(!_that.breadList[i].meta.showBreadcrumb) {
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
