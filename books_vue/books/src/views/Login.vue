<template>
    <div id="Login">
        <Header />
        <Ads />
        <b-container class="mt-2">
            <b-row>
                <b-col cols="12" md="3">
                    <b-button variant="success" @click="pushin">登录</b-button>
                    <b-button variant="outline-primary" @click="pushup">注册</b-button>
                </b-col>
                <b-col cols="12" md="7">
                    <b-form @submit="onSubmit" @reset="onReset"  v-if="show" id="sign_up">
                        <b-alert show variant="success">用户注册</b-alert>
                        <b-form-group
                        id="input-group-1"
                        label="邮箱地址:"
                        label-for="input-1"
                        description="我们不会将您的邮箱用于不正当行为。">
                            <b-form-input
                            id="input-1"
                            v-model="form.email"
                            type="email"
                            required
                            placeholder="请输入正确的邮箱地址">
                            </b-form-input>
                        </b-form-group>
                        <b-button variant="outline-primary" @click="onclickV"  id="verification"  :disabled ="canGet">{{btnText}}</b-button>
                        <b-form-group id="input-group-2" label="用户名:" label-for="input-2">
                            <b-form-input
                            id="input-2"
                            v-model="form.name"
                            required
                            placeholder="请输入用户名">
                            </b-form-input>
                        </b-form-group>
                        <b-form-group id="input-group-3" label="验证码:" label-for="input-3">
                            <b-form-input
                            id="input-3"
                            v-model="form.passcode"
                            required
                            placeholder="请输入验证码">
                            </b-form-input>
                        </b-form-group>
                        <b-form-group id="input-group-4" label="密码:" label-for="input-4">
                            <b-form-input
                            id="input-4"
                            v-model="form.password"
                            required
                            type="password"
                            placeholder="请输入密码">
                            </b-form-input>
                        </b-form-group>

                        <b-button type="submit" variant="primary">注册</b-button>
                        <b-button type="reset" variant="danger">重置</b-button>
                    </b-form>
                    <b-form @submit="onSubmit2" @reset="onReset"  v-if="show" id="sign_in">
                        <b-alert show variant="info">用户登录</b-alert>
                        <b-form-group id="input-group-1" label="用户名:" label-for="input-1">
                            <b-form-input
                            id="input-1"
                            v-model="form.name"
                            required
                            placeholder="请输入用户名">
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
        <AdsFooter />
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
      onSubmit(evt) {
        evt.preventDefault()
        const detailparams= reactive({
                url:this.$route.path,
                email:"",
                name:"",
                passcode:"",
                password:""
            })
        detailparams.email = this.form.email;
        detailparams.name = this.form.name;
        detailparams.passcode = this.form.passcode;
        detailparams.password = this.form.password;
        detailparams.url = detailparams.url+"/up";

            LogininInfoPost(detailparams).then(res =>{
                if(res.data.data == "ok"){
                    alert("注册成功,请登录!");
                }
                else if(res.data.data == "no_name"){
                    alert("用户名已被占用,请重试!");
                    this.form.name = ''
                }
                else if(res.data.data == "no_email"){
                    alert("邮箱未验证,请先进行邮箱验证!");
                }
                else if(res.data.data == "no_code"){
                    alert("验证码错误或超时,请重新输入验证码!");
                    this.form.passcode = ''
                }
                else if(res.data.data == "short_password"){
                    alert("密码至少需要8位,请重新设置密码!");
                    this.form.password = ''
                }
            })

      },
      onSubmit2(evt) {
        evt.preventDefault()
        const detailparams= reactive({
                url:this.$route.path,
                name:"",
                password:""
            })
        detailparams.name = this.form.name;
        detailparams.password = this.form.password;
        detailparams.url = detailparams.url+"/in";
        console.log("dqdww",detailparams)
            LogininInfoPost(detailparams).then(res =>{
                if(res.data.data == "no_user"){
                    alert("用户不存在,请重试!");
                }
                else if(res.data.data == "error_password"){
                    alert("密码错误,请重试!");
                }
                else if(res.data.data == "ok"){
                    alert("登录成功!");
                    this.$router.push("/user/"+detailparams.name);
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
      },
      onclickV (){
            const detailparams= reactive({
                url:this.$route.path,
                key:""
            })
            this.canGet = true;  //禁用按钮，防止多次触发
            this.time = 60;  //60秒后能继续按按钮
            this.timer1();
            detailparams.key = this.form.email;
            GetInfoPost(detailparams).then(res =>{
                if(res.data.data == "no"){
                    alert("输入的邮箱地址有误,请重新输入！")
                    this.form.email = ''
                }
        
            })
        },
      timer1(){   //验证码60s内不能继续点击的函数
            if(this.time > 0) {
                this.time--;
                this.btnText = this.time + "s后重新获取"
                this.timer = setTimeout(this.timer1,1000)
            }else{
                this.time = 0;
                this.btnText = "获取验证码";
                this.canGet = false;
                clearTimeout(this.timer);
            }
        },
        pushup(){
            document.getElementById('sign_in').style.display = "none";
            document.getElementById('sign_up').style.display = "inline";
        },
        pushin(){
            document.getElementById('sign_up').style.display = "none";
            document.getElementById('sign_in').style.display = "inline";
        }

    }
    

    
    
}
</script>


<style scoped lang="scss">
    #sign_up{
        display: none;
    }


</style>