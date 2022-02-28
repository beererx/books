from pymysql import connect
from pymysql.cursors import DictCursor
from settings import MYSQL_HOST, MYSQL_USER, MYSQL_PASS, MYSQL_DB, MYSQL_PORT


class Book(object):
    def __init__(self):
        self.conn = connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASS,
            db=MYSQL_DB,
            charset="utf8",
            port=MYSQL_PORT
        )
        self.cursor=self.conn.cursor(DictCursor)

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def get_cates_new_books_30(self, book_cate):
        sql = "SELECT id,book_id,book_name,book_last_update_time,book_newest_name," \
              "book_newest_url FROM book_infos WHERE book_cate = '{}' " \
              "ORDER BY book_last_update_time DESC LIMIT 30".format(book_cate)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data

    def get_cates_most_books_30(self, book_cate):
        data = []
        sql = "SELECT id,book_id,book_name,book_author,book_newest_url FROM book_infos " \
              "WHERE book_cate = '{}' ORDER BY book_newest_url DESC LIMIT 40".format(book_cate)
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data

    def get_book_infos_by_book_id(self, book_id):
        data = []
        sql = "SELECT * FROM book_infos WHERE book_id = '{}'".format(book_id)
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data

    def get_book_all_chapter_by_book_id(self, book_id):
        data = []
        sql = "SELECT id,book_id,sort_id,detail_title FROM book_details " \
              "WHERE book_id= '{}' ORDER BY sort_id".format(book_id)
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data

    def get_book_20_chapter_by_book_id(self, book_id):
        data = []
        sql = "SELECT id,book_id,sort_id,detail_title FROM book_details " \
              "WHERE book_id= '{}' ORDER BY sort_id DESC LIMIT 20".format(book_id)
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data

    def get_book_datail_by_book_id_sort_id(self, book_id, sort_id):
        data = []
        sql = "SELECT * FROM book_details WHERE book_id = '{}' AND sort_id = '{}'".format(book_id,sort_id)
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data

    def get_next_cap_id(self, book_id, sort_id):
        sql = "SELECT sort_id FROM book_details WHERE book_id = '{}' AND sort_id > '{}' ORDER BY" \
              " sort_id LIMIT 1".format(book_id, sort_id)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_front_cap_id(self, book_id, sort_id):
        sql = "SELECT sort_id FROM book_details WHERE book_id = '{}' AND sort_id < '{}' ORDER BY" \
              " sort_id DESC LIMIT 1".format(book_id, sort_id)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def search_books_by_key(self, key):
        data = []
        sql = "SELECT * FROM book_infos WHERE book_name  LIKE '%%{}%%' OR book_author LIKE '%%{}%%'".format(key, key)
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data

    def get_books_by_random(self):
        sql = "SELECT id,book_id,book_name,image_urls,book_author,book_desc,book_status FROM book_infos ORDER BY RAND() LIMIT 30"
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data


if __name__ == '__main__':
    book = Book()
    data = book.get_books_by_random()
    print(data)