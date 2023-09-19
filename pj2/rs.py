import threading
import time
import random
import sys
import unicodedata
import socket
def rs():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[rS]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    server_binding = ('', int(sys.argv[1]))
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[rS]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[rS]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[rS]: Got a connection request from a client at {}".format(addr))
    #dns=getDNS()
    while True:
        data=csockid.recv(1024).decode("utf-8").strip()
       # if data in dns: 
           # print("found")
           # re=dns.get(data)
           # csockid.send(re.encode("utf-8"))
        test_array = []
        print(data)
        count2=0
        #with open('PROJI-DNSRS.txt') as f:
        file=open('PROJI-DNSRS.txt','r')
        replaced=""
        for line in file:
            line = line.strip()
            if ' - NS' in line: 
                count2+=1
                str1=line
                str2=sys.argv[2] + " - NS"
                new_line=line.replace(str1,str2)
                replaced=replaced+new_line+'\n'
                break
            replaced=replaced+line+'\n'
            test_array.append(line.strip())       
        file.close()
        write_f=open('PROJI-DNSRS.txt', 'w')
        write_f.write(replaced)
        write_f.close()
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
                    if count2==0:
                    #if '- NS' not in item:
                        with open('PROJI-DNSRS.txt', 'a') as f1:
                            print(sys.argv[2] + " - NS", file=f1)
                    msgb=sys.argv[2] + " - NS"
                    csockid.send(msgb.encode("utf-8"))
                    break
        if not data:
            break
    csockid.close()              
    print("Done.")
    ss.close()
    exit()
 
if __name__ == "__main__":
    t1 = threading.Thread(name='rs', target=rs)
    t1.start()

