import socket
HOST='115.159.22.181'
#HOST='127.0.0.1'
PORT= 6666
def getSentence():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
    s.connect((HOST,PORT))       #要连接的IP与端口
    while True:
           s.send("load".encode('utf8'))      #把命令发送给对端
           data=s.recv(1024).decode('utf-8')     #把接收的数据定义为变量
           print(data)        #输出变量
           return data
    s.close()   #关闭连接
