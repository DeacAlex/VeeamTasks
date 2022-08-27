import socket
import sys

sys.path.insert(0, 'E:/VeeamTasks/database.py')
from database import check_data
from datetime import datetime

host = ""
port = 8001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', port))
s.listen(50)

while True:
    c, addr = s.accept()
    print('Connected to :', addr[0], ':', addr[1])
    data = c.recv(1024).decode()
    uid = data.split(' ')[5].strip(',')
    code = data.split(' ')[9]
    print(data)
    if check_data(uid, code) is True:
        with open('E:/VeeamTasks/server.txt', 'a') as log_file:
            now = datetime.now()
            date_time = now.strftime("%d-%m-%Y, %H:%M:%S: ")
            message = data.split(' ')[2].strip(',')
            log_file.write(date_time + message + '\n')

s.close()
