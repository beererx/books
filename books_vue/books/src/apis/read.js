import service from "../utils/request";


export function GetCates(){
    return service.request({
        url:"/books_cates",
        method:"get"
    });
}