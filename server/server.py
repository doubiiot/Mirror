import socket
import random
import pymysql
PORT = 6666
pass_word = '123456'
def InsertIntoMysql(buff):
    ins_succ = 0
    try:
        #create table all_sentence (id INT NOT NULL AUTO_INCREMENT,my_sentence VARCHAR(64) NOT NULL,PRIMARYY KEY(id))
        # 打开数据库连接
        db = pymysql.connect(host='127.0.0.1',user='root',passwd=pass_word,db='mysql')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cur = db.cursor()
        #数据库语句
        #cur.execute('CREATE DATABASE IF NOT EXISTS sentence')#create db
        cur.execute('USE sentence')
        #insert
        #INSERT INTO all_sentence  values('1','123456');
        cur.execute('INSERT INTO all_sentence(my_sentence) VALUES(%s)',(buff))
        cur.connection.commit()
        ins_succ = 1
    except Exception as e:
        print(e)
    db.close()
    return ins_succ

def load_sentence():
    try:
        # 打开数据库连接
        db = pymysql.connect(host='127.0.0.1',user='root',passwd=pass_word,db='mysql')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cur = db.cursor()
        cur.execute('USE sentence')
        #select one
        cur.execute('select count(*) from all_sentence')
        id_num = cur.fetchone()
        print("id_num = %s" % id_num)
        all_num = int(id_num[0])
        print("all_num = %s" % all_num)
        radnum = random.randint(1, all_num)
        print("radnum is %s" % radnum)
        print(str(radnum))
        try:
            cur.execute('SELECT * FROM all_sentence WHERE id = %s' % str(radnum))
        except Exception as sql_error:
            print(sql_error)
        data = cur.fetchone()
        print(data)
        return data
    except Exception as e:
        print(e)
    db.close()

if __name__ == "__main__":
    soc_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    soc_server.bind(('',PORT))
    soc_server.listen(5)
    while True:
        try:
            coon,addr = soc_server.accept()
            print("%s connect success!" % str(addr[0]))
            data = coon.recv(1024).decode('utf-8')
            if data == "load":
                snd_msg = load_sentence()
                #print("snd msg is %s" % snd_msg)
                #print(snd_msg[1])
                coon.sendall(snd_msg[1].encode('utf-8'))

            else:
                if(data.split('/', 1)[0] == 'newmsg'):
                    msg = data.split('/', 1)[1]
                    print(msg)
                    if(InsertIntoMysql(msg)):
                        print("msg : '%s' insert into mysql success!" % msg)
                        coon.sendall("insert success".encode('utf-8'))
                    else:
                        coon.sendall("insert failed".encode('utf-8'))
        except Exception as soc_error:
            print(soc_error)
