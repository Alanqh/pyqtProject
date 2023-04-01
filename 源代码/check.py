# 用于推理匹配，检查规则库中是否有符合的知识
class Check:  # 正向推理

    def check_rule1(self, fact, rule_condition):
        for r in rule_condition:  # 对于每个rule的condition（列表）进行遍历，r即是各个特征，如陆地上跑、水上游等等
            if r not in fact:  # 如果该规则的前提条件中的有一个特征不在fact中，说明匹配失败 ，只有所有特征都在fact中，才算成功
                return 0  # 匹配失败
        return 1

    def check_rule2(self, fact, rule_result):  # 逆向推理
        if rule_result not in fact:
            return 0
        return 1
        # 如果事实库中的每个事实都不能与result匹配，返回0
