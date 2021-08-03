<template>
    <div id="BookDetail">
        <Header />
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
        <Footer />
    </div>
    
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import { GetInfoPost } from "../apis/read";
import { reactive,ref,onMounted } from "@vue/composition-api"
import { replacebr }   from "../utils/replaceBr"
export default{
    name:"BookDetail",
    components:{
        Header,
        Footer
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
                // document.querySelector('meta[name="keywords"]').setAttribute("content", res.data.data[1]);
                // document.querySelector('meta[name="description"]').setAttribute("content", res.data.data[2]);
            });
        })

        onMounted(()=>{
        
        })

        return{
            items,
            replacebr
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