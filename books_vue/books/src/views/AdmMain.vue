<template>
    <div id="Login">
        <Header />
        <b-container class="mt-2">
            <b-row>
                <b-col cols="12" md="2">
                    <Management />
                </b-col>
                <b-col cols="12" md="8">
                    <el-breadcrumb separator="/">
                            <el-breadcrumb-item><i class="el-icon-date"></i> 网站管理</el-breadcrumb-item>
                            <el-breadcrumb-item>网站简介</el-breadcrumb-item>
                        </el-breadcrumb>
                    <div>
                        <b-carousel
                            id="carousel-no-animation"
                            style="text-shadow: 0px 0px 2px #000"
                            no-animation
                            indicators
                            img-width="1024"
                            img-height="480"

                        >
                            <b-carousel-slide
                            caption="目前本网站共有书籍"
                            img-src="https://picsum.photos/1024/480/?image=10"
                            >{{items.detailsitems[0].book_infos}}本</b-carousel-slide>
                            <b-carousel-slide
                            caption="目前本网站共有小说章节"
                            img-src="https://picsum.photos/1024/480/?image=12"
                            >{{items.detailsitems[0].book_details}}章</b-carousel-slide>
                            <b-carousel-slide
                            caption="目前本网站共有用户"
                            img-src="https://picsum.photos/1024/480/?image=22"
                            >{{items.detailsitems[0].user}}位</b-carousel-slide>
                            <b-carousel-slide
                            caption="目前本网站共有管理员"
                            img-src="https://picsum.photos/1024/480/?image=23"
                            >{{items.detailsitems[0].administrators}}位</b-carousel-slide>
                        </b-carousel>
                    </div>
                    <div>
                        <BookCateNum />
                    </div>
                </b-col>
                <b-col cols="12" md="2">
                </b-col>
            </b-row>
        </b-container>
        <Footer />
    </div>
</template>

<script>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import Ads from "../components/Ads.vue";
import AdsFooter from "../components/AdsFooter.vue";
import Management from "../components/Management.vue";
import BookCateNum from "../components/BookCateNum.vue";
import {ref,reactive,onMounted} from "@vue/composition-api"
import {GetInfoPost,LogininInfoPost} from "../apis/read"
import dateFormat from "../utils/date"
import store from '@/store'
import Vue from 'vue'
// import * as echarts from 'echarts'
export default {
    name:"HomeCate",
    components:{
        Header,
        Footer,
        Ads,
        AdsFooter,
        Management,
        BookCateNum
    },
    setup(props,context){
         const detailparams= reactive({
            url:context.root.$route.path,
            key:""
        })

        const items = reactive({
            detailsitems:[]
        })

        GetInfoPost(detailparams).then(res =>{
            items.detailsitems = res.data.data
        })
        onMounted(()=>{
        });
        return{
            items
      }    
        
    }
}
</script>


<style scoped lang="scss">
    #sign_up{
        display: none;
    }


</style>