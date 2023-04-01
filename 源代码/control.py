from Rules import Rule
from check import Check
from Rules import db


# 控制程序
# 控制推理机进行推理
class Control:
    # 开始正向推理匹配
    def identify1(self):
        # 建立游标
        cursor = db.cursor()
        # sql命令获取事实库与知识库
        sql0 = "SELECT MAX(RE_ID) FROM RECORD"
        try:
            cursor.execute(sql0)
        except Exception as e:
            print("查找事实库最大ID出错！")
            # 发生错误时回滚
            db.rollback()
            print("执行MySQL: %s 时出错：%s" % (sql0, e))
        max_id = cursor.fetchone()[0]  # 获取当前的最大ID
        sql1 = "SELECT * FROM RECORD WHERE RE_ID = %d" % max_id
        sql2 = "SELECT * FROM RULES"
        # 规则类对象列表
        rules = []
        # ans保存推理得到的结论
        ans = []

        try:
            cursor.execute(sql1)
            facts = cursor.fetchone()[1].split('/') # 获取事实库，你新输入的那些事实
            cursor.execute(sql2)
            rule_all = cursor.fetchall()  # 获取规则库，所有规则
            cursor.close()
            for rule in rule_all:
                r = Rule()
                r.set_condition(rule[2].split('/'))
                r.set_is_use(0)  # 表示该规则还没有匹配
                r.set_result(rule[1])
                rules.append(r)  # 存放各规则类对象

            # 建立匹配类的对象
            check = Check()
            # flag1判断每一轮匹配有没有匹配成功
            flag1 = 0
            # 遍历规则库
            while True:
                for r in rules:  # r代表一个规则对象
                    if r.get_is_use() == 0:
                        r.set_is_use(1)  # 匹配成功，标注该规则已匹配过
                        if check.check_rule1(facts, r.get_condition()) == 1:
                            facts.append(r.get_Result())  # 将结论加入事实库
                            condition = r.get_condition()  # 获取规则r的前提条件
                            # 保存中间推理过程，列表
                            temp = []
                            for i in range(len(condition)):  # 遍历condition中的每个特征
                                if condition[i] != '':
                                    temp.append(condition[i])
                            temp.append(r.get_Result())
                            ans.append(temp)
                            flag1 = 1
                            break  # 每一次匹配到一个规则后，讲结论加入事实库，break跳出for循环
                if flag1 == 0:  # for循环结束，flag1仍为0，说明没有一条规则匹配，故
                    break
                flag1 = 0  # 再令flag1=0，开始新一轮的for循环遍历规则库，继续推理，比如第一轮遍历推出是车，然后将车加入事实库

        except Exception as e:
            print("获取事实库出错！")
            # 发生错误时回滚
            db.rollback()
            print("执行MySQL1: %s或执行MySQL2 : %s 时出错：%s" % (sql1, sql2, e))
        # 返回结论，可能有多条
        return ans

    # 开始逆向推理匹配
    def identify2(self):
        # 建立游标
        cursor = db.cursor()
        # sql命令获取事实库与知识库
        sql0 = "SELECT MAX(RE_ID) FROM RECORD"
        try:
            cursor.execute(sql0)
        except Exception as e:
            print("查找事实库最大ID出错！")
            # 发生错误时回滚
            db.rollback()
            print("执行MySQL: %s 时出错：%s" % (sql0, e))
        max_id = cursor.fetchone()[0]  # 获取当前的最大ID
        sql1 = "SELECT * FROM RECORD WHERE RE_ID = %d" % max_id
        sql2 = "SELECT * FROM RULES"
        # 规则类对象列表
        rules = []
        # ans保存推理得到的结论
        ans = []

        try:
            cursor.execute(sql1)
            facts = list(cursor.fetchone()[1])  # 获取事实库，你新输入的那些事实
            cursor.execute(sql2)
            rule_all = cursor.fetchall()  # 获取规则库，所有规则
            cursor.close()
            for rule in rule_all:
                r = Rule()
                r.set_condition(rule[2].split('/'))
                r.set_is_use(0)  # 表示该规则还没有匹配
                r.set_result(rule[1])
                rules.append(r)  # 存放各规则类对象

            # 建立匹配类的对象
            check = Check()
            # flag1判断每一轮匹配有没有匹配成功
            flag1 = 0
            # 遍历规则库
            while True:
                for r in rules:  # r代表一个规则对象
                    if r.get_is_use() == 0:
                        r.set_is_use(1)  # 匹配成功，标注该规则已匹配过
                        result = r.get_Result()  # 获取规则r的结论
                        if check.check_rule2(facts, result) == 1:
                            condition = r.get_condition()
                            for i in range(len(condition)):  # 遍历condition中的每个特征
                                if condition[i] != '':  # 如果condition[i]不为空，就加入facts中
                                    facts.append(condition[i])  # 将前提条件加入事实库
                            # 保存中间推理过程，列表
                            temp = list(result)
                            temp.extend(condition)
                            ans.append(temp)
                            flag1 = 1  # flag=1表明已匹配成功
                            break  # 每一次匹配到一个规则后，讲结论加入事实库，break跳出for循环
                if flag1 == 0:  # for循环结束，flag1仍为0，说明没有一条规则匹配，故跳出while循环，返回空的ans
                    break
                flag1 = 0  # 再令flag1=0，开始新一轮的for循环遍历规则库，继续推理，比如第一轮遍历推出是车，然后将车加入事实库

        except Exception as e:
            print("获取事实库出错！")
            # 发生错误时回滚
            db.rollback()
            print("执行MySQL1: %s或执行MySQL2 : %s 时出错：%s" % (sql1, sql2, e))
        # 返回结论，可能有多条
        return ans
