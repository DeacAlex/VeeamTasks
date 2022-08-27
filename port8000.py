import socket
import uuid
from threading import Thread


def Main():
    host = ""
    port = 8000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
    s.listen(50)
    print("socket is listening")

    while True:
        c, addr = s.accept()

        def send():
            data = uuid.uuid1().hex
            c.send(data.encode('utf-8'))

        def receive():
            recv = c.recv(1024).decode()
            print ('Received:' + str(recv))

        print('Connected to :', addr[0], ':', addr[1])
        Thread(target=send).start()
        Thread(target=receive).start()

    s.close()


if __name__ == '__main__':
    Main()
