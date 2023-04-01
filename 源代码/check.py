# 用于推理匹配，检查规则库中是否有符合的知识
class Check:  # 正向推理

    def check_rule1(self, fact, rule):
        for r in rule:  # 对于每个rule的condition（列表）进行遍历，r即是各个特征，如陆地上跑、水上游等等
            if r != '':  # 有的规则可能会有几个前提条件为空如 ['','地上跑的','有轮子']
                if r not in fact:  # 如果该规则的前提条件中的有一个特征不在fact中，说明匹配失败 ，只有所有特征都在fact中，才算成功
                    return 0  # 匹配失败
        return 1

    def check_rule2(self, fact, result):  # 逆向推理
        for i in fact:  # i是事实库中的事实，依次判断i是否为result，如果是，就返回1
            if i != '':
                if i == result:
                    return 1
        return 0
        # 如果事实库中的每个事实都不能与result匹配，返回0
