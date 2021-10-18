from flask import Flask, jsonify, request
from books import Book
import json
from settings import BOOK_LIST, RSA_1024_PRIV_KEY, REQUEST_LISTS, TITLES
import re
import rsa
import base64
import time
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

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8088,debug=True)
