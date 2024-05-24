// 创建WebSocket连接
const socket = new WebSocket('ws://localhost:1234');

// 连接打开后发送JSON数据
socket.addEventListener('open', (event) => {
    const data = { "number": 0, "message": "Hello!" };
    socket.send(JSON.stringify(data));
});

// 监听消息
socket.addEventListener('message', (event) => {
    console.log(JSON.parse(event.data));
});
