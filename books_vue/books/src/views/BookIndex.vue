<template>
    <div id="BookIndex">
        <Header />
            <b-container v-if="items.indexitems.length == 1" class="mt-2">
                <b-row>
                    <b-col clos="12" md="4">
                        <b-img thumbnail fluid style="width:80%; margin-left:10%;" :src="items.indexitems[0].image_urls" alt="Image 1"></b-img>
                    </b-col>
                    <b-col clos="12" md="8">
                        <b-jumbotron header-level="5" v-if="items.indexitems[0]" style="padding:15px">
                            <template v-slot:header>{{items.indexitems[0].book_name}}</template>
                            <div>作者：{{items.indexitems[0].book_author}}</div>
                            <div>最新章节：{{items.indexitems[0].book_newest_name}}</div>
                            <div>最后更新时间：{{dateFormat(items.indexitems[0].book_last_update_time)}}</div>
                            <div>本书状态：{{items.indexitems[0].book_status}}</div>
                            <hr class="my-4">
                            <p v-html="items.indexitems[0].book_desc">
                            </p>
                            <hr class="my-4">
                            <b-button variant="primary" :href="'/book/'+items.indexitems[0].book_id+'/'+ items.allcapitems[0].sort_id">开始阅读</b-button>
                            <!-- <b-button variant="success" href="#" style="float:right">加入收藏</b-button> -->
                        </b-jumbotron>    
                    </b-col>
                </b-row>
                <b-row class="mb-2">
                    <b-col class="normal-center"><h5>最近更新的20章图书</h5></b-col> 
                </b-row>
                <b-row class="mb-4">
                    <b-col clos="12" md="4" v-for="item in items.new20capitems" :key="item.id"><a :href="'/book/'+item.book_id+'/'+item.sort_id ">{{ item.detail_title }}</a></b-col>
                </b-row>
                <b-row class="mb-2 ">
                    <b-col class="normal-center"><h5>所有章节的内容</h5></b-col>
                </b-row>
                <b-row class="mb-2">
                    <b-col clos="12" md="4" v-for="item in items.allcapitems" :key="item.id"><a :href="'/book/'+item.book_id+'/'+item.sort_id ">{{ item.detail_title }}</a></b-col>
                </b-row>
            </b-container>
            <b-container v-else class="mt-2">
                抱歉，您查找的图书不存在
            </b-container>
        <Footer />
    </div>
</template>


<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import {GetInfoPost} from "../apis/read";
import {reactive,ref,onMounted} from "@vue/composition-api"
import dateFormat from "../utils/date"
export default{
    name:"BookIndex",
    components:{
        Header,
        Footer
    },
    setup(props,context){
        const now_url = ref(context.root.$route.path);
        const indexparams = reactive({
            url: now_url.value,
            key: 'index'
        });

        const new20params = reactive({
            url: now_url.value,
            key: 'new20'
        });

        const allparams = reactive({
            url: now_url.value,
            key: 'all'
        });

        const titleparams = reactive({
            url: '/title',
            key: 'bookindex'
        });

        const items = reactive({
            indexitems:[],
            allcapitems:[],
            new20capitems:[]
        })
        GetInfoPost(indexparams).then(res =>{
            items.indexitems = res.data.data[0]
        })
        

        GetInfoPost(allparams).then(res =>{
            items.allcapitems = res.data.data
            GetInfoPost(titleparams).then(res => {
                console.log(items.indexitems[0].book_name)
                document.title = items.indexitems[0].book_name +'_'+ res.data.data[0]
                // document.querySelector('meta[name="keywords"]').setAttribute("content", res.data.data[1]);
                // document.querySelector('meta[name="description"]').setAttribute("content", res.data.data[2]);
            });
        });

        GetInfoPost(new20params).then(res =>{
            items.new20capitems = res.data.data
        });

        onMounted(()=>{
            
        })

        return{
            items,
            dateFormat
        }
    }
}
</script>

<style scoped lang="scss">

</style>