import { JSEncrypt } from "jsencrypt";

export function rsaEncrypt(data){
    console.log("in RSA data = ", data);
    const publicKey = `MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDX4xWFRZf94t0pxcyPre79qe/tAmSiKGGp9yy9jq3pdLeHpRvEqALKPWXjcyvPYzcosFfn50KXFrgTo/7+Mcs5PiTog610YZN0Q8jI0KLYfrOpIyBJjjldDDXsuo6I1gpkTMX45805Er9SUNTNViafuY8RwrGidqRglzUiRmwI/QIDAQAB`;
    const jse = new JSEncrypt();
    jse.setPublicKey(publicKey);
    const result = jse.encrypt(data);
    console.log("in RSA result = ", result);
    return result
}