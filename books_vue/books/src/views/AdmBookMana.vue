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
                            width="50">
                            </el-table-column>
                            <el-table-column
                            prop="book_name"
                            label="小说名"
                            width="120">
                            </el-table-column>
                            <el-table-column
                            prop="book_cate"
                            label="小说分类"
                            width="50">
                            </el-table-column>
                            <el-table-column
                            prop="book_author"
                            label="小说作者"
                            width="100">
                            </el-table-column>
                            <el-table-column
                            prop="book_status"
                            label="小说状态"
                            width="40">
                            </el-table-column>
                            <el-table-column
                            prop="book_last_update_time"
                            label="小说最后更新时间"
                            width="120">
                            </el-table-column>
                            <el-table-column
                            prop="book_desc"
                            label="小说简介"
                            width="350">
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
                        <el-dialog title="书籍修改" :visible.sync="dialogFormVisible">
                                <el-form :model="form">
                                    <el-form-item label="小说id" :label-width="formLabelWidth">
                                    <el-input v-model="form.book_id" autocomplete="off" :disabled="true"></el-input>
                                    </el-form-item>
                                    <el-form-item label="小说名" :label-width="formLabelWidth">
                                    <el-input v-model="form.book_name" autocomplete="off"></el-input>
                                    </el-form-item>
                                    <el-form-item label="小说分类" :label-width="formLabelWidth">
                                    <el-select v-model="form.book_cate" placeholder="请选择小说分类">
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
                                    <el-form-item label="作者" :label-width="formLabelWidth">
                                    <el-input v-model="form.book_author" autocomplete="off"></el-input>
                                    </el-form-item>
                                    <el-form-item label="简介" :label-width="formLabelWidth">
                                    <el-input
                                        type="textarea"
                                        :autosize="{ minRows: 2, maxRows: 10}"
                                        v-model="form.book_desc">
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
            dialogFormVisible: false,
            form: {
            book_name: '',
            book_cate: '',
            book_author: '',
            book_desc: '',
            book_id:''
            },
            formLabelWidth: '120px'
      
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
            this.form.book_cate = row.book_cate
            this.form.book_author = row.book_author
            this.form.book_desc = row.book_desc
            this.form.book_id = row.book_id
        },
        infosubmit(){
            this.dialogFormVisible = false;
            const detailparams= reactive({
                url:this.$route.path,
                book_name:"",
                book_cate:"",
                book_author:"",
                book_desc:"",
                book_id:""
            })
            detailparams.book_name = this.form.book_name;
            detailparams.book_cate = this.form.book_cate;
            detailparams.book_author = this.form.book_author;
            detailparams.book_desc = this.form.book_desc;
            detailparams.book_id = this.form.book_id;
            detailparams.url = detailparams.url+"/up";
            ChangeBookDetailPost(detailparams).then(res =>{
                    if(res.data.data == "ok"){
                    alert("添加成功!");
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