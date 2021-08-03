import service from "../utils/request";
import { rsaEncrypt } from "../utils/rsa";

export function GetCates(){
    return service.request({
        url:"/books_cates",
        method:"get"
    });
}

export function GetInfoPost(postparams){
    return service.request({
        method:"post",
        url:postparams.url,
        data:{
            key:postparams.key,
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.beerer.asia') //加密用
        }
    })
}