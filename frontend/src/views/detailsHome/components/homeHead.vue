<template>
    <div class="container">
        <div class="head-left">
            <el-tooltip content="收起菜单" placement="bottom" style="margin-right: 10px">
                <div class="header-collapse finger" @click="ceshi">
                    <i class="el-icon-s-fold"></i>
                </div>
            </el-tooltip>
            <div class="head-breadcrumb">
                <home-breadcrumb></home-breadcrumb>
            </div>
        </div>
        <div class="user-message">
            <div class="user-img">
                <el-image
                        style="width: 100%; height: 100%"
                        :src="userImg"
                        fit="cover"></el-image>
            </div>
            <el-dropdown trigger="click">
               <span class="el-dropdown-link finger">
                 您好，欢迎登录学校大数据教育平台<i class="el-icon-arrow-down el-icon--right"></i>
               </span>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item>用户设置</el-dropdown-item>
                    <el-dropdown-item>安全退出</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
        </div>
    </div>
</template>

<script>
    import homeBreadcrumb from './homeBreadcrumb'

    export default {
        name: "homeHead",
        data() {
            return {
                userImg: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
            }
        },
        components: {
            homeBreadcrumb
        },
        methods: {
            ceshi() {
                let _that = this
                // console.log(_that.$route.matched)
            }
        }
    }
</script>

<style scoped>
    .container{
        width: 100%;
        height: 100%;
        display: flex;
        background-color: #fff;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 1px 8px #888888;
        padding: 20px;
    }
    .header-collapse i{
        font-size: 18px;
        box-sizing: content-box;
    }
    .user-img{
        width: 32px;
        height: 32px;
        border-radius: 50%;
        overflow: hidden;
        margin-right: 10px;
    }
    .user-message{
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }
    .head-left{
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }
    .head-breadcrumb{
        padding-left: 10px;
        border-left: 1px solid #eee;
    }
</style>
