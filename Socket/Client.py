'''
Client端流程:
1.建立socket
2.发送内容到指定服务器
3.接受服务器指定的反馈内容

'''
import socket
def clientFunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #发送的数据必须是bytes格式
    text = "I love you"
    data = text.encode()
    #发送数据
    sock.sendto(data, ("127.0.0.1",7852))
    #等待反馈
    data,addr=sock.recvfrom(200)
    #反馈的数据需要解码
    data=data.decode()
    print(data)
if __name__ == '__main__':
    clientFunc()