<template>
    <el-container style="width: 100%;height: 100%">
        <el-aside width="200px">
            <home-aside></home-aside>
        </el-aside>
        <el-container>
            <el-header>
                <home-head></home-head>
            </el-header>
            <el-main class="home-main">
               <router-view  v-if="isRouterAlive"></router-view>
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
    import homeAside from './components/homeAside'
    import homeHead from './components/homeHead'

    export default {
        name: "index",
        provide(){
            return{
                reload:this.reload
            }
        },
        data() {
            return {
                isRouterAlive: true
            }
        },
        components: {
            homeHead,
            homeAside
        },
        methods: {
            ceshi() {
               // console.log(homeManage)
            },
            reload(){
                this.isRouterAlive = false
                this.$nextTick(function () {
                    this.isRouterAlive = true
                })
            }
        }
    }
</script>

<style scoped>
    /deep/ .el-header{
        padding: 0;
    }
    .home-main{
        padding: 12px;
    }
</style>
