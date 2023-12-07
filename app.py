# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, session, redirect, url_for
import secrets
from py import register_and_login, admin

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # 16 bytes = 32 characters
# 假设这里有一些其他数据
data_to_display = {
    'info1': 'Some information 1',
    'info2': 'Some information 2',
    'info3': 'Some information 3',
}

# 假设这里有一些其他数据
data_to_display_yi = {
    'info1': 'Some information 1',
    'info2': 'Some information 2',
    'info3': 'Some information 3',
}


# 主页路由
@app.route('/')
def index():
    python_links = register_and_login.read_json_file('static/json/links.json',"Python")
    ai_links = register_and_login.read_json_file('static/json/links.json', "AI")
    special_links = register_and_login.read_json_file('static/json/links.json', "Special")
    data_links = register_and_login.read_json_file('static/json/links.json', "Data")
    # print(links_data)
    return render_template('index.html', logged_in=session.get('logged_in'), data=data_to_display,
                           python_links=python_links, ai_links=ai_links, special_links=special_links,
                           data_links=data_links)


# 注册路由
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 获取注册表单数据
        username = request.form.get('username')
        password = request.form.get('password')

        # 将注册信息写入文本文件（以追加方式）
        with open('user_txt/user_data.txt', 'a') as file:
            file.write(f'Username: {username}, Password: {password}\n')

        # 注册成功后直接跳转到主页面
        session['logged_in'] = True
        session['username'] = username
        return redirect(url_for('index'))
    else:
        # 如果是GET请求，返回注册页面
        return render_template('register.html')


# 登录路由
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 获取登录表单数据
        username = request.form.get('username')
        password = request.form.get('password')

        # 检查用户凭据
        if register_and_login.check_user_credentials(username, password):
            session['logged_in'] = True
            session['username'] = username  # 将用户名存储在session中
            return redirect(url_for('index'))
        else:
            return '登录失败，请检查用户名和密码。'
    else:
        # 如果是GET请求，返回登录页面
        return render_template('login.html')


# 退出路由
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))


# 管理员登录路由
@app.route('/yilogin', methods=['GET', 'POST'])
def yilogin():
    if request.method == 'POST':
        # 获取登录表单数据
        username = request.form.get('username')
        password = request.form.get('password')

        # 检查用户凭据
        if admin.check_admin_credentials(username, password):
            session['admin_logged_in'] = True
            session['username'] = username  # 将用户名存储在session中
            return redirect(url_for('gaogao'))
        else:
            return '登录失败，请检查用户名和密码。'
    else:
        # 如果是GET请求，返回登录页面
        return render_template('gaogao_login.html', logged_in=session.get('admin_logged_in'), data=data_to_display)


# 管理员页面路由
@app.route('/gaogao')
def gaogao():
    # 读取用户数据并传递给模板
    with open('user_txt/user_data.txt', 'r') as file:
        users = [line.strip() for line in file]

    return render_template('gaogao.html', users=users)


# 添加用户路由
@app.route('/gaogao/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        # 获取表单数据
        username = request.form.get('username')
        password = request.form.get('password')

        # 读取所有用户数据
        with open('user_txt/user_data.txt', 'r') as file:
            users = [line.strip() for line in file]

        # 检查用户是否已存在
        if any(f'Username: {username}' in user for user in users):
            # 用户已存在，返回模板并传递用户信息和失败消息
            return render_template('gaogao.html', users=users, add_success_message='用户已存在')

        # 用户不存在，将用户信息写入文本文件
        with open('user_txt/user_data.txt', 'a') as file:
            file.write(f'Username: {username}, Password: {password}\n')

        # 获取所有用户数据并传递到模板
        with open('user_txt/user_data.txt', 'r') as file:
            users = [line.strip() for line in file]

        # 返回模板，并传递用户信息和成功消息
        return render_template('gaogao.html', users=users, add_success_message='用户添加成功')


# 删除用户路由
@app.route('/gaogao/delete_user', methods=['POST'])
def delete_user():
    if request.method == 'POST':
        # 获取要删除的用户名
        username_to_delete = request.form.get('username')

        # 读取所有用户数据
        with open('user_txt/user_data.txt', 'r') as file:
            users = [line.strip() for line in file]

        # 检查用户是否存在
        if any(f'Username: {username_to_delete}' in user for user in users):
            # 用户存在，写入不包含要删除用户的数据
            with open('user_txt/user_data.txt', 'w') as file:
                for user in users:
                    if not user.startswith(f'Username: {username_to_delete}'):
                        file.write(f'{user}\n')

            # 读取删除后的所有用户数据并传递到模板
            with open('user_txt/user_data.txt', 'r') as file:
                users = [line.strip() for line in file]

            # 返回模板，并传递用户信息和成功消息
            return render_template('gaogao.html', users=users, del_success_message='用户删除成功')
        else:
            # 用户不存在，返回模板并传递用户信息和失败消息
            return render_template('gaogao.html', users=users, del_success_message='用户不存在')


if __name__ == '__main__':
    app.run(debug=True)
