<template>
    <div>
        <el-card class="school-overview-card current-card-box" shadow="always">
            <div slot="header" class="clearfix current-card-head">
                <span>基本信息</span>
            </div>
            <div class="information-table-allBox">
                <div class="photo-allBox">
                    <div class="photo-information-box">
                        <div class="information-three-box">
                            <div class="information-current-box">
                                <div class="information-label">姓名</div>
                                <div class="information-text">{{ form.name }}</div>
                            </div>
                            <div class="information-current-box">
                                <div class="information-label">出生年月</div>
                                <div class="information-text">{{ form.birth }}</div>
                            </div>
                            <div class="information-current-box">
                                <div class="information-label">入学时间</div>
                                <div class="information-text">{{ form.entrance }}</div>
                            </div>
                        </div>
                        <div class="information-three-box">
                            <div class="information-current-box">
                                <div class="information-label">性别</div>
                                <div class="information-text">{{ form.gender }}</div>
                            </div>
                            <div class="information-current-box">
                                <div class="information-label">民族</div>
                                <div class="information-text">{{ form.nation }}</div>
                            </div>
                            <div class="information-current-box">
                                <div class="information-label">身份证号</div>
                                <div class="information-text">{{ form.IDCard }}</div>
                            </div>
                        </div>
                        <div class="information-three-box">
                            <div class="information-current-box">
                                <div class="information-label">学号</div>
                                <div class="information-text">{{ form.studentNo }}</div>
                            </div>
                            <div class="information-current-box">
                                <div class="information-label">政治面貌</div>
                                <div class="information-text">{{ form.politicalOutlook }}</div>
                            </div>
                            <div class="information-current-box">
                                <div class="information-label">家长电话</div>
                                <div class="information-text">{{ form.phone }}</div>
                            </div>
                        </div>
                    </div>
                    <div class="photo-box">
                        <el-image
                                style="width: 95%; height: 95%"
                                src="https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"
                                fit="cover"></el-image>
                    </div>
                </div>
                <div class="information-current-box">
                    <div class="information-label">籍贯</div>
                    <div class="information-text">{{ form.nativePlace }}</div>
                </div>
                <div class="information-current-box">
                    <div class="information-label">家庭住址</div>
                    <div class="information-text">{{ form.homeAddress }}</div>
                </div>
                <div class="information-four-allBox">
                    <div class="information-four-box">
                        <div class="information-current-box">
                            <div class="information-label">年级</div>
                            <div class="information-text">{{ form.grade }}</div>
                        </div>
                        <div class="information-current-box">
                            <div class="information-label">家庭经济状况</div>
                            <div class="information-text">{{ form.familyEconomic }}</div>
                        </div>
                        <div class="information-current-box">
                            <div class="information-label">是否住校</div>
                            <div class="information-text">{{ form.campusLive }}</div>
                        </div>
                    </div>
                    <div class="information-four-box">
                        <div class="information-current-box">
                            <div class="information-label">班级</div>
                            <div class="information-text">{{ form.class }}</div>
                        </div>
                        <div class="information-current-box">
                            <div class="information-label">是否独生子女</div>
                            <div class="information-text">{{ form.onlyChild }}</div>
                        </div>
                        <div class="information-current-box">
                            <div class="information-label">生源类型</div>
                            <div class="information-text">{{ form.sourceType }}</div>
                        </div>
                    </div>
                    <div class="information-four-box">
                        <div class="information-current-box">
                            <div class="information-label">班级职务</div>
                            <div class="information-text">{{ form.classPosition }}</div>
                        </div>
                        <div class="information-current-box">
                            <div class="information-label">是否孤儿</div>
                            <div class="information-text">{{ form.orphan }}</div>
                        </div>
                        <div class="information-current-box">
                            <div class="information-label">生源地</div>
                            <div class="information-text">{{ form.originPlace }}</div>
                        </div>
                    </div>
                    <div class="information-four-box">
                        <div class="information-current-box">
                            <div class="information-label">健康状况</div>
                            <div class="information-text">{{ form.health }}</div>
                        </div>
                        <div class="information-current-box">
                            <div class="information-label">是否优抚子女</div>
                            <div class="information-text">{{ form.preferentialTreatment }}</div>
                        </div>
                        <div class="information-current-box">
                            <div class="information-label">毕业学校</div>
                            <div class="information-text">{{ form.graduationSchool }}</div>
                        </div>
                    </div>
                </div>
            </div>
        </el-card>
    </div>
</template>

<script>
    export default {
        name: "information",
        data() {
            return {
                form: {
                    name: '',  // 姓名
                    birth: '',  // 出生年月
                    entrance: '',  // 入学时间
                    gender: '',  // 性别
                    nation: '',  // 民族
                    IDCard: '',  // 身份证号
                    studentNo: '',  // 学号
                    politicalOutlook: '',  // 政治面貌
                    phone: '',  // 家长电话
                    nativePlace: '', // 籍贯
                    homeAddress: '',  // 家庭住址
                    grade: '',  // 年级
                    familyEconomic: '',  // 家庭经济状况
                    campusLive: '',  // 是否住校
                    class: '',  //班级
                    onlyChild: '',  // 是否独生子女
                    sourceType: '',  // 生源类型
                    classPosition: '',  // 班级职务
                    orphan: '',  // 是否孤儿
                    originPlace: '', // 生源地
                    health: '', // 健康状况
                    preferentialTreatment: '', //是否优抚子女
                    graduationSchool: ''  // 毕业学校
                }
            }
        },
    }
</script>

<style scoped>
    .information-table-allBox{
        width: 100%;
        border-right: 1px solid #d6d6d6;
        border-bottom: 1px solid #d6d6d6;
    }
    .photo-allBox{
        width: 100%;
        display: flex;
        align-items: stretch;
        justify-content: flex-start;
    }
    .photo-information-box{
        flex: 1;
        display: flex;
        align-items: flex-start;
        justify-content: flex-start;
    }
    .information-three-box{
        width: 33.333333%;
    }
    .photo-box{
        width: 140px;
        border-left: 1px solid #d6d6d6;
        border-top: 1px solid #d6d6d6;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .information-current-box{
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }
    .information-label{
        width: 132px;
        padding: 12px 5px;
        border-left: 1px solid #d6d6d6;
        border-top: 1px solid #d6d6d6;
        height: 48px;
        font-size: 14px;
        text-align: center;
        background-color: #eee;
    }
    .information-text{
        flex: 1;
        padding: 12px 5px;
        border-left: 1px solid #d6d6d6;
        border-top: 1px solid #d6d6d6;
        height: 48px;
    }
    .information-four-allBox{
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }
    .information-four-box{
        width: 25%;
    }
</style>
