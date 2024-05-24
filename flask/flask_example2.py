# 客户端通过get请求发送参数 服务器响应html字符串



# GET请求是一种HTTP请求方法，用于从服务器获取数据
# GET请求是无状态的，通常用于请求不包含用户敏感数据的公共资源，如HTML页面或图片
# 通过URL的查询字符串（即URL中的?key=value部分）传递参数

# request对象是一个包含了HTTP请求信息的对象 其中包含客户端的http请求的各种信息和数据
# 通过request.args.get()方法来获取URL中的查询参数

# 测试url：http://127.0.0.1:5000/user?name=John&age=30

from flask import Flask, request

# 初始化 Flask 应用
app = Flask(__name__)

# 定义一个处理 GET 请求的路由
@app.route('/user', methods=['GET'])
def get_user():
    # 获取 URL 中的查询参数 name 和 age
    name = request.args.get('name')
    age = request.args.get('age')
    
    # 检查是否提供了 name 和 age 参数
    if name is None or age is None:
        return 'Missing parameters! Please provide both name and age.'
    
    # 准备要返回的响应内容
    response = f'Hello, {name}! You are {age} years old.'
    
    # 返回响应
    return response

# 启动 Flask 应用
if __name__ == '__main__':
    app.run(debug=True)
