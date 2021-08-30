<template>
    <div class="index-main">
        <div class="login-box" id="login">
            <div class="login-top-box flex-box align-items-center justify-content-spaceBetween">
                <div class="login-logo"><img src="../../assets/img/logo3.png"></div>
                <div class="login-top-text flex-box align-items-center">
                    <div class="login-top-icon"><img src="../../assets/img/icon1.png"></div>
                    欢迎登录学校大数据教育平台系统
                </div>
            </div>
            <div class="login-content-box">
                <div class="login-content-bg">
                    <img src="../../assets/img/login-bg.png">
                </div>
                <el-card class="login-card-box">
                    <div class="flex-box login-tabs-box">
                        <div class="login-tabs-text finger" @click="tabsChange(1)" :class="[loginActive === 1 ? 'login-tabs-active' : '']">手机登录</div>
                        <div class="login-tabs-xian"></div>
                        <div class="login-tabs-text finger" @click="tabsChange(2)" :class="[loginActive === 2 ? 'login-tabs-active' : '']">账号登录</div>
                    </div>
                    <div class="login-text-box">
                        <div class="flex-box login-warning-box align-items-center" v-if="errorShow">
                            <i class="el-icon-warning-outline" style="margin-right: 5px;font-size: 14px"></i>
                            {{ loginWarningText }}
                        </div>
                        <div class="login-input-box">
                            <div v-if="loginActive !== 3">
                                <div v-if="loginActive === 1">
                                    <div class="loginBox"><img src="../../assets/img/user.png" class="icon"/><el-input v-model="phoneNo" placeholder="请输入手机号" clearable class="login-input" ></el-input></div>
                                    <div class="loginBox"><img src="../../assets/img/password.png" class="icon"/><el-input placeholder="请输入验证码" v-model="verificationCodeNo" clearable class="login-input"  >
                                        <template slot="append">
                                            <div class="login-verification-code finger" v-if="!verificationCodeStart" @click="verificationCodeBtn">{{ verificationCodeText }}</div>
                                            <div class="login-verification-code finger" v-if="verificationCodeStart">{{ verificationCode }}s</div>
                                        </template>
                                    </el-input></div>
                                </div>
                                <div v-if="loginActive === 2">
                                    <div class="loginBox"><img src="../../assets/img/user.png" class="icon"/><el-input v-model="userName" placeholder="用户名/手机/邮箱" clearable class="login-input" ></el-input></div>
                                    <div class="loginBox"><img src="../../assets/img/password.png" class="icon"/><el-input  v-model="password" placeholder="密码" clearable class="login-input" ></el-input></div>
                                </div>
                                <div class="flex-box align-items-center justify-content-spaceBetween" style="margin-top: 20px">
                                    <div class="login-phone-btn flex-box align-items-center finger" @click="phoneLogin">
                                        <div class="login-phone-icon" v-if="loginActive !== 1"><img src="../../assets/img/phone-icon.png"></div>
                                        <div class="login-phone-text" v-if="loginActive !== 1">短信验证码登录</div>
                                    </div>
                                    <div class="login-forget-box finger">
                                        忘记密码？
                                    </div>
                                </div>
                                <div class="login-btn-box finger" @click="loginBtn">
                                    登录
                                </div>
                            </div>
                            <div v-if="loginActive === 3">
                                <div class="login-ewm-box" v-if="ewmShow"><img src="../../assets/img/ewm.png"></div>
                                <div class="login-ewm-box login-noEwm-box" v-if="!ewmShow">
                                    <div style="width: 100%;margin-bottom: -50px;text-align: center;color: #fff;font-size: 15px">二维码已失效</div>
                                    <div class="login-ewm-invalidBtn finger" @click="refreshBtn">点击刷新</div>
                                </div>
                                <div class="login-ewm-text flex-box align-items-center justify-content-center">
                                    <div class="login-ewm-saoIcon"><img src="../../assets/img/saoyisao.png"></div>
                                    打开<span>微信APP</span>扫码登录
                                </div>
                            </div>
                            <div class="login-register-box flex-box align-items-center justify-content-center" @click="register">
                                <div class="finger">
                                    立即注册
                                    <i class="el-icon-arrow-right" style="font-size: 9px;"></i>
                                </div>
                            </div>
                        </div>
                        <div class="login-arther">
                            <div class="login-arther-title">
                                <div class="login-arther-xian"></div>
                                <div class="login-arther-text">使用以下账号登录</div>
                            </div>
                            <div class="login-arther-content flex-box align-items-center justify-content-spaceBetween">
                                <div class="login-arther-wx flex-box align-items-center finger" v-if="loginActive !== 3" @click="ewmLogin">
                                    <div class="login-arther-wx-icon"><img src="../../assets/img/wx-icon.png"></div>
                                    微信扫码登录
                                </div>
                                <div class="login-arther-wx flex-box align-items-center finger" v-if="loginActive === 3" @click="phoneLogin">
                                    <div class="login-phone-icon"><img src="../../assets/img/phone-icon.png"></div>
                                    短信验证码登录
                                </div>
                            </div>
                        </div>
                    </div>
                </el-card>

                <el-dialog
                        title="用户注册"
                        :visible.sync="registerVisible"
                        width="30%"
                        :before-close="registerClose">
                    <el-form ref="form" :model="registerForm" label-width="90px">
                        <el-form-item label="用户名/姓名">
                            <el-input v-model="registerForm.name" placeholder="请输入用户名/姓名"></el-input>
                        </el-form-item>
                        <el-form-item label="密码">
                            <el-input v-model="registerForm.password" placeholder="请输入密码"></el-input>
                        </el-form-item>
                        <el-form-item label="确认密码">
                            <el-input v-model="registerForm.confirmPassword" placeholder="请再次确认密码"></el-input>
                        </el-form-item>
                        <el-form-item label="学校">
                            <el-select v-model="registerForm.school" placeholder="请选择学校">
                                <el-option label="昆一中" value="昆一中"></el-option>
                                <el-option label="昆三中" value="昆三中"></el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="职位">
                            <el-select v-model="registerForm.position" placeholder="请选择职位">
                                <el-option label="教师" value="教师"></el-option>
                                <el-option label="年级主任" value="年级主任"></el-option>
                                <el-option label="教导主任" value="教导主任"></el-option>
                                <el-option label="政治主任" value="政治主任"></el-option>
                                <el-option label="校级管理" value="校级管理"></el-option>
                                <el-option label="校长" value="校长"></el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="手机号码">
                            <el-input v-model="registerForm.phoneNum" placeholder="请输入手机号码"></el-input>
                        </el-form-item>
                        <el-form-item label="电子邮箱">
                            <el-input v-model="registerForm.email" placeholder="请输入电子邮箱"></el-input>
                        </el-form-item>
                    </el-form>
                      <span slot="footer" class="dialog-footer">
                        <el-button @click="registerVisible = false">取 消</el-button>
                        <el-button type="primary" @click="registerVisible = false">立即创建</el-button>
                      </span>
                </el-dialog>

            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "index",
        components: {

        },
        data() {
            return {
                loginActive: 1,
                loginWarningText: '账户名与密码不匹配，请重新输入',
                phoneNo: '',
                verificationCodeText: '获取验证码',
                verificationCode: 60,
                verificationCodeStart: false,
                registerTimes: '',
                verificationCodeNo: '',
                errorShow: false,
                userName: '',
                password: '',
                ewmShow: true,
                invalid: 60,
                invalidTime: '',
                registerVisible: false,
                registerForm: {
                    name: '',
                    school: '',
                    position: '',
                    phoneNum: '',
                    email: '',
                    password: '',
                    confirmPassword: ''
                }
            }
        },
        methods: {
            registerClose() {
                this.registerVisible = false
            },
            register() {
                this.registerVisible = true
            },
            phoneLogin() {
                if(this.loginActive === 3) {
                    clearInterval(this.invalidTime)
                }
                this.loginActive = 1
                this.errorShow = false
            },
            tabsChange(type) {
                if(this.loginActive === 3) {
                    clearInterval(this.invalidTime)
                }
                this.loginActive = type
                this.errorShow = false
            },
            verificationCodeBtn() {
                this.verificationCodeStart = true
                this.registerTimes = setInterval(()=>{
                    this.verificationCode --
                    if(this.verificationCode === 0){
                        this.verificationCode = 60
                        this.verificationCodeStart = false
                        clearInterval(this.registerTimes)
                    }
                },1000)
            },
            refreshBtn() {
                this.ewmShow = true
                this.invalid = 60
                this.invalidTime = setInterval(()=>{
                    this.invalid --
                    if(this.invalid === 0){
                        this.invalid = 60
                        this.ewmShow = false
                        clearInterval(this.invalidTime)
                    }
                },1000)
            },
            ewmLogin() {
                this.loginActive = 3
                this.ewmShow = true
                this.invalidTime = setInterval(()=>{
                    this.invalid --
                    if(this.invalid === 0){
                        this.invalid = 60
                        this.ewmShow = false
                        clearInterval(this.invalidTime)
                    }
                },1000)
            },
            loginBtn() {
                if(this.loginActive === 1) {
                    if(!this.phoneNo && !this.verificationCodeNo) {
                        this.loginWarningText = '请输入手机号码和验证码'
                        this.errorShow = true
                        return;
                    }
                    if(this.phoneNo && !this.verificationCodeNo) {
                        this.loginWarningText = '请输入验证码'
                        this.errorShow = true
                        return;
                    }
                }
                if(this.loginActive === 2) {
                    if(!this.userName && !this.password) {
                        this.loginWarningText = '请输入用户名和密码'
                        this.errorShow = true
                        return;
                    }
                    if(this.userName && !this.password) {
                        this.loginWarningText = '请输入密码'
                        this.errorShow = true
                        return;
                    }
                }
                this.$router.push({
                    path: '/',
                })
            }
        }
    }
</script>

<style scoped>
    @import "../../assets/style/login.css";
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
