import threading
from socket import *

host = '127.0.0.1'
port = 20499

clientSocket = socket(AddressFamily.AF_INET,SocketKind.SOCK_STREAM)
alias = input("Alais : ")

clientSocket.connect((host,port))
print(f"Connected To Server ({host}:{port}) successfully")

def send():
    while True:
        msg = f"{alias}: {input()}"
        clientSocket.send(msg.encode())

def receive():
    while True:
        msg = clientSocket.recv(1024).decode()
        if msg == "alias?":
            clientSocket.send(alias.encode())
        else:
            print(msg)

threading.Thread(target=receive,name='RECEIVE').start()
threading.Thread(target=send,name='RECEIVE').start()

