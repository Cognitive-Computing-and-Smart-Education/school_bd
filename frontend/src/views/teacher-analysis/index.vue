<template>
    <div>
        <router-view class="container"/>
    </div>
</template>

<script>
    export default {
        inject: ["reload"],
        name: "index",
        data(){
            return{

            }
        },
        mounted() {
            console.log(this.$route);
            this.$nextTick(() => {
                this.reload()
            })
        },
        methods: {

        }
    }

</script>

<style scoped>

</style>
