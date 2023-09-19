import threading
import time
import random
import sys
import socket
def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket1 created")
        cs2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket2 created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
    port = int(sys.argv[2])
    port2 = int(sys.argv[3])
    #addr = socket.gethostbyname(socket.gethostname('rs'))
    addr = socket.gethostbyname(sys.argv[1])
    #addr2 = socket.gethostbyname(sys.argv[1])
    
    server_binding = (addr, port)
    cs.connect(server_binding)
    count=0
    msg = open('PROJI-HNS.txt','r')
    for entry in msg:
        new_data=str(" %s" % entry).encode("utf-8")
        if new_data:
            cs.send(new_data)
            time.sleep(2)
            data_from_server=cs.recv(1024).decode("utf-8")
            print("Data received from rs: %s" % data_from_server)
             
                
                
            while data_from_server:
                if count==0:
                    if ' - NS' in data_from_server:
                        tsHostname=data_from_server.replace(' - NS', '')
                        addr2 = socket.gethostbyname(tsHostname)
                        server_binding2 = (addr2, port2)
                        cs2.connect(server_binding2)
                        count +=1
                        cs2.send(new_data)
                        data_from_ts=cs2.recv(1024).decode("utf-8")
                        print("Data received from ts: %s" % data_from_ts)
                        with open("RESOLVED.txt", "a") as f:
                            print ("%s" % data_from_ts, file=f)
                        break
                    else: 
                        with open("RESOLVED.txt", "a") as f:
                            print ("%s" % data_from_server, file=f)
                            break
                else: 
                    if ' - NS' in data_from_server:
                        cs2.send(new_data)
                        data_from_ts=cs2.recv(1024).decode("utf-8")
                        print("Data received from ts: %s" % data_from_ts)
                        with open("RESOLVED.txt", "a") as f:
                            print ("%s" % data_from_ts, file=f)
                        break
                    else: 
                        with open("RESOLVED.txt", "a") as f:
                            print ("%s" % data_from_server, file=f)
                            break
    cs.close()
    cs2.close()
    exit()

if __name__ == "__main__":
    t2 = threading.Thread(name='client', target=client)
    t2.start()
