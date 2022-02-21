<template>
    <div id="BookDetail">
        <Header />
        <Ads />
        <b-container v-if="items.detailsitems.length == 1" class="mt-2">
            <b-row>
                <b-col class="mt-2">
                    当前路径：<a href="/">首页</a>--<a :href="'/book/'+items.detailsitems[0].book_id">{{items.detailsitems[0].book_name}}</a>--{{items.detailsitems[0].detail_title}}
                </b-col>
            </b-row>
            <b-row class="mt-2 mb-2">
                <b-col id="detail_title">
                    {{items.detailsitems[0].detail_title}}
                </b-col>
            </b-row>
            <b-row class="mt-2 mb-2">
                <b-col class="normal-center" cols="4" md="4" v-if="items.detailsitems[0].front_sort_id == ''">
                    <a :href="'/book/'+items.detailsitems[0].book_id">上一页</a>
                </b-col>
                <b-col class="normal-center" cols="4" md="4" v-else>
                    <a :href="'/book/'+items.detailsitems[0].book_id+'/'+items.detailsitems[0].front_sort_id">上一页</a>
                </b-col>
                <b-col class="normal-center" cols="4" md="4">
                    <a :href="'/book/'+items.detailsitems[0].book_id">目录</a>
                </b-col>
                <b-col class="normal-center" cols="4" md="4" v-if="items.detailsitems[0].next_sort_id == ''">
                    <a :href="'/book/'+items.detailsitems[0].book_id">下一页</a>
                </b-col>
                <b-col class="normal-center" cols="4" md="4" v-else >
                    <a :href="'/book/'+items.detailsitems[0].book_id+'/'+items.detailsitems[0].next_sort_id">下一页</a>
                </b-col>
            </b-row>
            <div class="mt-3">
                <b-button-group>
                    <b-button variant="primary" @click="init" v-trigger>字体</b-button>
                    <b-button variant="success" @click="fbig">大</b-button>
                    <b-button variant="info" @click="fmiddle">中</b-button>
                    <b-button variant="warning" @click="fsmall">小</b-button>
                    <b-button variant="light" @click="lighton">开灯</b-button>
                    <b-button variant="dark" @click="lightoff">关灯</b-button>
                </b-button-group>
            </div>
            <b-row>
                <b-col>
                    <p id="content_text" v-html="replacebr(items.detailsitems[0].detail_content)"></p>
                </b-col>
            </b-row>
            <b-row class="mt-2 mb-2">
                <b-col class="normal-center" cols="4" md="4" v-if="items.detailsitems[0].front_sort_id == ''">
                    <a :href="'/book/'+items.detailsitems[0].book_id">上一页</a>
                </b-col>
                <b-col class="normal-center" cols="4" md="4" v-else>
                    <a :href="'/book/'+items.detailsitems[0].book_id+'/'+items.detailsitems[0].front_sort_id">上一页</a>
                </b-col>
                <b-col class="normal-center" cols="4" md="4">
                    <a :href="'/book/'+items.detailsitems[0].book_id">目录</a>
                </b-col>
                <b-col class="normal-center" cols="4" md="4" v-if="items.detailsitems[0].next_sort_id == ''">
                    <a :href="'/book/'+items.detailsitems[0].book_id">下一页</a>
                </b-col>
                <b-col class="normal-center" cols="4" md="4" v-else >
                    <a :href="'/book/'+items.detailsitems[0].book_id+'/'+items.detailsitems[0].next_sort_id">下一页</a>
                </b-col>
            </b-row>
        </b-container>
        <b-container v-else class="mt-2">
            图书章节不存在
        </b-container>
        <AdsFooter />
        <Footer />
    </div>
    
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import Ads from "../components/Ads.vue";
import AdsFooter from "../components/AdsFooter.vue";
import { GetInfoPost } from "../apis/read";
import { reactive,ref,onMounted } from "@vue/composition-api"
import { replacebr }   from "../utils/replaceBr"
export default{
    name:"BookDetail",
    components:{
        Header,
        Footer,
        Ads,
        AdsFooter
    },
    setup(props,context){
        const detailparams= reactive({
            url:context.root.$route.path,
            key:""
        })

        const titleparams = reactive({
            url: '/title',
            key: 'bookdetail'
        });

        const items = reactive({
            detailsitems:[]
        })

        GetInfoPost(detailparams).then(res =>{
            items.detailsitems = res.data.data
            GetInfoPost(titleparams).then(res => {
                document.title = items.detailsitems[0].detail_title+'_'+items.detailsitems[0].book_name+'_'+ res.data.data[0]
            });
        })

        onMounted(()=>{
        
        })

        return{
            items,
            replacebr
        }
    },
    methods:{
        fbig(){
            var fsize = document.getElementById("content_text");
            fsize.style.fontSize = "30px";
            document.cookie='fontSize = "30px"';
        },
        fmiddle(){
            var fsize = document.getElementById("content_text");
            fsize.style.fontSize = "25px";
            document.cookie='fontSize = "25px"';
        },
        fsmall(){
            var fsize = document.getElementById("content_text");
            fsize.style.fontSize = "17px";
            document.cookie='fontSize = "17px"';
        },
        lighton(){
            var light = document.getElementById("BookDetail");
            light.style.backgroundColor = "#E9FAFF";
        },
        lightoff(){
            var light = document.getElementById("BookDetail");
            light.style.backgroundColor = "#617379";
        },
        init(){
            var strcookie = document.cookie;
            var arrcookie = strcookie.split("; ");
            for ( var i = 0; i < arrcookie.length; i++) {
                var arr = arrcookie[i].split("=");
                if (arr[0] == "fontSize"){
                    var num = arr[1].replace(/[^\d]/g,' ');
                    num = parseInt(num)
                    var fsize = document.getElementById("content_text");
                    fsize.style.fontSize = num + "px";
                }
            }
        }
    },
    directives:{
        trigger:{
            inserted(el,binging){
                el.click()
      }
   }
 }
    
}
</script>

<style scoped lang="scss">
#detail_title{
    text-align: center;
    font-size: 22px;
}
#detail_list{
    text-align: center;
}
#content_text{
    text-indent: 13px;
    font-size: 17px;
    line-height: 35px;
}

</style>