"""
-Server端的编写流程
                1.建立socket负责具体通信，这个socket其实只负责接受对方的请求
                2.绑定端口和地址
                3.监听接入的访问socket
                4.接受访问的socket，可以理解接受访问即建立了一个通讯的链接通路
                5.接受对方的发送内容，利用接收到的socket接收内容
                6.如果有必要，给对方反馈信息
                7.关闭链路通路
"""
import socket


def tcp_src():
    # 1.建立socket负责具体通信,只负责接受对方的请求.真正通信的是链接后的通路
    # 需要用到两个参数AF_INET含义同UDP一致
    # SOCK_STREAM 表明是使用tcp进行通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定端口和地址
    # 此时地址是一个元组类型内容,第一部分是地址,第二个部分是端口
    addr = ("127.0.0.1", 8998)
    sock.bind(addr)

    # 3.监听接入的访问socket
    sock.listen()

    #永久运行循环
    while True:
        # 4.接受访问的socket,可以理解为接受访问就建立一个通讯链路
        # accept返回的元组一个个辅助给skt,第二个赋值给addr
        skt,addr = sock.accept()

        # 5.接受对方发送的内容,利用接收到的socket接受内容
        # 500代表接受使用的buffersize
        msg = skt.recv(500)

        # 接受的是byts格式内容,需要进行解码
        msg = msg.decode()

        rst = "Receivd msg:{0}from{1}".format(msg,addr)
        print(rst)

        # 6.如果有必要,则给对方发送反馈信息
        skt.send(rst.encode())

        # 7 .关闭通信链路
        skt.close()
if __name__ == '__main__':
    print("Start TCP Server......")
    tcp_src()
    print("Ending TCO server.....")
