from flask import request, jsonify, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from adms import Adms
import functools
Privatekey = "beerer"


def create_token(adm_id):
    s = Serializer(Privatekey, expires_in=3600)
    token = s.dumps({"id": adm_id}).decode("ascii")
    return token


def verify_token(token):
    s = Serializer(Privatekey)
    try:
        data = s.loads(token)
    except Exception:
        return None
    adm = Adms()
    user = adm.get_name_by_adm(data["id"])
    return user


def login_required(view_func):
    @functools.wraps(view_func)
    def verify_token(*args, **kwargs):
        try:
            token = request.headers["Authorization"]
        except Exception:
            resData = {
                "resCode": 777,
                "data": [],
                "message": '缺少参数token'
            }
            return jsonify(resData)
        s = Serializer(Privatekey)
        try:
            s.loads(token)
        except Exception:
            resData = {
                "resCode": 777,
                "data": [],
                "message": '登录已过期'
            }
            return jsonify(resData)
        return view_func(*args, **kwargs)
    return verify_token

