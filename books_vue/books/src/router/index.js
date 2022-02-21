import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Cate from "../views/Cate.vue";
import BookIndex from "../views/BookIndex";
import BookDetail from "../views/BookDetail";
import BookSearch from "../views/BookSearch";
import Login from "../views/Login";
import User from "../views/User";
import Asignin from "../views/Asignin";
import AdmMain from "../views/AdmMain";
import AdmBookMana from "../views/AdmBookMana";
import AdmPassChage from "../views/AdmPassChage";
import AdmBookDetailMana from "../views/AdmBookDetailMana";
import AdmInsertBook from "../views/AdmInsertBook";
import AdmInsertBookDatail from "../views/AdmInsertBookDatail";
import AdmUserColl from "../views/AdmUserColl";
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
  },
  {//登录界面
    path: "/login/in",
    name: "Login",
    component: Login
  },
  {//用户界面
    path:"/user/:name",
    name: "User",
    component: User
  },
  {//管理员登入界面
    path: "/adm/login",
    name: "Asignin",
    component: Asignin
  },
  {//管理员控制界面_网站简介
    path: "/adm/main",
    name: "AdmMain",
    component: AdmMain,
    mate:{ authRequired: true}
  },
  {//管理员控制界面_书籍管理
    path: "/adm/booksmana",
    name: "AdmBookMana",
    component: AdmBookMana,
    mate:{ authRequired: true}
  },
  {//管理员控制界面_添加书籍
    path: "/adm/bookinsert",
    name: "AdmInsertBook",
    component: AdmInsertBook,
    mate:{ authRequired: true}
  },
  {//管理员控制界面_章节管理
    path: "/adm/bookdetailmana",
    name: "AdmBookDetailMana",
    component: AdmBookDetailMana,
    mate:{ authRequired: true}
  },
  {//管理员控制界面_添加章节
    path: "/adm/bookdetailinsert",
    name: "AdmInsertBookDatail",
    component: AdmInsertBookDatail,
    mate:{ authRequired: true}
  },
  {//管理员控制界面_用户管理
    path: "/adm/usercollect",
    name: "AdmUserColl",
    component: AdmUserColl,
    mate:{ authRequired: true}
  },
  {//管理员控制界面_修改密码
    path: "/adm/passchage",
    name: "AdmPassChage",
    component: AdmPassChage,
    mate:{ authRequired: true}
  }
];

const router = new VueRouter({
  routes,
  mode:'history',
});

router.beforeEach((to,from,next)=>{
  const token = localStorage.getItem('token')
  if((to.name == 'AdmMain' || to.name == 'AdmBookMana' || to.name == 'AdmInsertBook' || to.name == 'AdmBookDetailMana'
   || to.name == 'AdmInsertBookDatail' || to.name == 'AdmUserColl' || to.name == 'AdmPassChage') && !token) next ({ name: 'Asignin'})
  else next()
})

export default router;
