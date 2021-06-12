<template>
  <b-container>
      <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">小说</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item v-for="item in headData.headers" :key="item.id" :href="item.url" :class="item.url == now_url ? 'active':''">{{ item.text }}</b-nav-item>
            <b-nav-item href="#" disabled>最好看的小说就在此</b-nav-item>
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-form>
              <b-form-input size="sm" class="mr-sm-2" placeholder="请输入图书名或作者名"></b-form-input>
              <b-button size="sm" class="my-2 my-sm-0" type="submit">搜索</b-button>
            </b-nav-form>
<!-- 
            <b-nav-item-dropdown right>
              
              <template v-slot:button-content>
                <em>User</em>
              </template>
              <b-dropdown-item href="#">Profile</b-dropdown-item>
              <b-dropdown-item href="#">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown> -->
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </b-container>
</template>

<script>
import {GetCates} from "../apis/read";
import { reactive,ref } from "@vue/composition-api" //reactive定义对象 ref定义常量

export default {
    name:"Header",
    setup(props,context){
      const headData = reactive({
        headers:[]
      });
      GetCates().then(res =>{
        console.log(res);
        headData.headers = res.data.data;
        console.log(headData.headers);
      });
      return {
        headData
      }
    }
};
</script>

<style scoped lang="scss">

</style>
