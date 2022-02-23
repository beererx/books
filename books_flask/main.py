from flask import Flask, jsonify, request
from books import Book
from mails import Mail
from users import User
from adms import Adms
import json
from settings import BOOK_LIST, RSA_1024_PRIV_KEY, REQUEST_LISTS, TITLES
import re
import rsa
import base64
import time
from ttoken import create_token, login_required, verify_token
import random

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


# 检查是否含有特殊字符
def is_string_validate(str):
    sub_str = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",str)
    if len(str) == len(sub_str):
        # 合法
        return False
    else:
        # 不合法
        return True


# rsa解密
def get_secret_key(cryptdata):
    privkey = rsa.PrivateKey.load_pkcs1(RSA_1024_PRIV_KEY)
    msg = rsa.decrypt(base64.b64decode(cryptdata), privkey)
    try:
        result = {
            "request_time": msg.decode().split(":")[0],   #時間戳，防爬虫
            "request_url": msg.decode().split(":")[1]
        }
    except:
        result = {
            "request_time": '',  # 時間戳，防爬虫
            "request_url": ''
        }
    return result


@app.route('/')
def hell_world():
    abc = 'dsvv'
    return abc


#获取关键词
@app.route('/title', methods=['POST'])
def get_title_infos():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        resData = {
            "resCode": 0,
            "data": TITLES[secret_result['request_url']][key],
            "message": '首页关键词'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


@app.route('/books_cates', methods=['GET'])
def get_books_cates():
    resData = {
        "resCode": 0,
        "data": [
            {"id":0, "text": '首页', "url":'/'},
            {"id":1, "text": '玄幻', "url":'/xuanhuan'},
            {"id":2, "text": '修真', "url":'/xiuzhen'},
            {"id":3, "text": '都市', "url":'/dushi'},
            {"id":4, "text": '历史', "url":'/lishi'},
            {"id":5, "text": '网游', "url":'/wangyou'},
            {"id":6, "text": '科幻', "url":'/kehuan'},
            {"id":7, "text": '言情', "url":'/yanqing'},
            {"id":8, "text": '其他', "url":'/qita'},
            {"id":9, "text": '完本', "url":'/quanben'},
        ],
        "message": '头部'
    }
    return jsonify(resData)


#图书分类信息
@app.route('/<string:book_cate>', methods=['POST'])
def get_cates_infos(book_cate):
    if is_string_validate(book_cate):
        resData = {
            "resCode": 404,
            "data": [],
            "message": '输入有误'
        }
        return jsonify(resData)
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        if book_cate in BOOK_LIST:
            if key == 'new':
                book = Book()
                sql_data = book.get_cates_new_books_30(book_cate)
                resData = {
                    "resCode": 0,
                    "data": [sql_data],
                    "message": '最新的30本小说'
                }
                return jsonify(resData)
            elif key == 'most':
                book = Book()
                sql_data = book.get_cates_most_books_30(book_cate)
                resData = {
                    "resCode": 0,
                    "data": [sql_data],
                    "message": '最新的30本小说'
                }
                return jsonify(resData)
            else:
                resData = {
                    "resCode": 2,
                    "data": [],
                    "message": '输出参数错误'
                }
                return jsonify(resData)
        else:
            return 404

    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#图书首页信息
@app.route('/book/<int:book_id>',methods=['POST'])
def get_book_infos_by_id(book_id):
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        print(get_data)
        key = get_data['key']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        book = Book()
        sql_data = book.get_book_infos_by_book_id(book_id)
        if key == 'index':
            resData = {
                "resCode": 0,
                "data": [sql_data],
                "message": '小说详细介绍'
            }
            return jsonify(resData)
        elif key == 'new20':
            if len(sql_data) == 0:
                resData = {
                    "resCode": 5,
                    "data": [],
                    "message": '图书不存在'
                }
                return jsonify(resData)
            all_data = book.get_book_20_chapter_by_book_id(book_id)
            resData = {
                "resCode": 0,
                "data": all_data,
                "message": '图书最新20章节'
            }
            return jsonify(resData)
        elif key == 'all':
            if len(sql_data) == 0:
                resData = {
                    "resCode": 5,
                    "data": [],
                    "message": '图书不存在'
                }
                return jsonify(resData)
            all_data = book.get_book_all_chapter_by_book_id(book_id)
            resData = {
                "resCode": 0,
                "data": all_data,
                "message": '图书所有章节'
            }
            return jsonify(resData)
        else:
            resData = {
                "resCode": 2,
                "data": [],
                "message": '输出参数错误'
            }
            return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#获取图书详情页接口
@app.route("/book/<int:book_id>/<int:sort_id>", methods=['POST'])
def get_book_datail_infos(book_id,sort_id):
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        book = Book()
        sql_book_id_data = book.get_book_infos_by_book_id(book_id)
        if len(sql_book_id_data) == 0:
            resData = {
                "resCode": 5,
                "data": [],
                "message": '图书不存在'
            }
            return jsonify(resData)
        sql_detail_data = book.get_book_datail_by_book_id_sort_id(book_id,sort_id)
        sql_detail_data[0]['book_name'] = sql_book_id_data[0]['book_name']
        next_sort_id = book.get_next_cap_id(book_id,sort_id)
        if next_sort_id == None:
            sql_detail_data[0]['next_sort_id'] = ''
        else:
            sql_detail_data[0]['next_sort_id'] = next_sort_id['sort_id']
        front_sort_id = book.get_front_cap_id(book_id, sort_id)
        if front_sort_id == None:
            sql_detail_data[0]['front_sort_id'] = ''
        else:
            sql_detail_data[0]['front_sort_id'] = front_sort_id['sort_id']
        resData = {
            "resCode": 0,
            "data": sql_detail_data,
            "message": '章节信息'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#图书搜索接口
@app.route('/search', methods=['POST'])
def search_book():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        if is_string_validate(key):
            resData = {
                "resCode": 2,
                "data": [],
                "message": '参数错误'
            }
            return jsonify(resData)
        book = Book()
        search_data = book.search_books_by_key(key)
        if len(search_data) == 0:
            resData = {
                "resCode": 6,
                "data": [],
                "message": '查询无结果'
            }
            return jsonify(resData)
        resData = {
            "resCode": 0,
            "data": search_data,
            "message": '查询结果'
        }
        return jsonify(resData)

    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#用户验证码接口
@app.route('/login/in', methods=['POST'])
def push_verification():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        email = get_data['key']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)

        mail = Mail()
        random_num = mail.create_random(email)
        push_data = mail.post_email(email, random_num)
        if (push_data) == "ok":
            resData = {
                "resCode": 0,
                "data": "ok",
                "message": '发送成功'
            }
            return jsonify(resData)
        resData = {
            "resCode": 0,
            "data": "no",
            "message": '发送失败'
        }
        return jsonify(resData)

    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#用户注册接口
@app.route('/login/in/up', methods=['POST'])
def login_up():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        email = get_data['email']
        name = get_data['name']
        passcode = get_data['passcode']
        password = get_data['password']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)

        mail = Mail()
        user = User()
        legitimate = mail.random_judge(email, passcode)
        if(len(password)<8):
            resData = {
                "resCode": 0,
                "data": "short_password",
                "message": '密码过短'
            }
            return jsonify(resData)
        if(legitimate == "ok"):
            res = user.registered_user(name, email, password)
            if(res == "no"):
                resData = {
                    "resCode": 0,
                    "data": "no_name",
                    "message": '用户名已被占有'
                }
                return jsonify(resData)
            else:
                resData = {
                    "resCode": 0,
                    "data": "ok",
                    "message": '发送成功'
                }
                return jsonify(resData)
        elif(legitimate == "no_email"):
            resData = {
                "resCode": 0,
                "data": "no_email",
                "message": '邮箱未验证'
            }
            return jsonify(resData)
        else:
            resData = {
                "resCode": 0,
                "data": "no_code",
                "message": '验证码错误或超时'
            }
            return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#用户登录接口
@app.route('/login/in/in', methods=['POST'])
def login_in():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        name = get_data['name']
        password = get_data['password']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)

        user = User()
        res = user.sign_in(name, password)
        if(res == "ok"):
            resData = {
                "resCode": 0,
                "data": "ok",
                "message": '登录成功'
            }
            return jsonify(resData)
        elif(res == "no_user"):
            resData = {
                "resCode": 0,
                "data": "no_user",
                "message": '用户不存在'
            }
            return jsonify(resData)
        elif(res == "error_password"):
            resData = {
                "resCode": 0,
                "data": "error_password",
                "message": '密码错误'
            }
            return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#用户个人信息
@app.route('/user/<name>', methods=['POST'])
def get_user_infos(name):
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        user = User()
        sql_data = user.get_user_infos(name)
        resData = {
            "resCode": 0,
            "data": [sql_data],
            "message": '个人信息'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#用户签到
@app.route('/user/<name>/signin',methods=['POST'])
def push_sign_in(name):
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        user = User()
        sql_data = user.push_signin(name)
        resData = {
            "resCode": 0,
            "data": sql_data,
            "message": '个人信息'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#管理员登录接口
@app.route('/adm/login', methods=['POST'])
def login_in_by_adm():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        name = get_data['name']
        password = get_data['password']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        adm = Adms()
        res = adm.sign_in_by_adm(name, password)
        if (res == "no_user"):
            resData = {
                "resCode": 0,
                "data": "no_user",
                "message": '管理员账户不存在'
            }
            return jsonify(resData)
        elif (res == "error_password"):
            resData = {
                "resCode": 0,
                "data": "error_password",
                "message": '密码错误'
            }
            return jsonify(resData)
        else:
            token = create_token(res)
            resData = {
                "resCode": 0,
                "data": "ok",
                "message": '登录成功',
                "token": token
            }
            return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#管理员网站简介接口
@app.route('/adm/main', methods=['POST'])
def get_data_of_web():
    if request.method == 'POST':
        try:
            token = request.headers["Authorization"]
            jtoken = verify_token(token)
            if(jtoken == None):
                resData = {
                    "resCode": 777,
                    "data": [],
                    "message": '参数token错误'
                }
                return jsonify(resData)
        except Exception:
            resData = {
                "resCode": 777,
                "data": [],
                "message": '缺少参数token'
            }
            return jsonify(resData)
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        if is_string_validate(key):
            resData = {
                "resCode": 2,
                "data": [],
                "message": '参数错误'
            }
            return jsonify(resData)
        adm = Adms()
        data = adm.get_all_data()
        resData = {
            "resCode": 0,
            "data": data,
            "message": '网站简介'
        }
        return jsonify(resData)

    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#管理员书籍列表接口
@app.route('/adm/booksmana', methods=['POST'])
def get_data_for_books_infos():
    if request.method == 'POST':
        try:
            token = request.headers["Authorization"]
            jtoken = verify_token(token)
            if (jtoken == None):
                resData = {
                    "resCode": 777,
                    "data": [],
                    "message": '参数token错误'
                }
                return jsonify(resData)
        except Exception:
            resData = {
                "resCode": 777,
                "data": [],
                "message": '缺少参数token'
            }
            return jsonify(resData)
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        if is_string_validate(key):
            resData = {
                "resCode": 2,
                "data": [],
                "message": '参数错误'
            }
            return jsonify(resData)
        adm = Adms()
        data = adm.get_all_data_for_books_infos()
        resData = {
            "resCode": 0,
            "data": data,
            "message": '书籍简介'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#管理员书籍修改接口
@app.route('/adm/booksmana/up', methods=['POST'])
def change_data_for_books_infos():
    if request.method == 'POST':
        try:
            token = request.headers["Authorization"]
            jtoken = verify_token(token)
            if(jtoken == None):
                resData = {
                    "resCode": 777,
                    "data": [],
                    "message": '参数token错误'
                }
                return jsonify(resData)
        except Exception:
            resData = {
                "resCode": 777,
                "data": [],
                "message": '缺少参数token'
            }
            return jsonify(resData)
        get_data = json.loads(request.get_data(as_text=True))
        book_name = get_data['book_name']
        book_cate = get_data['book_cate']
        book_author = get_data['book_author']
        book_desc = get_data['book_desc']
        book_id = get_data['book_id']
        book_status = "连载中"
        if(book_cate == "quanben"):
            book_status = "完本"
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        adm = Adms()
        data = adm.change_all_data_for_books_infos(book_name, book_author, book_status, book_cate, book_desc, book_id)
        resData = {
            "resCode": 0,
            "data": data,
            "message": '小说简介修改'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#管理员书籍添加接口
@app.route('/adm/bookinsert/up', methods=['POST'])
def create_data_for_books_infos():
    if request.method == 'POST':
        try:
            token = request.headers["Authorization"]
            jtoken = verify_token(token)
            if(jtoken == None):
                resData = {
                    "resCode": 777,
                    "data": [],
                    "message": '参数token错误'
                }
                return jsonify(resData)
        except Exception:
            resData = {
                "resCode": 777,
                "data": [],
                "message": '缺少参数token'
            }
            return jsonify(resData)
        get_data = json.loads(request.get_data(as_text=True))
        book_name = get_data['book_name']
        book_cate = get_data['book_cate']
        book_author = get_data['book_author']
        book_desc = get_data['book_desc']
        book_id = get_data['book_id']
        book_status = "连载中"
        if(book_cate == "quanben"):
            book_status = "完本"
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        adm = Adms()
        data = adm.create_all_data_for_books_infos(book_id, book_name, book_author, book_status, book_cate, book_desc)
        resData = {
            "resCode": 0,
            "data": data,
            "message": '小说书籍添加'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#管理员章节列表接口
@app.route('/adm/bookdetailmana', methods=['POST'])
def get_data_for_books_details():
    if request.method == 'POST':
        try:
            token = request.headers["Authorization"]
            jtoken = verify_token(token)
            if(jtoken == None):
                resData = {
                    "resCode": 777,
                    "data": [],
                    "message": '参数token错误'
                }
                return jsonify(resData)
        except Exception:
            resData = {
                "resCode": 777,
                "data": [],
                "message": '缺少参数token'
            }
            return jsonify(resData)
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        if is_string_validate(key):
            resData = {
                "resCode": 2,
                "data": [],
                "message": '参数错误'
            }
            return jsonify(resData)
        adm = Adms()
        data = adm.get_all_data_for_books_details()
        resData = {
            "resCode": 0,
            "data": data,
            "message": '章节简介'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#管理员章节修改接口
@app.route('/adm/bookdetailmana/up', methods=['POST'])
def change_data_for_books_detail():
    if request.method == 'POST':
        try:
            token = request.headers["Authorization"]
            jtoken = verify_token(token)
            if(jtoken == None):
                resData = {
                    "resCode": 777,
                    "data": [],
                    "message": '参数token错误'
                }
                return jsonify(resData)
        except Exception:
            resData = {
                "resCode": 777,
                "data": [],
                "message": '缺少参数token'
            }
            return jsonify(resData)
        get_data = json.loads(request.get_data(as_text=True))
        book_name = get_data['book_name']
        book_id = get_data['book_id']
        sort_id = get_data['sort_id']
        detail_title = get_data['detail_title']
        detail_content = get_data['detail_content']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        adm = Adms()
        data = adm.change_all_data_for_books_detail(detail_title, detail_content, sort_id, book_id)
        resData = {
            "resCode": 0,
            "data": data,
            "message": '小说章节修改'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#管理员章节添加接口
@app.route('/adm/bookdetailinsert/up', methods=['POST'])
def create_data_for_books_detail():
    if request.method == 'POST':
        try:
            token = request.headers["Authorization"]
            jtoken = verify_token(token)
            if(jtoken == None):
                resData = {
                    "resCode": 777,
                    "data": [],
                    "message": '参数token错误'
                }
                return jsonify(resData)
        except Exception:
            resData = {
                "resCode": 777,
                "data": [],
                "message": '缺少参数token'
            }
            return jsonify(resData)
        get_data = json.loads(request.get_data(as_text=True))
        book_name = get_data['book_name']
        detail_content = get_data['detail_content']
        detail_title = get_data['detail_title']
        sort_id = get_data['sort_id']
        book_id = get_data['book_id']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        adm = Adms()
        judge = adm.judge_book_name(book_id, book_name)
        if(judge == "no_book"):
            resData = {
                "resCode": 0,
                "data": "no_book",
                "message": '书籍不存在'
            }
            return jsonify(resData)
        elif(judge == "error_bookname"):
            resData = {
                "resCode": 0,
                "data": "error_bookname",
                "message": '书籍id与书籍名不匹配'
            }
            return jsonify(resData)
        else:
            data = adm.create_all_data_for_books_details(book_id, sort_id, detail_title, detail_content)
            resData = {
                "resCode": 0,
                "data": data,
                "message": '小说章节添加'
            }
            return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#管理员用户列表接口
@app.route('/adm/usercollect', methods=['POST'])
def get_data_for_user():
    if request.method == 'POST':
        try:
            token = request.headers["Authorization"]
            jtoken = verify_token(token)
            if(jtoken == None):
                resData = {
                    "resCode": 777,
                    "data": [],
                    "message": '参数token错误'
                }
                return jsonify(resData)
        except Exception:
            resData = {
                "resCode": 777,
                "data": [],
                "message": '缺少参数token'
            }
            return jsonify(resData)
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        if is_string_validate(key):
            resData = {
                "resCode": 2,
                "data": [],
                "message": '参数错误'
            }
            return jsonify(resData)
        adm = Adms()
        data = adm.get_all_data_for_users()
        resData = {
            "resCode": 0,
            "data": data,
            "message": '用户列表'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)


#管理员密码修改接口
@app.route('/adm/passchage', methods=['POST'])
def change_password_by_adm():
    if request.method == 'POST':
        try:
            token = request.headers["Authorization"]
            jtoken = verify_token(token)
            if(jtoken == None):
                resData = {
                    "resCode": 777,
                    "data": [],
                    "message": '参数token错误'
                }
                return jsonify(resData)
        except Exception:
            resData = {
                "resCode": 777,
                "data": [],
                "message": '缺少参数token'
            }
            return jsonify(resData)
        get_data = json.loads(request.get_data(as_text=True))
        name = get_data['name']
        oldpassword = get_data['oldpassword']
        newpassword1 = get_data['newpassword1']
        newpassword2 = get_data['newpassword2']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)

        adm = Adms()
        res = adm.change_password(name, oldpassword, newpassword1, newpassword2)
        if (res == "ok"):
            resData = {
                "resCode": 0,
                "data": "ok",
                "message": '密码修改成功'
            }
            return jsonify(resData)
        elif (res == "no_user"):
            resData = {
                "resCode": 0,
                "data": "no_user",
                "message": '管理员账户不存在'
            }
            return jsonify(resData)
        elif (res == "no_change"):
            resData = {
                "resCode": 0,
                "data": "no_change",
                "message": '密码相同'
            }
            return jsonify(resData)
        elif (res == "error_password"):
            resData = {
                "resCode": 0,
                "data": "error_password",
                "message": '原密码错误'
            }
            return jsonify(resData)
        elif (res == "atypism"):
            resData = {
                "resCode": 0,
                "data": "atypism",
                "message": '密码不一致'
            }
            return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)

#管理员用户列表接口
@app.route('/adm/bookcate_num', methods=['POST'])
def get_book_cate_num():
    if request.method == 'POST':
        try:
            token = request.headers["Authorization"]
            jtoken = verify_token(token)
            if(jtoken == None):
                resData = {
                    "resCode": 777,
                    "data": [],
                    "message": '参数token错误'
                }
                return jsonify(resData)
        except Exception:
            resData = {
                "resCode": 777,
                "data": [],
                "message": '缺少参数token'
            }
            return jsonify(resData)
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']
        secretKey = get_data['secretKey']
        secret_result = get_secret_key(secretKey)
        if secret_result['request_time'] == '':
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if (int(time.time() * 1000) - int(secret_result['request_time']) > 300000):
            resData = {
                "resCode": 101,
                "data": [],
                "message": '超時'
            }
            return jsonify(resData)
        if secret_result['request_url'] not in REQUEST_LISTS:
            resData = {
                "resCode": 102,
                "data": [],
                "message": '参数不存在'
            }
            return jsonify(resData)
        if is_string_validate(key):
            resData = {
                "resCode": 2,
                "data": [],
                "message": '参数错误'
            }
            return jsonify(resData)
        adm = Adms()
        data = adm.get_book_cate_num()
        resData = {
            "resCode": 0,
            "data": data,
            "message": '各类型小说数量'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode": 1,
            "data": [],
            "message": '请求方法错误'
        }
        return jsonify(resData)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8088, debug=True)
