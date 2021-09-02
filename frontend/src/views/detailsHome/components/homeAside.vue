<template>
    <el-col class="aside-scroll">
        <div class="aside-logo"><img src="../../../assets/img/logo4.png"></div>
        <el-menu
                :unique-opened="true"
                :router="true"
                background-color="#545c64"
                text-color="#fff"
                active-text-color="#fff"
                @select="handleSelect"
                :default-active="activeAside"
                class="el-menu-vertical-demo aside-tree"
                :class="{'aside-tree-sm':isCollapse}"
                ref="asideMenu"
                :collapse="isCollapse || false">
            <template>
                <el-menu-item width="200px"
                              style="padding-left: 30px;padding-right:0px;margin-left: 0px;text-align: left"
                              :index="'/'"
                              :route="{path:'/',name:'home'}"
                              :key="'/'">
                    <template slot="title">
                        <i class="el-icon-location" style="color: #fff;width: 14px;margin-right: 8px"></i>
                        <span slot="title">首页</span>
                    </template>
                </el-menu-item>
            </template>
            <template v-for="(item,index) in routerList">
                <el-submenu :key="index" :index="index+''" v-if="item.children">
                    <template slot="title">
                        <i :class="item.meta.icon" style="color: #fff;width: 14px;margin-right: 8px"></i>
                        <span slot="title">{{item.meta.title}}</span>
                    </template>
                    <el-menu-item width="200px"
                                  style="padding-left: 30px;padding-right:0px;margin-left: 0px;text-align: left"
                                  v-for="child in item.children"
                                  :index="child.path"
                                  :route="{path:child.path,name:child.name}"
                                  :key="child.path">{{child.meta.title}}
                    </el-menu-item>
                </el-submenu>
                <el-menu-item width="200px" v-else
                              style="padding-left: 30px;padding-right:0px;margin-left: 0px;text-align: left"
                              :index="item.path"
                              :route="{path:item.path,name:item.name}"
                              :key="item.path">
                    <template slot="title">
                        <i :class="item.meta.icon" style="color: #fff;width: 14px;margin-right: 8px"></i>
                        <span slot="title">{{item.meta.title}}</span>
                    </template>
                </el-menu-item>
            </template>
        </el-menu>
    </el-col>
</template>

<script>
    import homeManage from '@/router/homeManage.js'
    import { mapGetters, mapMutations } from "vuex";

    export default {
        name: "homeAside",
        data() {
            return {
                routerList: [],
                activeAside: ''
            }
        },
        props: ['isCollapse'],
        created() {
            this.routerList = homeManage
            console.log(this.routerList)
        },
        computed: {
            ...mapGetters(["routerPath"]),
        },
        watch: {
            routerPath() {
                // this.getNowTime();
                // console.log(this.routerPath)
                this.activeAside = this.routerPath
            }
        },
        methods: {
            ...mapMutations(["changeRouterPath"]),
            handleSelect(index, indexPath) {
                let _that = this
                _that.changeRouterPath(index);
                // this.$nextTick(() => {
                //     this.$router.push({
                //         path: index,
                //     })
                // })
            }
        }
    }
</script>

<style scoped>
    /deep/ .el-menu-item{
        padding-left: 20px !important;
    }
    /deep/ .el-submenu .el-menu-item{
        padding-left: 50px !important;
    }
    .aside-logo{
        width: 100%;
        border-bottom: 1px solid #5c646b;
        padding: 10px;
    }
    .aside-logo img{
        width: 100%;
        display: inline-block;
    }
    .aside-scroll{
        width: 200px;
        height: 100%;
        overflow-x: hidden;
        background-color: #545c64;
        /*background: url('~@/assets/images/aside_bg.png') no-repeat 0 320px;*/
        /*background-size: 100%;*/
    }
    .aside-tree{
        width: 200px;
        background: transparent;
        transition: all .3s;
        border-right: none;
    }
    .aside-tree-sm{
        width: 65px;
    }
    /*.el-menu-item:hover{*/
    /*    background-color: #009688 !important;*/
    /*}*/
    .el-menu-item.is-active{
        background-color: rgba(67,74,80,1) !important;
    }
</style>
