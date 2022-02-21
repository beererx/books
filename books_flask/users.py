from pymysql import connect
from pymysql.cursors import DictCursor
from settings import MYSQL_HOST, MYSQL_USER, MYSQL_PASS, MYSQL_DB, MYSQL_PORT
import time

class User(object):
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

    def registered_user(self, name, email, password):
        data = []
        already_name = None
        sql = "SELECT user_name FROM users WHERE user_name = '{}'".format(name)
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            data.append(temp)
        if(data != []):
            already_name = data[0]["user_name"]
        if(name == already_name):
            return "no"
        sql2 = "INSERT INTO users (user_name,user_mail,user_password,signin,dlevel,last_signed) " \
              "VALUES('{}','{}','{}',0,0,'2000/1/1')".format(name, email, password)
        self.cursor.execute(sql2)
        self.conn.commit()
        return "ok"

    def sign_in(self, name, password):
        data = []
        sql = "SELECT user_name,user_password FROM users WHERE user_name = '{}'".format(name)
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            data.append(temp)
        if (data != []):
            already_name = data[0]["user_name"]
            already_password = data[0]["user_password"]
        else:
            return "no_user"
        if(name == already_name and password == already_password):
            return "ok"
        else:
            return "error_password"

    def get_user_infos(self, name):
        data = []
        user = {}
        sql = "SELECT * FROM users WHERE user_name = '{}'".format(name)
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            data.append(temp)
        if (data != []):
            user['user_id'] = data[0]["user_id"]
            user['user_name'] = data[0]["user_name"]
            user['signin'] = data[0]["signin"]
            user['dlevel'] = data[0]["dlevel"]
        else:
            return "error"
        return user

    def push_signin(self, name):
        data = []
        sql = "SELECT signin, dlevel, last_signed FROM users WHERE user_name = '{}'".format(name)
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            data.append(temp)
        signin = data[0]["signin"]
        last_signed = data[0]["last_signed"]
        dlevel = data[0]["dlevel"]
        lasttime = last_signed.timestamp()
        nowtime = time.time()
        localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        time_difference = nowtime - lasttime
        if(time_difference <86400):
            return "less_time"
        else:
            signin = signin+1
            grade = signin/10
            if(grade > dlevel):
                dlevel = dlevel+1
        sql2 = "UPDATE users SET signin='{}', dlevel='{}',last_signed = '{}' WHERE user_name = '{}'".\
            format(signin, dlevel, localtime, name)
        self.cursor.execute(sql2)
        self.conn.commit()
        return "ok"

if __name__ == '__main__':
    user = User()
    #data = user.sign_in("xiaom", "1234567323")
    data = user.push_signin("xiaom")
    print(data)