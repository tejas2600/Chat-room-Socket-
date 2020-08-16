import socket
import threading


username = input("Enter your Username: ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname, 9999))

def receive():
    while True:
        try:
            
            
            message = client.recv(1024).decode('ascii')
            if message == 'USERNAME':
                client.send(username.encode('ascii'))
            else:
                print(message)
        except:
            
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(username, input(''))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()        