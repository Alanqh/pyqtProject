import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="qwerty123456", database="动物识别系统")


# 规则类
class Feature:

    # 展示所有特征函数
    def display_feature(self):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "SELECT * FROM FEATURES"
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            cursor.close()
            # 执行完毕 返回结果
            return results
        except:
            print("Error: unable to fetch data")

    # 查找特征函数
    def get_features(self, index):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        sql = "SELECT * FROM FEATURES \
               WHERE F_ID = %s" % index
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            cursor.close()
            return results
        except:
            print("Error: unable to fetch data")
