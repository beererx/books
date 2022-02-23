<template>
  <div>
    <div id="main" style="height:730px;width:730px"></div>
  </div>
</template>

<script>
import {ref,reactive,onMounted} from "@vue/composition-api"
import {GetInfoPost,GetBookCateNum} from "../apis/read"

export default {
  name: 'HomeCate',
  data() {
    return {
    };
  },
  mounted() {
    this.GetBookcateNum()
  },
  methods: {
    GetBookcateNum(){
        const bookcate= reactive({
            key:""
        })
        const items = reactive({
            bookitems:[]
        })

        GetBookCateNum(bookcate).then(res =>{
            items.bookitems = res.data.data
            var servicedata=[];
             for(var i=0;i<items.bookitems.length;i++){
                 var obj=new Object();
                 obj.value=items.bookitems[i].num;
                 obj.name=items.bookitems[i].book_cate;
                 servicedata[i]=obj;
             }
            var myChart = this.$echarts.init(document.getElementById('main'));
            var option = {
                title: {
                    text: '小说类型分类',
                    subtext: '',
                    left: 'center'
                },
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    top: '5%',
                    left: 'center'
                },
                series: [
                    {
                    name: '小说数量',
                    type: 'pie',
                    radius: ['40%', '70%'],
                    avoidLabelOverlap: false,
                    itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                    },
                    label: {
                        show: false,
                        position: 'center'
                    },
                    emphasis: {
                        label: {
                        show: true,
                        fontSize: '40',
                        fontWeight: 'bold'
                        }
                    },
                    labelLine: {
                        show: false
                    },
                    data: servicedata
                    }
                ]
            };
            myChart.setOption(option);
        })
    }
  },
};
</script>