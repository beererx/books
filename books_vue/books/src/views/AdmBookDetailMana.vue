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
                            <el-breadcrumb-item>书籍列表</el-breadcrumb-item>
                        </el-breadcrumb>
                        <el-table
                            :data="items.detailsitems.slice((currentPage-1)*pagesize,currentPage*pagesize)"
                            border
                            style="width: 100%">
                            <el-table-column
                            fixed
                            prop="book_id"
                            label="小说id"
                            width="30">
                            </el-table-column>
                            <el-table-column
                            prop="book_name"
                            label="小说名"
                            width="100">
                            </el-table-column>
                            <el-table-column
                            prop="sort_id"
                            label="小说章节id"
                            width="30">
                            </el-table-column>
                            <el-table-column
                            prop="detail_title"
                            label="章节名"
                            width="80">
                            </el-table-column>
                            <el-table-column
                            prop="detail_content"
                            label="小说内容"
                            width="3000">
                            </el-table-column>
                            <el-table-column
                            fixed="right"
                            label="操作"
                            width="100">
                                <template slot-scope="scope">
                                    <el-button type="text" @click="dialogFormVisible = true, handleEdit(scope.row)">修改</el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                        <el-dialog title="章节修改" :visible.sync="dialogFormVisible">
                                <el-form :model="form">
                                    <el-form-item label="小说id" :label-width="formLabelWidth">
                                    <el-input v-model="form.book_id" autocomplete="off" :disabled="true"></el-input>
                                    </el-form-item>
                                    <el-form-item label="小说名" :label-width="formLabelWidth">
                                    <el-input v-model="form.book_name" autocomplete="off" :disabled="true"></el-input>
                                    </el-form-item>
                                    <el-form-item label="章节id" :label-width="formLabelWidth">
                                    <el-input v-model="form.sort_id" autocomplete="off" :disabled="true"></el-input>
                                    </el-form-item>
                                    <el-form-item label="章节名" :label-width="formLabelWidth">
                                    <el-input v-model="form.detail_title" autocomplete="off"></el-input>
                                    </el-form-item>
                                    <el-form-item label="章节内容" :label-width="formLabelWidth">
                                    <el-input
                                        type="textarea"
                                        :autosize="{ minRows: 2, maxRows: 100}"
                                        v-model="form.detail_content">
                                    </el-input>
                                    </el-form-item>
                                </el-form>
                                <div slot="footer" class="dialog-footer">
                                    <el-button @click="dialogFormVisible = false">取 消</el-button>
                                    <el-button type="primary" @click="infosubmit">确 定</el-button>
                                </div>
                        </el-dialog> 
                         <div class="block">
                            <el-pagination
                                @size-change="handleSizeChange"
                                @current-change="handleCurrentChange"
                                :current-page="currentPage"
                                :page-sizes="[20, 50, 70, 100.200]" 
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
import {GetInfoPost,LogininInfoPost,ChangeBookDetailPost} from "../apis/read"
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
            form: {
            book_id:'',
            book_name: '',
            detail_title:'',
            detail_content:'',
            sort_id:''
            },
            formLabelWidth: '120px',
            dialogFormVisible: false
      }    
        
    },
    methods: {
        handleSizeChange (size) {
            this.pagesize = size;
        },
        handleCurrentChange (currentPage) {
            this.currentPage = currentPage;
        },
        handleEdit(row){
            this.form.book_name = row.book_name
            this.form.detail_title = row.detail_title
            this.form.detail_content = row.detail_content
            this.form.book_id = row.book_id
            this.form.sort_id = row.sort_id
        },
        infosubmit(){
            this.dialogFormVisible = false;
            const detailparams= reactive({
                url:this.$route.path,
                book_name:"",
                detail_title:"",
                detail_content:"",
                book_id:"",
                sort_id:""
            })
            detailparams.book_name = this.form.book_name;
            detailparams.detail_title = this.form.detail_title;
            detailparams.detail_content = this.form.detail_content;
            detailparams.book_id = this.form.book_id;
            detailparams.sort_id = this.form.sort_id;
            detailparams.url = detailparams.url+"/up";
            ChangeBookDetailPost(detailparams).then(res =>{
                    if(res.data.data == "ok"){
                    alert("修改成功!");
                    location.reload()
                }
            })
        }
    }
    

    
    
}
</script>


<style scoped lang="scss">
    #sign_up{
        display: none;
    }


</style>