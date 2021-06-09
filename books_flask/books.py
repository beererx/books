from pymysql import connect
from pymysql.cursors import DictCursor
from settings import MYSQL_HOST,MYSQL_USER,MYSQL_PASS,MYSQL_DB,MYSQL_PORT
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

    def get_books_infos_limit(self):
        sql = 'SELECT * FROM book_infos LIMIT 3'
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            #print(temp)
            data.append((temp))
        return data