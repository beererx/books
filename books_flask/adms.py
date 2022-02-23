from pymysql import connect
from pymysql.cursors import DictCursor
from settings import MYSQL_HOST, MYSQL_USER, MYSQL_PASS, MYSQL_DB, MYSQL_PORT
class Adms(object):
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

    def sign_in_by_adm(self, name, password):
        data = []
        sql = "SELECT * FROM administrators WHERE adm_name = '{}'".format(name)
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            data.append(temp)
        if (data != []):
            already_name = data[0]["adm_name"]
            already_password = data[0]["adm_password"]
            adm_id = data[0]["adm_id"]
        else:
            return "no_user"
        if(name == already_name and password == already_password):
            return adm_id
        else:
            return "error_password"

    def get_name_by_adm(self, id):
        data = []
        sql = "SELECT * FROM administrators WHERE adm_id = '{}'".format(id)
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            data.append(temp)
        if (data != []):
            return data[0]
        else:
            return None

    def change_password(self, name, password, newpassword1, newpassword2):
        data = []
        sql = "SELECT adm_name,adm_password FROM administrators WHERE adm_name = '{}'".format(name)
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            data.append(temp)
        if (data != []):
            name = data[0]["adm_name"]
            oldpassword = data[0]["adm_password"]
        else:
            return "no_user"
        if password != oldpassword:
            return "error_password"
        if newpassword1 == newpassword2:
            if oldpassword != newpassword1:
                sql2 = "UPDATE administrators SET adm_password='{}' WHERE adm_name = '{}'".format(newpassword1, name)
                self.cursor.execute(sql2)
            else:
                return "no_change"
        else:
            return "atypism"
        self.conn.commit()
        return "ok"

    def get_all_data(self):
        push = []
        all_data = {}
        self.cursor.execute("explain select * from users;")
        data = self.cursor.fetchall()
        user = data[0]["rows"]
        all_data['user'] = user
        self.cursor.execute("explain select * from administrators;")
        data = self.cursor.fetchall()
        administrators = data[0]["rows"]
        all_data['administrators'] = administrators
        self.cursor.execute("explain select * from book_details;")
        data = self.cursor.fetchall()
        book_details = data[0]["rows"]
        all_data['book_details'] = book_details
        self.cursor.execute("explain select * from book_infos;")
        data = self.cursor.fetchall()
        book_infos = data[0]["rows"]
        all_data['book_infos'] = book_infos
        push.append(all_data)
        return push

    def get_all_data_for_books_infos(self):
        sql = "SELECT book_id,book_cate,book_name,book_author,book_status,book_last_update_time,book_desc FROM book_infos"
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data

    def change_all_data_for_books_infos(self, name, author, status, cate, desc, id):
        sql = "UPDATE book_infos SET book_name = '{}' ,book_cate='{}',book_author='{}',book_status='{}',book_desc='{}'" \
              " WHERE book_id = '{}'".format(name, cate, author, status, desc, id)
        self.cursor.execute(sql)
        self.conn.commit()
        return "ok"

    def create_all_data_for_books_infos(self, id, name, author, status, cate, desc):
        sql = "INSERT INTO book_infos(book_id,book_cate,book_name,image_urls,book_author,book_status,book_desc)" \
              "VALUES('{}','{}','{}','https://www.biquge.com.cn/files/article/image/45/45215/45215s.jpg'," \
              "'{}','{}','{}')".format(id, cate, name, author, status, desc)
        self.cursor.execute(sql)
        self.conn.commit()
        return "ok"

    def get_all_data_for_books_details(self):
        sql = "SELECT a.book_id,book_name,sort_id,detail_title,detail_content FROM" \
              " book_details as a,book_infos as b WHERE a.book_id=b.book_id LIMIT 500"
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data

    def change_all_data_for_books_detail(self, detail_title, detail_content, sort_id, book_id):
        sql = "UPDATE book_details SET detail_title = '{}',detail_content = '{}' WHERE sort_id = '{}' " \
              "AND book_id = '{}'".format(detail_title, detail_content, sort_id, book_id)
        self.cursor.execute(sql)
        self.conn.commit()
        return "ok"

    def judge_book_name(self, book_id, book_name):
        sql = "SELECT book_name FROM book_infos WHERE book_id = '{}'".format(book_id)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            data.append(temp)
        if (data != []):
            name = data[0]["book_name"]
            if(book_name == name):
                return "ok"
            else:
                return "error_bookname"
        else:
            return "no_book"

    def create_all_data_for_books_details(self, book_id, sort_id, detail_title, detail_content):
        sql = "INSERT INTO book_details(book_id,sort_id,detail_title,detail_content)" \
              "VALUES('{}','{}','{}','{}')".format(book_id, sort_id, detail_title, detail_content)
        self.cursor.execute(sql)
        self.conn.commit()
        return "ok"

    def get_all_data_for_users(self):
        sql = "SELECT user_name,user_mail,signin,dlevel,last_signed FROM users"
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data

    def get_book_cate_num(self):
        sql = "SELECT book_cate,COUNT(book_cate) AS num FROM book_infos GROUP BY book_cate"
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            data.append(temp)
        data[0]['book_cate'] = '都市'
        data[1]['book_cate'] = '科幻'
        data[2]['book_cate'] = '历史'
        data[3]['book_cate'] = '其他'
        data[4]['book_cate'] = '全本'
        data[5]['book_cate'] = '网游'
        data[6]['book_cate'] = '修真'
        data[7]['book_cate'] = '玄幻'
        data[8]['book_cate'] = '言情'
        return data


if __name__ == '__main__':
    adm = Adms()
    #data = user.sign_in("xiaom", "1234567323")
    data = adm.get_book_cate_num()
    #data = adm.sign_in_by_adm("rr1", "11111")
    #data = adm.create_all_data_for_books_details(8888,88,'xx','aaa')
    print(data)