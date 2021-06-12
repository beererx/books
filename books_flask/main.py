from flask import Flask,jsonify
from books import Book

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hell_world():
    book = Book()
    arrData = book.get_books_infos_limit()
    print(arrData)
    return jsonify(arrData)

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
        "message": '对本次请求的说明'
    }
    return jsonify(resData)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8088,debug=True)
