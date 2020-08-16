import socket
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname, 9999))
server.listen()

clients = []
usernames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            
            message = client.recv(1024)
            broadcast(message)
        except:
            
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast('{} left!'.format(username).encode('ascii'))
            usernames.remove(username)
            break

def receive():
    while True:
        
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        
        client.send('USERNAME'.encode('ascii'))
        username = client.recv(1024).decode('ascii')
        usernames.append(username)
        clients.append(client)

    
        print("Username is {}".format(username))
        broadcast("{} joined!".format(username).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()