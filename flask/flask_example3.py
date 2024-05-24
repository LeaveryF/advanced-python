# 客户端通过get请求获取图片 服务器响应发送图片文件



from flask import Flask, send_file

# 初始化 Flask 应用
app = Flask(__name__)

# 定义一个处理 GET 请求的路由
@app.route('/image', methods=['GET'])
def get_image():
    # 指定要返回的图片文件路径
    image_path = 'res/image.png'
    
    # 返回图片文件作为响应体
    return send_file(image_path, mimetype='image/png')

# 启动 Flask 应用
if __name__ == '__main__':
    app.run(debug=True)
