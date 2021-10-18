<template>
    <div id="HomeCate">
        <Header />
        <Ads />
        <b-container class="mt-2">
            <div v-if="items.newitems.length > 0">
                <b-row>
                    <b-col cols="12" md="7">
                        <h4 class="mb-1">最新更新的小说</h4>
                        <div translate="translate" class="bd-example vue-example vue-example-b-table-fields-array notranslate">
                            <div>
                                <table role="table" aria-busy="false" aria-colcount="3" class="table b-table table-striped table-hover" id="__BVID__866">
                                    <thead role="rowgroup" class="">
                                        <tr role="row" class="">
                                            <th role="columnheader" scope="col" aria-colindex="1" class="">小说名</th>
                                            <th role="columnheader" scope="col" aria-colindex="2" class="">最新章节</th>
                                            <th role="columnheader" scope="col" aria-colindex="3" class="">更新时间</th>
                                        </tr>
                                    </thead>
                                    <tbody role="rowgroup">
                                        <tr role="row" v-for="item in items.newitems" :key="item.id">
                                            <td aria-colindex="1" role="cell" class=""><a :href="'/book/'+ item.book_id">{{item.book_name}}</a></td>
                                            <td aria-colindex="2" role="cell" class=""><a :href="'/book/'+ item.book_id + '/'+ item.book_newest_url">{{item.book_newest_name}}</a></td>
                                            <td aria-colindex="3" role="cell" class="">{{dateFormat(item.book_last_update_time)}}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </b-col>
                    <b-col cols="12" md="1">
                    </b-col>
                    <b-col cols="12" md="4">
                        <h4 class="mb-1">最多阅读的小说</h4>
                        <div translate="translate" class="bd-example vue-example vue-example-b-table-fields-array notranslate">
                            <div>
                                <table role="table" aria-busy="false" aria-colcount="3" class="table b-table table-striped table-hover" id="__BVID__866">
                                    <thead role="rowgroup" class="">
                                        <tr role="row" class="">
                                            <th role="columnheader" scope="col" aria-colindex="1" class="">小说名</th>
                                            <th role="columnheader" scope="col" aria-colindex="2" class="">作者</th>
                                        </tr>
                                    </thead>
                                    <tbody role="rowgroup">
                                        <tr role="row" v-for="item in items.mostitems" :key="item.id">
                                            <td aria-colindex="1" role="cell" class=""><a :href="'/book/'+ item.book_id">{{item.book_name}}</a></td>
                                            <!-- <td aria-colindex="2" role="cell" class=""><a :href="'/book/'+ item.book_id + '/'+ item.book_newest_url">{{item.book_author}}</a></td> -->
                                            <td aria-colindex="2" role="cell" class="">{{item.book_author}}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>    
                    </b-col>
                </b-row>
            </div>
            <div v-else>
                无效分类
            </div>
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
import {GetInfoPost} from "../apis/read"
import dateFormat from "../utils/date"

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

        const newparams = reactive({
            url: now_url.value,
            key:"new"
        });
        
        const mostparams = reactive({
            url: now_url.value,
            key:"most"
        });

        const items = reactive({
            newitems:[],
            mostitems:[]
        });

        GetInfoPost(newparams).then(res =>{
            items.newitems = res.data.data[0]
        });

        GetInfoPost(mostparams).then(res =>{
            items.mostitems = res.data.data[0]
        });

        onMounted(()=>{
            const titlePramas = reactive({
                url: '/title',
                key: context.root.$route.path.replace(/\//g,'')
            });

            GetInfoPost(titlePramas).then(res => {
                document.title = res.data.data[0];
                // document.querySelector('meta[name="keywords"]').setAttribute("content", res.data.data[1]);
                // document.querySelector('meta[name="description"]').setAttribute("content", res.data.data[2]);
            });
        });
        return{
            items,
            dateFormat
        }
    }
}
</script>

<style scoped lang="scss">

</style>