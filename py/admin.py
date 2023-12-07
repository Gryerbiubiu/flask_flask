"""
# -*- coding:utf-8 -*-
# 高高快乐每一天！#
# @File : admin.py
# @Time : 2023/11/21 21:15
"""


# 模拟用户数据存储在txt文件中
def check_admin_credentials(username, password):
    with open('user_txt/gaogao.txt', 'r') as file:
        for line in file:
            if f'Username: {username}, Password: {password}' in line:
                return True
    return False



























    return user_list
