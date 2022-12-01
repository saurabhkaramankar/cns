import socket
import pickle
import math

s = socket.socket()
port = 1729
s.bind(('', port))
print("socket binded to {0}".format(port))
s.listen(5)
print('server is listening')

while True:
    # connection
    c, address = s.accept()
    c.send('Hello! you are connected'.encode())
    print(address, 'got connection')

    # getting data
    data = pickle.loads(c.recv(1024))
    p = data[0]
    e1 = data[1]
    e2 = data[2]

    # sending the encrypted message
    r = int(input("Enter the secret key\n"))
    c1 = pow(e1, r, p)
    message = [ord(i) for i in input("Enter the message\n")]
    r2 = pow(e2, r, p)
    c2 = [(i*r2)%p for i in message]
    data = pickle.dumps([c2, c1])
    c.send(data)
    c.close()





