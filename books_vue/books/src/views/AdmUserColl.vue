<template>
    <div id="Login">
        <Header />
        <b-container class="mt-2">
            <b-row>
                <b-col cols="12" md="2">
                    <Management />
                </b-col>
                <b-col cols="12" md="10">
                    <div class="crumbs">
                        <el-breadcrumb separator="/">
                            <el-breadcrumb-item><i class="el-icon-date"></i> 网站管理</el-breadcrumb-item>
                            <el-breadcrumb-item>用户列表</el-breadcrumb-item>
                        </el-breadcrumb>
                        <el-table
                            :data="items.detailsitems.slice((currentPage-1)*pagesize,currentPage*pagesize)"
                            border
                            style="width: 100%">
                            <el-table-column
                            fixed
                            prop="user_name"
                            label="用户名"
                            width="100">
                            </el-table-column>
                            <el-table-column
                            prop="user_mail"
                            label="用户邮箱"
                            width="250">
                            </el-table-column>
                            <el-table-column
                            prop="signin"
                            label="签到次数"
                            width="100">
                            </el-table-column>
                            <el-table-column
                            prop="dlevel"
                            label="用户等级"
                            width="100">
                            </el-table-column>
                            <el-table-column
                            prop="last_signed"
                            label="最后签到时间"
                            width="250">
                            </el-table-column>
                            <el-table-column
                            fixed="right"
                            label="操作"
                            width="100">
                                <template slot-scope="scope">
                                    <el-button type="text"></el-button>
                                </template>
                            </el-table-column>
                        </el-table> 
                         <div class="block">
                            <el-pagination
                                @size-change="handleSizeChange"
                                @current-change="handleCurrentChange"
                                :current-page="currentPage"
                                :page-sizes="[20, 50, 70, 100.200,300]" 
                                :page-size="pagesize"        
                                layout="total, sizes, prev, pager, next, jumper"
                                :total="items.detailsitems.length"> 
                            </el-pagination>
                        </div>   
                    </div>
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
import {ref,reactive,onMounted} from "@vue/composition-api"
import {GetInfoPost,LogininInfoPost,ChangeBookInfoPost,ChangeBookDetailPost} from "../apis/read"
import dateFormat from "../utils/date"
import store from '@/store'
import Vue from 'vue'

export default {
    name:"HomeCate",
    components:{
        Header,
        Footer,
        Ads,
        AdsFooter,
        Management
    },
    setup(props,context){
        const now_url = ref(context.root.$route.path);
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
            items,
            currentPage:1, 
            pagesize:20,
      }    
        
    },
    methods: {
        handleSizeChange (size) {
            this.pagesize = size;
        },
        handleCurrentChange (currentPage) {
            this.currentPage = currentPage;
        }
       
    }
    

    
    
}
</script>


<style scoped lang="scss">
    #sign_up{
        display: none;
    }


</style>