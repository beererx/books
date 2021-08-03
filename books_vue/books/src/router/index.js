import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Cate from "../views/Cate.vue";
import BookIndex from "../views/BookIndex";
import BookDetail from "../views/BookDetail";
import BookSearch from "../views/BookSearch";

Vue.use(VueRouter);

const routes = [
  { //图书首页
    path: "/",
    name: "Home",
    component: Home,
  },
  {//图书搜索页
    path: "/search",
    name: "BookSearch",
    component: BookSearch
  },
  { //图书分类页
    path: "/:cate_id",
    name: "Cate",
    component: Cate
  },
  {//图书介绍页
    path: "/book/:book_id",
    name: "BookIndex",
    component: BookIndex
  },
  {//图书阅读页
    path: "/book/:book_id/:sort_id",
    name: "BookDetail",
    component: BookDetail
  }
];

const router = new VueRouter({
  routes,
  mode:'history',
});

export default router;
