"""
# -*- coding:utf-8 -*-
# 高高快乐每一天！#
# @File : register_and_login.py
# @Time : 2023/11/20 20:40
"""
import json


def read_json_file(file_path, class_count):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    categories = data["categories"]
    for category in categories:
        if category["name"] == class_count:
            return category["items"]


# json_data = read_json_file('../static/json/links.json','Python')
# print(json_data)


# 模拟用户数据存储在txt文件中
def check_user_credentials(username, password):
    with open('user_txt/user_data.txt', 'r') as file:
        for line in file:
            if f'Username: {username}, Password: {password}' in line:
                return True
    return False


# 从txt文件读取数据
def read_links_data(class_count):
    links_data = []
    if class_count == 0:
        with open("user_txt/python_links.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.split(',')
                if len(parts) == 2:
                    text = parts[0].strip()
                    url = parts[1].strip()
                    links_data.append({"text": text, "url": url})
        return links_data
    if class_count == 1:
        with open("user_txt/AI_links.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.split(',')
                if len(parts) == 2:
                    text = parts[0].strip()
                    url = parts[1].strip()
                    links_data.append({"text": text, "url": url})
        return links_data
    if class_count == 2:
        with open("user_txt/Special_links.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.split(',')
                if len(parts) == 2:
                    text = parts[0].strip()
                    url = parts[1].strip()
                    links_data.append({"text": text, "url": url})
        return links_data
    if class_count == 3:
        with open("user_txt/Data_links.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.split(',')
                if len(parts) == 2:
                    text = parts[0].strip()
                    url = parts[1].strip()
                    links_data.append({"text": text, "url": url})
        return links_data
