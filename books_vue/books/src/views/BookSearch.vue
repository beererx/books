<template>
    <div id="BookSearch">
        <Header />
        <b-container class="mt-2">
            <b-row><b-col><h4>查询结果</h4></b-col></b-row>
            <b-row>
                <b-col v-if="searchres.items.length > 0">
                    <table role="table" aria-busy="false" aria-colcount="3" class="table b-table table-striped table-hover">
                        <thead role="rowgroup" class="">
                            <tr role="row" class="">
                                <th role="columnheader" scope="col" aria-colindex="1" class=""><div>图书名字</div></th>
                                <th role="columnheader" scope="col" aria-colindex="2" class=""><div>作者</div></th>
                                <th role="columnheader" scope="col" aria-colindex="3" class=""><div>最新章节</div></th>
                            </tr>
                        </thead>
                        <tbody role="rowgroup">
                            <tr role="row" v-for="item in searchres.items" :key="item.id">
                                <td aria-colindex="1" role="cell" class=""><a :href="'/book/'+item.book_id">{{ item.book_name }}</a></td>
                                <td aria-colindex="2" role="cell" class="">{{ item.book_author }}</td>
                                <td aria-colindex="3" role="cell" class=""><a :href="'/book/'+item.book_id+'/'+item.book_newest_url">{{ item.book_newest_name }}</a></td>
                            </tr>
                        </tbody>
                        
                    </table>
                </b-col>
                <b-col v-else>
                    您所查询的图书不存在，请重新尝试
                </b-col>
            </b-row>
        </b-container>
        <Footer />
    </div>
</template>

<script>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import {ref,reactive,onMounted} from "@vue/composition-api"
import {GetInfoPost} from "../apis/read"
import dateFormat from "../utils/date"

export default {
    name:"BookSearch",
    components:{
        Header,
        Footer
    },
    setup(props,context){
        const searchparams = reactive({
            url: "/search",
            key: context.root.$route.query.q
        });

        const searchres = reactive({
          items:[]
        })
        GetInfoPost(searchparams).then(res => {
            searchres.items = res.data.data
        });
        
        onMounted(()=>{
            
        });
        return{
            searchres
        }
        
    }
}
</script>

<style scoped lang="scss">

</style>