import threading
from socket import *

host = '127.0.0.1'
port = 20499

serverSocket = socket(AddressFamily.AF_INET,SocketKind.SOCK_STREAM)

serverSocket.bind((host,port))
serverSocket.listen(5)
print("Server is up & Listining ...")

clients = []
aliases = []

def broadcast(message):
    for client in clients:
        client.send(message.encode())

def handle_client(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(index)
            client.close()
            alias = aliases[index]
            broadcast(f"~ {alias} has lesft the chat room! ~")
            aliases.remove(alias)
            break


def handle_connections():
    while True:
        client,address = serverSocket.accept()
        print(f"New Connection from => {address[0]}:{address[1]}")
        client.send('alias?'.encode())
        alias = client.recv(1024).decode()
        clients.append(client)
        aliases.append(alias)
        print(f"Connection from => {address[0]}:{address[1]} ({alias}) established successfully")
        broadcast(f"~({alias}) has Joined the Chat room ~")
        threading.Thread(target=handle_client,args=(client,)).start()

if __name__ == "__main__":
    handle_connections()

