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
                            <el-breadcrumb-item>章节添加</el-breadcrumb-item>
                    </el-breadcrumb>
                    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                        <el-form-item label="小说id" prop="bookid">
                            <el-input v-model="ruleForm.bookid"></el-input>
                        </el-form-item>
                        <el-form-item label="小说名" prop="bookname">
                            <el-input v-model="ruleForm.bookname"></el-input>
                        </el-form-item>
                        <el-form-item label="小说章节id" prop="detailid">
                            <el-input v-model="ruleForm.detailid"></el-input>
                        </el-form-item>
                        <el-form-item label="小说章节标题" prop="detailtitle">
                            <el-input v-model="ruleForm.detailtitle"></el-input>
                        </el-form-item>
                        <el-form-item label="小说章节内容" prop="detailcontent">
                            <el-input
                                type="textarea"
                                :autosize="{ minRows: 2, maxRows: 100}"
                                v-model="ruleForm.detailcontent">
                            </el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="submitForm()">立即创建</el-button>
                            <el-button @click="resetForm('ruleForm')">重置</el-button>
                        </el-form-item>
                    </el-form>
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
import {ref,reactive,onMounted} from "@vue/composition-api"
import {GetInfoPost,LogininInfoPost,CreateBookInfoPost,ChangeBookDetailPost} from "../apis/read"
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
        onMounted(()=>{
            
        });
        return{
      }    
        
    },
    data() {
      return {
        ruleForm: {
          bookname: '',
          bookid: '',
          detailid: '',
          detailtitle: '',
          detailcontent: ''

        },
        rules: {
          bookid:[
            { required: true, message: '请输入小说id', trigger: 'blur' },
          ],
          booknamename: [
            { required: true, message: '请输入小说书名', trigger: 'blur' },
          ],
          detailid: [
            { required: true, message: '请输入小说章节id', trigger: 'blur' },
          ],
          detailtitle: [
            { required: true, message: '请输入小说章节标题', trigger: 'blur' }
          ],
          detailcontent: [
            { required: true, message: '请输入小说章节内容', trigger: 'blur' }
          ]
        }
      };
    },
    methods: {
      submitForm() {
            const detailparams= reactive({
                url:this.$route.path,
                book_name:"",
                book_id:"",
                sort_id:"",
                detail_title:"",
                detail_content:"",
            })
            detailparams.book_name = this.ruleForm.bookname
            detailparams.sort_id = this.ruleForm.detailid;
            detailparams.detail_title = this.ruleForm.detailtitle;
            detailparams.detail_content = this.ruleForm.detailcontent;
            detailparams.book_id = this.ruleForm.bookid;
            detailparams.url = detailparams.url+"/up";
            console.log("sadad",detailparams);
            ChangeBookDetailPost(detailparams).then(res =>{
                    if(res.data.data == "ok"){
                    alert("添加成功!");
                    location.reload()
                  }
                    else if (res.data.data == "no_book"){
                      alert("小说不存在，请重试!");
                    }
            })
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
  
    

    
    
}
</script>


<style scoped lang="scss">
    #sign_up{
        display: none;
    }


</style>