<template>
  <b-container id="Header">
      <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">小说</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item v-for="item in headData.headers" :key="item.id" :href="item.url" :class="item.url == now_url ? 'active':''">{{ item.text }}</b-nav-item>
            <b-nav-item href="#" disabled>最好看的小说就在此</b-nav-item>
          </b-navbar-nav>
          <b-navbar-nav class="ml-auto">
            <ul  class="navbar-nav ml-auto">
              <li  class="form-inline">
                <div class="form-inline">
                  <input v-model="search.key" type="text" placeholder="请输入图书名或作者名" class="mr-sm-2 form-control form-control-sm" id="__BVID__14">
                  <button @click="onclickS" type="submit" class="btn my-2 my-sm-0 btn-secondary btn-sm">搜索</button>
                </div>
              </li>
            </ul>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </b-container>
</template>

<script>
import {GetCates} from "../apis/read";
import { reactive,ref,onMounted} from "@vue/composition-api" //reactive定义对象 ref定义常量
import { stripscript } from "../apis/validate"
export default {
    name:"Header",
    setup(props,context){
      const now_url = ref(context.root.$route.path);

      const headData = reactive({
        headers:[]
      });
      GetCates().then(res =>{
        //console.log(res);
        headData.headers = res.data.data;
        //console.log(headData.headers);
      });

      onMounted(()=>{
        
      })

      const search = reactive({
        key:''
      });

      const onclickS = () =>{
        if (stripscript(search.key) == false || search.key == ''){
          alert("输入错误，请重试")
        }
        else{
          context.root.$router.push({
            path: '/search',
            query:{
              q:search.key
            }
          })
        }
        
      }

      return {
        headData,
        now_url,
        search,
        onclickS
      }
    }
};
</script>

<style scoped lang="scss">
@media (max-width:500px) {
  #Header{
    margin-top:37px
  }
}
</style>
