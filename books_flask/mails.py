import yagmail
import random
from pymysql import connect
from pymysql.cursors import DictCursor
from settings import MYSQL_HOST, MYSQL_USER, MYSQL_PASS, MYSQL_DB, MYSQL_PORT
import time


class Mail(object):
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

    def create_random(self, postmail):
        random_num = random.randint(100000, 999999)
        sql = "INSERT INTO verification(verification_mail,verification_random,verification_time)" \
              "VALUES('{}','{}',NOW())".format(postmail, random_num)
        self.cursor.execute(sql)
        self.conn.commit()
        return random_num

    def post_email(self, postmail, random_num):
        try:
            yagmail_server = yagmail.SMTP(user="2426758235@qq.com", password="gegoqfwoxfugebfg", host="smtp.qq.com")
            email_name = [postmail]
            email_title = ["小说网站验证码"]
            email_content = ["您的验证码是"+str(random_num)+"上述验证码30分钟内有效，如失效，请您重新申请发送邮箱验证码进行验证。"]
            yagmail_server.send(to=email_name, subject=email_title, contents=email_content)
            yagmail_server.close()
            return "ok"
        except:
            sql = "DELETE FROM verification WHERE verification_mail = '{}'".format(postmail)
            self.cursor.execute(sql)
            self.conn.commit()
            return "no"

    def random_judge(self, postmail, random_num):
        data = []
        sql = "SELECT verification_random,verification_time FROM verification WHERE verification_mail = '{}' " \
              "ORDER BY verification_time DESC LIMIT 1".format(postmail)
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            data.append(temp)
        if(data != []):
            verification_random = data[0]["verification_random"]
            verification_time = data[0]["verification_time"]
        else:
            return "no_email"
        judgetime = verification_time.timestamp()
        nowtime = time.time()
        time_difference = nowtime-judgetime
        if time_difference < 1800 and random_num == verification_random:
            return "ok"
        else:
            return "no"


if __name__ == '__main__':
    mail = Mail()
    #mail.post_email(123456)
    #mail.create_random("2856235527@qq.com")
    print(mail.random_judge("2856235527@qq.com", "311951"))
