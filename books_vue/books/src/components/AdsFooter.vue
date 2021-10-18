<template>
    <b-container>
        <div>
            <a href="https://curl.qcloud.com/TS1bu0QZ" target="_blank">
                <img style="width:100%" src="../assets/AD.jpg" alt="'https://curl.qcloud.com/TS1bu0QZ'" />
            </a>
            </div>
    </b-container>
</template>

<style lang="scss" scoped>

</style>

<script>
import { GetInfoPost } from "../apis/read.js";
import { reactive } from '@vue/composition-api';

export default {
    name: "AdsFooter",
    setup(props, context){
        
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