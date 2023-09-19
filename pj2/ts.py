import threading
import time
import sys
import random
import unicodedata
import socket
def ts():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[tS]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding2 = ('', int(sys.argv[1]))
    ss.bind(server_binding2)
    ss.listen(1)
    host = socket.gethostname()
    print("[ts]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[ts]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[ts]: Got a connection request from a client at {}".format(addr))
    while True:
        data=csockid.recv(1024).decode("utf-8").strip()
       # if data in dns: 
           # print("found")
           # re=dns.get(data)
           # csockid.send(re.encode("utf-8"))
        test_array = []
        print(data)
        with open('PROJI-DNSTS.txt') as f:
            for line in f:
                test_array.append(line.strip())

        #print ("Data received from client: %s" % data)
        #print ("Data to client: %s" % data[::-1],"%s" % data)
        #send the new data back to client
        count=0 
        for item in test_array: 
            max=len(test_array)
            count+=1
            if data.casefold() in item.casefold() and data.casefold()[:3] == item.casefold()[:3]:
                csockid.send(item.encode("utf-8"))
                time.sleep(1)
                count=0
                break
            #else if data not in item: 
            else:
                if count==max:
                    msgb=data + " - Error:HOST NOT FOUND"
                    csockid.send(msgb.encode("utf-8"))
                    break
        if not data:
            break
    csockid.close()              
    print("Done.")
    ss.close()
    exit()
    
if __name__ == "__main__":
    t1 = threading.Thread(name='ts', target=ts)
    t1.start()
