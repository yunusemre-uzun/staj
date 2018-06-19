import socket
import threading
import sys

def client(conn):
    global connections
    conn.send(str.encode("Welcome!\n"))
    while True:
        data = conn.recv(2048)
        for i in range(len(connections)):
            if(connections[i]==conn):
                break
        reply = "User-"+str(i+1)+" "+data.decode('utf-8')
        conn.sendall(str.encode("You: " + data.decode('utf-8')))
        for n in connections:
            if(n==conn):
                continue
            n.sendall(str.encode(reply))
    conn.close()

if __name__ == "__main__" :
    host = ''
    port = int(input())
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.bind((host,port))
    except socket.error as e :
        print(str(e))
    s.listen(5)
    connections = []
    while True :
        conn , addr = s.accept()
        print("Connected to " + str(addr[0]) + " : " + str(addr[1]))
        t1 = threading.Thread(target = client,args=(conn,))
        t1.start()
        connections.append(conn)
        
    

