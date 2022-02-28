<template>
<b-container>
    <div id="main-top-ad">
        <a target="_blank" href="https://curl.qcloud.com/TS1bu0QZ"><img id="ad_top" style="width:100%" src="../assets/AD_tinypng.jpg"  alt="'https://curl.qcloud.com/TS1bu0QZ'"/></a>
    </div>
    <div id="main-left-ad">
        <a target="_blank" href="https://curl.qcloud.com/TS1bu0QZ"><img src="../assets/AD2_webp.webp"  alt="'https://curl.qcloud.com/TS1bu0QZ'"/></a>
    </div>
    <div id="main-right-ad">
        <a target="_blank" href="https://curl.qcloud.com/TS1bu0QZ"><img src="../assets/AD2.jpg"  alt="'https://curl.qcloud.com/TS1bu0QZ'"/></a>
    </div>
</b-container>
    
</template>

<style lang="scss" scoped>

@media (max-width: 500px) {
    #main-left-ad{
        display: none;
    }  
    
    #main-right-ad{
        display: none;
    }  

    #main-top-ad{
        position: fixed;
        bottom: auto;
        top: 0;
        left: 0;
        z-index: 99999;
        right: 0;
    }

    
}


#main-left-ad{
    position: absolute;
    bottom: auto;
    top: 0;
    width: 150px;
    height: 600px;
    z-index: 99999;
    margin-top: 150px;
    left: 0;
    margin-left: 10px;
}

#main-right-ad{
    position:absolute;
    bottom: auto;
    top: 0;
    width: 150px;
    height: 600px;
    z-index: 99999;
    margin-top: 150px;
    right: 0;
    margin-right: 40px;
}
</style>

<script>
import { GetInfoPost } from "../apis/read.js";
import { reactive } from '@vue/composition-api';


export default {
    name:"Ads",
    setup(props,context){

        const is_PC = () =>{
            if(document.body.clientWidth < 400){
                return 'phone'
            }else{
                return 'pc'
            }
        }
    }
}
</script>