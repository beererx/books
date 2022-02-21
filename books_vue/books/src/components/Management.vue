<template>
    <div id="Login">
        <b-container class="mt-2">
            <b-row>
                <b-col cols="12" md="2">
                </b-col>
                <b-col cols="12" md="7">
                    <div>
                        <b-button-group vertical>
                            <b-button variant="primary" :href="'/adm/main'">网站简介</b-button>
                            <b-button variant="secondary" :href="'/adm/booksmana'">书籍管理</b-button>
                            <b-button variant="success" :href="'/adm/bookinsert'">书籍添加</b-button>
                            <b-button variant="danger" :href="'/adm/bookdetailmana'">章节管理</b-button>
                            <b-button variant="warning" :href="'/adm/bookdetailinsert'">章节添加</b-button>
                            <b-button variant="info" :href="'/adm/usercollect'">用户管理</b-button>
                            <b-button variant="light" :href="'/adm/passchage'">密码修改</b-button>
                        </b-button-group>
                    </div>
                </b-col>
                <b-col cols="12" md="2">
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import Ads from "../components/Ads.vue";
import AdsFooter from "../components/AdsFooter.vue";
import {ref,reactive,onMounted} from "@vue/composition-api"
import {GetInfoPost,LogininInfoPost} from "../apis/read"
import dateFormat from "../utils/date"
import store from '@/store'
import Vue from 'vue'

export default {
    name:"HomeCate",
    components:{
        Header,
        Footer,
        Ads,
        AdsFooter
    },
    setup(props,context){
        const now_url = ref(context.root.$route.path);
        
        onMounted(()=>{
            
        });
        return{

      }    
        
    }
    

    
    
}
</script>


<style scoped lang="scss">
    #sign_up{
        display: none;
    }


</style>