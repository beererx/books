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

export function GetBookCateNum(postparams){
    return service.request({
        method:"post",
        url:"/adm/bookcate_num",
        data:{
            key:postparams.key,
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.beerer.asia') //加密用
        }
    })
}

export function LogininInfoPost(postparams){
    return service.request({
        method:"post",
        url:postparams.url,
        data:{
            email:postparams.email,
            name:postparams.name,
            passcode:postparams.passcode,
            password:postparams.password,
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.beerer.asia') //加密用
        }
    })
}

export function ChangeinInfoPost(postparams){
    return service.request({
        method:"post",
        url:postparams.url,
        data:{
            name:postparams.name,
            oldpassword:postparams.oldpassword,
            newpassword1:postparams.newpassword1,
            newpassword2:postparams.newpassword2,
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.beerer.asia') //加密用
        }
    })
}

export function ChangeBookInfoPost(postparams){
    return service.request({
        method:"post",
        url:postparams.url,
        data:{
            book_name:postparams.book_name,
            book_cate:postparams.book_cate,
            book_author:postparams.book_author,
            book_desc:postparams.book_desc,
            book_id:postparams.book_id,
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.beerer.asia') //加密用
        }
    })
}

export function ChangeBookDetailPost(postparams){
    return service.request({
        method:"post",
        url:postparams.url,
        data:{
            book_name:postparams.book_name,
            detail_content:postparams.detail_content,
            detail_title:postparams.detail_title,
            book_id:postparams.book_id,
            sort_id:postparams.sort_id,
            secretKey: rsaEncrypt(new Date().getTime()+':'+'www.beerer.asia') //加密用
        }
    })
}