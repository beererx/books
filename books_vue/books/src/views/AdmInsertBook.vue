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
                            <el-breadcrumb-item>书籍添加</el-breadcrumb-item>
                    </el-breadcrumb>
                    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                        <el-form-item label="小说id" prop="bookid">
                            <el-input v-model="ruleForm.bookid"></el-input>
                        </el-form-item>
                        <el-form-item label="小说名" prop="name">
                            <el-input v-model="ruleForm.name"></el-input>
                        </el-form-item>
                        <el-form-item label="小说分类" prop="cate">
                            <el-select v-model="ruleForm.cate" placeholder="请选择合适的小说分类">
                                <el-option label="玄幻" value="xuanhuan"></el-option>
                                <el-option label="修真" value="xiuzhen"></el-option>
                                <el-option label="都市" value="dushi"></el-option>
                                <el-option label="历史" value="lishi"></el-option>
                                <el-option label="网游" value="wangyou"></el-option>
                                <el-option label="科幻" value="kehuan"></el-option>
                                <el-option label="言情" value="yanqing"></el-option>
                                <el-option label="其他" value="qita"></el-option>
                                <el-option label="完本" value="quanben"></el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="小说作者" prop="author">
                            <el-input v-model="ruleForm.author"></el-input>
                        </el-form-item>
                        <el-form-item label="小说简介" prop="desc">
                            <el-input
                                type="textarea"
                                :autosize="{ minRows: 2, maxRows: 10}"
                                v-model="ruleForm.desc">
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
import {GetInfoPost,LogininInfoPost,CreateBookInfoPost,ChangeBookInfoPost} from "../apis/read"
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
          name: '',
          desc: '',
          cate: '',
          author: '',
          bookid: ''
        },
        rules: {
          bookid:[
            { required: true, message: '请输入小说id', trigger: 'blur' },
          ],
          name: [
            { required: true, message: '请输入小说书名', trigger: 'blur' },
          ],
          author: [
            { required: true, message: '请输入小说作者名', trigger: 'blur' },
          ],
          cate: [
            { required: true, message: '请选择小说分类', trigger: 'blur' }
          ],
          desc: [
            { required: true, message: '请输入小说简介', trigger: 'blur' }
          ]
        }
      };
    },
    methods: {
      submitForm() {
            const detailparams= reactive({
                url:this.$route.path,
                book_name:"",
                book_cate:"",
                book_author:"",
                book_desc:"",
                book_id:""
            })
            detailparams.book_name = this.ruleForm.name
            detailparams.book_cate = this.ruleForm.cate;
            detailparams.book_author = this.ruleForm.author;
            detailparams.book_desc = this.ruleForm.desc;
            detailparams.book_id = this.ruleForm.bookid;
            detailparams.url = detailparams.url+"/up";
            ChangeBookInfoPost(detailparams).then(res =>{
                    if(res.data.data == "ok"){
                    alert("添加成功!");
                    location.reload()
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