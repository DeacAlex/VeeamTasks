import socket
import sys
import uuid
from threading import Thread

sys.path.insert(0, 'E:/VeeamTasks/database.py')
from database import insert_data, sql_database, check_data

host = 'local host'
port = 8000
port1 = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', port))
my_uid = uuid.uuid4().hex
data = s.recv(1024).decode()


def recv():
    if not data: sys.exit(0)
    print("Your unique code from the server is:", data)


print("My uuid is:", my_uid)
message = input("Message:")
s.send("{}".format(message).encode('utf-8'))
Thread(target=recv).start()
insert_data(my_uid, data)
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', port1))
text_message = input("Your text message:")
s.send("Text message: {}, User's UUID: {}, User's unique code: {}".format(text_message, my_uid, data).encode('utf-8'))
s.close()

