<template>
    <div id="Login">
        <Header />
        <b-container class="mt-2">
            <b-row>
                <b-col cols="12" md="3">
                </b-col>
                <b-col cols="12" md="7">
                    <b-alert show variant="primary">管理员登录(账户:root 密码:123456)</b-alert>
                    <b-form @submit="onSubmit2" @reset="onReset"  v-if="show" id="sign_in" @keyup.enter.native="onSubmit2">
                        <b-form-group id="input-group-1" label="用户名:" label-for="input-1">
                            <b-form-input
                            id="input-1"
                            v-model="form.name"
                            required
                            placeholder="请输入管理账户名">
                            </b-form-input>
                        </b-form-group>
                        <b-form-group id="input-group-2" label="密码:" label-for="input-2">
                            <b-form-input
                            id="input-2"
                            v-model="form.password"
                            required
                            type="password"
                            placeholder="请输入密码">
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
            canGet:false,    //获取验证码按钮是否禁用
            time:0,
            btnText: "获取验证码",
            timer:null,
            form: {
            email: '',
            name: '',
            passcode: '',
            password: ''
            },
            show: true,
            count: 60,
      }    
        
    },
    methods: {
      onSubmit2(evt) {
        evt.preventDefault()
        const detailparams= reactive({
                url:this.$route.path,
                name:"",
                password:""
            })
        detailparams.name = this.form.name;
        detailparams.password = this.form.password;
            LogininInfoPost(detailparams).then(res =>{
                if(res.data.data == "no_user"){
                    alert("用户不存在，请重试!");
                }
                else if(res.data.data == "error_password"){
                    alert("密码错误，请重试!");
                }
                else if(res.data.data == "ok"){
                    alert("登录成功!");
                    localStorage.setItem("token",res.data.token)
                    this.$router.push("/adm/main");
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