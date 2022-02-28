<template>
    <div id="HomeCate">
        <Header />
        <Ads />
        <b-container class="mt-2">
            <b-row>
                <b-card-group  deck v-for="item in items.detailsitems" :key="item.id" class="col-md-6" style="margin-left:6px">
                    <b-card no-body class="overflow-hidden" style="max-width: 540px;">
                        <b-row no-gutters>
                        <b-col md="6">
                            <b-card-img-lazy :src="item.image_urls" class="rounded-0" ></b-card-img-lazy>
                        </b-col>
                        <b-col md="6">
                            <b-card-body :title="item.book_name">
                                <b-card-text>
                                    作者:{{item.book_author}}</p>
                                    本书状态:{{item.book_status}}</p>
                                    简介:{{item.book_desc}}
                                </b-card-text>
                                <b-button variant="primary" :href="'/book/'+ item.book_id">开始阅读</b-button>
                            </b-card-body>
                        </b-col>
                        </b-row>
                    </b-card>
                </b-card-group>   
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
        const detailparams= reactive({
            url:context.root.$route.path,
            key:""
        })

        const items = reactive({
            detailsitems:[]
        })

        GetInfoPost(detailparams).then(res =>{
            items.detailsitems = res.data.data
            for(var i = 0;i<items.detailsitems.length;i++){
                var cut = items.detailsitems[i].book_desc
                if(cut.length>70){
                    cut = cut.substr(0,70)
                    cut = cut+"..."
                    items.detailsitems[i].book_desc = cut
                }
                
            }
        })
        onMounted(()=>{
            
        });
        return{
            items
      }    
        
    }
}
</script>

<style scoped lang="scss">

</style>