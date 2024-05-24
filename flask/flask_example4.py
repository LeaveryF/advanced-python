# 客户端post表单数据 服务器响应html字符串



# POST 请求是一种 HTTP 请求方法，用于向服务器提交数据
# POST 请求的数据通常不会显示在 URL 中，而是包含在请求体中，因此适用于提交包含用户敏感信息或大量数据的表单

# 使用 request.form 属性来获取 POST 请求中的表单数据

# 测试：在apifox中新建接口
#       改post - 请求参数 - body - form-data - 指定数据
#       - 运行 - 输入url: http://127.0.0.1:5000/submit - 发送

# apifox里可以不写文档直接测试 但类型必须改为post

# 或者更简单地 使用apipost中的 快捷请求

from flask import Flask, request

# 初始化 Flask 应用
app = Flask(__name__)

# 定义一个处理 POST 请求的路由
@app.route('/submit', methods=['POST'])
def submit_data():
    # 获取 POST 请求中的表单数据
    name = request.form.get('name')
    age = request.form.get('age')
    
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
