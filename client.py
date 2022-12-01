import socket
import pickle

def get_e1(p):
    for i in range(2, p):
        if math.gcd(i, p) == 1:
            return i
    return -1

def inverse(a, p):
    for i in range(1, p):
        if pow(i*a,1, p) == 1:
            return i


s = socket.socket()
port = 1729
s.connect(('127.0.0.1', port))
print(s.recv(1024).decode())

# Elgamal Algorithm
p = int(input("Enter the prime p\n"))
e1 = int(input("Select any one of the co-prime of p in zp\n"))
d = int(input("Enter the private key\n"))
e2 = pow(e1, d, p)
data = [p, e1, e2]

# data sending
data = pickle.dumps(data)
s.send(data)

# message receiving
data = pickle.loads(s.recv(1024))
c1 = data[1]
c2 = data[0]
decrypted_message = ''.join(chr((i*inverse(pow(c1, d, p), p))%p) for i in c2)
print(f'message = {decrypted_message}')
s.close()