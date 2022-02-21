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
                            <el-breadcrumb-item>密码修改</el-breadcrumb-item>
                        </el-breadcrumb>
                    <b-alert show variant="primary">管理员密码修改</b-alert>
                    <b-form @submit="onSubmit2" @reset="onReset"  v-if="show" id="sign_in">
                        <b-form-group id="input-group-1" label="管理账户名:" label-for="input-1">
                            <b-form-input
                            id="input-1"
                            v-model="form.name"
                            required
                            placeholder="请输入管理账户名">
                            </b-form-input>
                        </b-form-group>
                        <b-form-group id="input-group-2" label="原密码:" label-for="input-2">
                            <b-form-input
                            id="input-2"
                            v-model="form.oldpassword"
                            required
                            type="password"
                            placeholder="请输入原密码">
                            </b-form-input>
                        </b-form-group>
                        <b-form-group id="input-group-3" label="新密码:" label-for="input-3">
                            <b-form-input
                            id="input-3"
                            v-model="form.newpassword1"
                            required
                            type="password"
                            placeholder="请输入新密码">
                            </b-form-input>
                        </b-form-group>
                        <b-form-group id="input-group-4" label="新密码:" label-for="input-4">
                            <b-form-input
                            id="input-4"
                            v-model="form.newpassword2"
                            required
                            type="password"
                            placeholder="请再次输入新密码">
                            </b-form-input>
                        </b-form-group>

                        <b-button type="submit" variant="primary">登录</b-button>
                        <b-button type="reset" variant="danger">重置</b-button>
                    </b-form>
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
import {GetInfoPost,LogininInfoPost,ChangeinInfoPost} from "../apis/read"
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
        
        onMounted(()=>{
            
        });
        return{
            form: {
            name: '',
            oldpassword:'',
            newpassword1:'',
            newpassword2:''
            },
            show: true,
      }    
        
    },
    methods: {
      onSubmit2(evt) {
        evt.preventDefault()
        const chageparams= reactive({
                url:this.$route.path,
                name:"",
                oldpassword:"",
                newpassword1:"",
                newpassword2:""
            })
        chageparams.name = this.form.name;
        chageparams.oldpassword = this.form.oldpassword;
        chageparams.newpassword1 = this.form.newpassword1;
        chageparams.newpassword2 = this.form.newpassword2;
        console.log("dqdww",chageparams)
            ChangeinInfoPost(chageparams).then(res =>{
                if(res.data.data == "no_user"){
                    alert("管理员不存在，请重试!");
                }
                else if(res.data.data == "error_password"){
                    alert("原密码错误，请重试!");
                }
                else if(res.data.data == "ok"){
                    alert("密码修改成功!");
                }
                else if(res.data.data == "no_change"){
                    alert("原密码与新密码相同，请重试!");
                }
                else if(res.data.data == "atypism"){
                    alert("两次输入的新密码不一致，请重试!");
                }
            })

      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form values
        this.form.email = ''
        this.form.name = ''
        this.form.passcode = ''
        this.form.password = ''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
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