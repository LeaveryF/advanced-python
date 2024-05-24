# 客户端服务器以json格式收发数据



# 客户端post json数据 服务器响应json数据
# 客户端需要有处理json数据的能力

# 测试：在apifox中新建接口
#       改post - 请求参数 - body - json - 示例 - 指定数据
#       - 运行 - 输入url: http://127.0.0.1:5000/submit - 发送

from flask import Flask, request, jsonify

# 初始化 Flask 应用
app = Flask(__name__)

# 定义一个处理 POST 请求的路由
@app.route('/submit', methods=['POST'])
def submit_data():
    # 获取 POST 请求中的 JSON 数据
    # request.get_json()返回一个python字典对象
    # 如果非json格式数据 或解析失败 将返回none
    # request.json属性同样可以返回处理后的json数据(字典对象) 但如果不是json格式将引发异常 不推荐使用
    print(request.get_json())
    data = request.get_json()
    
    # 检查是否提供了 name 和 age 参数
    if 'name' not in data or 'age' not in data:
        return jsonify({'error': 'Missing parameters! Please provide both name and age.'}), 400
    
    # 准备要返回的响应内容
    response = {
        'message': f'Hello, {data["name"]}! You are {data["age"]} years old.'
    }
    
    # 返回 JSON 格式的响应
    # jsonify() (json化/序列化) 将 Python 对象转换为 JSON 格式的 HTTP 响应  它可以接收各种python对象
    # 根据文档 字典或列表类型返回时会自动序列化 可以不调用该函数
    # return response
    return jsonify(response)

# 启动 Flask 应用
if __name__ == '__main__':
    app.run(debug=True)
