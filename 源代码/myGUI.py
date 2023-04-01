import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from ttkbootstrap import Style

from Features import Feature
from Rules import Rule
from Rules import db
from control import Control


class Window:
    def __init__(self, root):

        # 创建主窗口
        self.root = root
        self.root.title("动物识别系统")
        width = 1000  # 宽度
        height = 600  # 高度
        align_str = '%dx%d' % (width, height)
        root.geometry(align_str)

        # 创建输入框
        label_input = tk.Label(root, text="请输入结果或事实:")
        label_input.grid(row=0, column=0, padx=10, pady=10)

        self.entry_input = tk.Entry(root, width=40, fg="gray")
        self.entry_input.insert(0, "请输入结果或事实，例如：有翅膀/鸟类")
        self.entry_input.grid(row=1, column=1, padx=10, pady=10)
        self.entry_input.bind("<FocusIn>", lambda event: self.on_entry_click(self.entry_input))

        # 显示特征库
        label_feature = tk.Label(root, text="特征库:", width=25, height=2)
        label_feature.grid(row=0, column=4, padx=10, pady=10)

        self.m = scrolledtext.ScrolledText(root, width=30, height=30, font=('黑体', 12), wrap=tk.WORD)
        self.m.place(x=650, y=60)  # 放置的位置
        self.gui_feature()

        # 显示展示框
        label_result = tk.Label(root, text="展示框:")
        label_result.grid(row=4, column=0, padx=10, pady=10)
        self.t = scrolledtext.ScrolledText(root, width=65, height=20, font=('黑体', 12), wrap=tk.WORD)
        self.t.place(x=100, y=200)  # 放置的位置

        # 创建按钮
        button_forward = tk.Button(root, text="正向推理", command=self.forward_inference)
        button_forward.grid(row=2, column=2, padx=10, pady=10)

        button_backward = tk.Button(root, text="逆向推理", command=self.backward_inference)
        button_backward.grid(row=2, column=3, padx=10, pady=10)

        button_view = tk.Button(root, text="查看规则", command=self.view_rules)
        button_view.grid(row=0, column=2, padx=10, pady=10)

        button_delete = tk.Button(root, text="删除规则", command=self.delete_window)
        button_delete.grid(row=1, column=3, padx=10, pady=10)

        button_modify = tk.Button(root, text="修改规则", command=self.modify_window)
        button_modify.grid(row=1, column=2, padx=10, pady=10)

        button_add = tk.Button(root, text="添加规则", command=self.add_window)
        button_add.grid(row=0, column=3, padx=10, pady=10)

        button_clear = tk.Button(root, text="一键清空", width=40, command=self.clear_all)
        button_clear.grid(row=2, column=1, padx=10, pady=10)

    # 定义输入框默认文本的清空函数
    def on_entry_click(self, entry):
        if entry.get() == "请输入结果或事实，例如：有翅膀/鸟类":
            entry.delete(0, "end")
            entry.config(fg="black")

    # 查看特征函数
    def gui_feature(self):
        self.m.delete(1.0, 'end')  # 清空文本框
        feature = Feature()
        results = feature.display_feature()  # 结果数据集

        for row in results:  # 遍历结果集中的每一行
            s = str(row[0]) + '：'  # row[0]表示规则表每行第一个字段，即id
            if row[1] != '':  # row[1]第二个字段 即特征1
                s += row[1]  # s中添加row[1]
            self.m.insert('end', s + "\n")  # m代表这个文本框

    # 记录用户的输入内容到综合数据库中
    def add_record(self):
        cursor = db.cursor()
        # 查找当前综合数据库最大ID
        sql = "SELECT MAX(RE_ID) FROM RECORD"
        try:
            cursor.execute(sql)
        except Exception as e:
            print("查找事实库最大ID出错！")
            # 发生错误时回滚
            db.rollback()
            print("执行MySQL: %s 时出错：%s" % (sql, e))
        max_id = cursor.fetchone()[0]  # 获取当前的最大ID
        max_id += 1
        # 将事实加入综合数据库
        if self.entry_input.get() != '':
            sql = "INSERT INTO RECORD(RE_ID, FACT) \
                                        VALUES (%d,'%s')" % (max_id, self.entry_input.get())
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 将操作提交到数据库中，否则数据库中数据不改变，增删改等sql语句后都要加这个方法
                cursor.close()
            except Exception as e:
                print("添加事实出错！")
                # 发生错误时回滚
                db.rollback()
                print("执行MySQL: %s 时出错：%s" % (sql, e))

    # 正向推理函数
    def forward_inference(self):
        self.t.delete(1.0, 'end')
        self.add_record()
        a = Control()
        ans = a.identify1()  # 推理过程函数，ans返回结论
        if not ans:
            self.t.insert('end', "无法识别！！！" + '\n')
        else:
            # lens_ans表示结论个数
            lens_ans = len(ans)
            for i in range(lens_ans):  # for i in range(2) 则i值为0,1
                if i != lens_ans - 1:
                    self.t.insert('end', "推理得到的中间结果：")
                else:
                    self.t.insert('end', "推理得到的最终结果：")
                lens_temp = len(ans[i])  # 每个结论列表的长度
                for j in range(lens_temp):  # 遍历结论列表中的每一项
                    if j == 0:  # 第一项直接输出
                        self.t.insert('end', ans[i][j])
                    elif j != lens_temp - 1:  # 后面的特征
                        self.t.insert('end', "+" + ans[i][j])
                    else:  # 输出结果，签名加上-->
                        self.t.insert('end', "-->" + ans[i][j] + '\n')

    # 逆向推理函数
    def backward_inference(self):
        self.t.delete(1.0, 'end')
        self.add_record()
        a = Control()
        ans = a.identify2()  # 推理过程函数，ans返回结论
        if not ans:
            self.t.insert('end', "无法识别！！！" + '\n')
        else:
            # lens_ans表示结论个数，ans是一个列表，里面装个各个结论列表
            lens_ans = len(ans)
            for i in range(lens_ans):  # for i in range(2) 则i值为0,1
                if lens_ans == 1:
                    break
                self.t.insert('end', "推理得到的中间结果：")
                lens_temp = len(ans[i])  # 每个结论（列表）的长度
                for j in range(lens_temp):  # 遍历结论列表中的每一项
                    if j == 0:  # 第一项直接输出
                        self.t.insert('end', ans[i][j] + "-->")
                    elif j != lens_temp - 1:  # 后面的特征
                        self.t.insert('end', ans[i][j] + "+")
                    else:  # 输出结果，前面加上-->
                        self.t.insert('end', ans[i][j] + '\n')
            self.t.insert('end', "推理得到的最终结果：")
            self.t.insert('end', ans[0][0] + "-->")
            result = []  # 建立一个结果的列表
            for i in range(lens_ans):
                result.append(ans[i][0])  # 它存放了所有可以进一步分解的事实
            # print(result)
            for i in range(lens_ans):
                lens_temp = len(ans[i])  # 保存每一条结论的字段数
                for j in range(lens_temp):  # 遍历每一条结论的每一个字段
                    if ans[i][j] not in result:  # 剔除掉可以进一步分解的事实
                        if i != lens_ans - 1 or j != lens_temp - 1:  # 如果不是最后一个，输出该事实 + '+'
                            self.t.insert('end', ans[i][j] + '+')
                        else:
                            self.t.insert('end', ans[i][j])  # 最后一个事实不需要再加'+'

    # 查看规则函数
    def view_rules(self):
        self.t.delete(1.0, 'end')  # 清空文本框
        rule = Rule()
        results = rule.display_rule()  # 结果数据集
        for row in results:  # 遍历结果集
            s = str(row[0]) + '：' + row[2] + '-->' + row[1]
            self.t.insert('end', s + "\n")  # self.t代表这个文本框

    # 修改规则函数
    def modify_window(self):

        def confirm():
            # 确认修改规则函数
            self.modify_rules(entry_id.get(), entry_condition.get(), entry_result.get())
            modify_window.destroy()

        # 打开新页面，输入要修改的规则ID、条件、结果，最后确认修改
        modify_window = tk.Toplevel()
        modify_window.title("修改规则")
        label_id = tk.Label(modify_window, text="规则ID:")
        label_id.grid(row=0, column=0, padx=10, pady=10)
        entry_id = tk.Entry(modify_window, width=40)
        entry_id.grid(row=0, column=1, padx=10, pady=10)
        label_condition = tk.Label(modify_window, text="条件:")
        label_condition.grid(row=1, column=0, padx=10, pady=10)
        entry_condition = tk.Entry(modify_window, width=40)
        entry_condition.grid(row=1, column=1, padx=10, pady=10)
        label_result = tk.Label(modify_window, text="结果:")
        label_result.grid(row=2, column=0, padx=10, pady=10)
        entry_result = tk.Entry(modify_window, width=40)
        entry_result.grid(row=2, column=1, padx=10, pady=10)
        button_confirm = tk.Button(modify_window, text="确认", command=confirm)
        button_confirm.grid(row=3, column=1, padx=10, pady=10)

    def modify_rules(self, r_id, conditions, result):
        # 建立游标
        cursor = db.cursor()
        # 查找该规则id是否存在
        if r_id != '':
            sql = "SELECT * FROM RULES WHERE R_ID = %s" % r_id
            cursor.execute(sql)
            if cursor.fetchone() is None:
                messagebox.showerror(title="规则不存在！", message="您要修改的规则编号不存在！请重新输入编号")
            else:
            # SQL 更新语句(修改)
                sql = "UPDATE RULES SET CONDITIONS='%s/'," \
                    "RESULT='%s' WHERE R_ID = %s" % (conditions, result, r_id)

            try:
                if conditions != '' and result != '':
                    cursor.execute(sql)
                    # 执行sql语句
                    db.commit()
                    messagebox.showinfo(title="修改成功！", message="规则已修改！请重新查看规则！")
                else:
                    messagebox.showerror(title="修改失败！", message="规则或结果为空")
                cursor.close()
            except Exception as e:
                print("修改规则出错！")
                # 发生错误时回滚
                db.rollback()
                print("执行MySQL: %s 时出错：%s" % (sql, e))
        else:
            messagebox.showerror(title="未输入编号！", message="请输入编号")
            cursor.close()

    # 添加规则函数
    def add_window(self):
        # 确认函数，确认后删除
        def confirm():
            self.add_rules(entry_condition.get(), entry_result.get())
            add_window.destroy()

        # 打开新页面，输入要添加的规则条件、结果，最后确认添加
        add_window = tk.Toplevel()
        add_window.title("添加规则")
        label_condition = tk.Label(add_window, text="条件:")
        label_condition.grid(row=1, column=0, padx=10, pady=10)
        entry_condition = tk.Entry(add_window, width=40)
        entry_condition.grid(row=1, column=1, padx=10, pady=10)
        label_result = tk.Label(add_window, text="结果:")
        label_result.grid(row=2, column=0, padx=10, pady=10)
        entry_result = tk.Entry(add_window, width=40)
        entry_result.grid(row=2, column=1, padx=10, pady=10)
        button_confirm = tk.Button(add_window, text="确认", command=confirm)
        button_confirm.grid(row=3, column=1, padx=10, pady=10)

    def add_rules(self, conditions, result):
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # 获取当前最大规则id
        sql = "SELECT MAX(R_ID) FROM RULES"
        cursor.execute(sql)
        max_id = cursor.fetchone()[0] + 1
        # SQL 插入语句
        sql = "INSERT INTO RULES(R_ID,RESULT,CONDITIONS) \
                   VALUES (%d,'%s','%s')" % \
              (max_id, result, conditions)
        try:
            if conditions != '' and result != '':
                cursor.execute(sql)
                # 执行sql语句
                db.commit()
                messagebox.showinfo(title="添加成功！", message="新规则已添加知识库！请重新查看规则！")
            else:
                messagebox.showerror(title="添加失败！", message="规则或结果为空")
            cursor.close()
        except Exception as e:
            print("添加规则出错！")
            # 发生错误时回滚
            db.rollback()
            print("执行MySQL: %s 时出错：%s" % (sql, e))

    # 删除规则函数
    def delete_window(self):

        def confirm():
            # 确认删除规则函数
            self.delete_rule(entry_id.get())
            # 关闭子页面
            delete_window.destroy()

        # 打开新页面，输入要删除的规则ID，最后确认删除
        delete_window = tk.Toplevel()
        delete_window.title("删除规则")
        label_id = tk.Label(delete_window, text="规则ID:")
        label_id.grid(row=0, column=0, padx=10, pady=10)
        entry_id = tk.Entry(delete_window, width=40)
        entry_id.grid(row=0, column=1, padx=10, pady=10)
        button_confirm = tk.Button(delete_window, text="确认", command=confirm)
        button_confirm.grid(row=1, column=1, padx=10, pady=10)

    def delete_rule(self, r_id):
        # 建立游标
        cursor = db.cursor()
        if r_id != '':
            # 查询删除的ID是否存在
            sql = "SELECT * FROM RULES WHERE R_ID = %s" % r_id
            # 执行SQL语句
            cursor.execute(sql)
            results = cursor.fetchone()
            if results is None:
                messagebox.showerror(title="删除的规则不存在", message="您选择删除的规则不存在，请重新输入！")
            else:
                # SQL 删除语句
                sql = "DELETE FROM RULES WHERE R_ID = %s" % r_id
                try:
                    # 执行SQL语句
                    cursor.execute(sql)
                    # 提交修改
                    db.commit()
                    messagebox.showinfo(title="删除成功！", message="删除成功！请重新查看规则！")
                    cursor.close()
                except Exception as e:
                    print("删除规则出错！")
                    # 发生错误时回滚
                    db.rollback()
                    print("执行MySQL: %s 时出错：%s" % (sql, e))
        else:
            messagebox.showerror(title="未输入编号！", message="请输入编号！")
            cursor.close()

    # 一键清空函数
    def clear_all(self):
        # 清空所有文本框
        if self.entry_input.get() != "请输入结果或事实，例如：有翅膀/鸟类":
            self.entry_input.delete(0, "end")
        self.t.delete('1.0', tk.END)

style = Style(theme='sandstone')
# 切换主题，修改theme值即可:
# ['vista', 'classic', 'cyborg', 'journal', 'darkly', 'flatly', 'clam']
# ['alt', 'solar', 'minty', 'litera', 'united', 'xpnative', 'pulse']
# ['cosmo', 'lumen', 'yeti', 'superhero', 'winnative', 'sandstone', 'default']
window = style.master
Window(window)
window.mainloop()
