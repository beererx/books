<template>
    <div id="User">
        <Header />
        <Ads />
            <b-container class="mt-2">
                <b-row>
                    <b-col clos="12" md="3">
                        
                    </b-col>
                    <b-col clos="12" md="7">
                        <b-jumbotron header-level="5"  style="padding:15px">
                            <template v-slot:header>用户名:{{items.useritems[0].user_name}}</template>
                            <div>用户编号:{{items.useritems[0].user_id}}</div>
                            <div>等级:{{items.useritems[0].dlevel}}</div>
                            <div>签到次数:{{items.useritems[0].signin}}</div>
                            <hr class="my-4">
                            <b-button variant="primary" @click="dosignin">签到</b-button>
                        </b-jumbotron>    
                    </b-col>
                    <b-col clos="12" md="2">
                        
                    </b-col>
                </b-row>
            </b-container>
        <AdsFooter />
        <Footer />
    </div>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import Ads from "../components/Ads.vue";
import AdsFooter from "../components/AdsFooter.vue";
import {GetInfoPost} from "../apis/read";
import {reactive,ref,onMounted} from "@vue/composition-api"
import dateFormat from "../utils/date"
export default{
    name:"BookIndex",
    components:{
        Header,
        Footer,
        Ads,
        AdsFooter
    },
    setup(props,context){
        const userparams= reactive({
            url:context.root.$route.path,
            key:""
        })

        const items = reactive({
            useritems:[]
        })

        GetInfoPost(userparams).then(res =>{
            items.useritems = res.data.data
        })
        onMounted(()=>{
            
        })

        return{
            items
        }
    },
    methods:{
        dosignin(){
            const signinparams= reactive({
                url:this.$route.path,
                key:""
            })
            const userparams= reactive({
            url:this.$route.path,
            key:""
            })
            signinparams.url =signinparams.url+"/signin"
            GetInfoPost(signinparams).then(res =>{
                console.log("dsafddfas",res.data.data)
                if(res.data.data == "less_time"){
                    alert("距离上次签到还未满24小时!")
                }
                else{
                    alert("签到成功!")
                    GetInfoPost(userparams).then(res =>{
                     this.items.useritems = res.data.data
                    })
                }
            })
        }
    }
}
</script>

<style scoped lang="scss">

</style>