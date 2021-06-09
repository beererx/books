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

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8088,debug=True)
