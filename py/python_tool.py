"""
# -*- coding:utf-8 -*-
# 高高快乐每一天！#
# @File : python_tool.py
# @Time : 2023/11/24 21:04
"""
# python_code.py
import csv

def write_to_csv(data, filename):
    """
    import csv
    参数:
    - data: 要写入的数据，以字典形式表示
    - filename: 要写入的CSV文件名
    - 可套入循环追加填写，不会被顶替
    """
    with open(filename, 'a', newline='', encoding='utf_8_sig') as csvfile:
        fieldnames = data.keys()  # 获取字典的键作为CSV文件的列名
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 检查文件是否已存在，如果不存在，则写入标题行
        if csvfile.tell() == 0:
            writer.writeheader()  # 写入CSV文件的标题行
        # 写入数据
        writer.writerow(data)
