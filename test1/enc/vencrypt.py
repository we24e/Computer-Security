#!/usr/bin/python3
import sys

def main(key, origin, ci):
    while origin:
        o=origin.read(1)
        if not o:
            break
        k=key.read(1)
        if not k:
            key.seek(0)
            k=key.read(1)
        makecip(o, k, ci)
    key.close()
    origin.close()
    ci.close()

def makecip(o,k,ci):
    row = ord(o)
    col = ord(k)
    cur=row+col
    pos=cur % 256
    ci.write(int.to_bytes(pos,byteorder= sys.byteorder,length=1))
            
    
if __name__ == "__main__":
    try:
        if (len(sys.argv)) != 4:
            msg='Wrong number of arguments'
            print(msg)
    
        else :
            key=open(sys.argv[1], mode="rb")
            origin=open(sys.argv[2], mode="rb")
            ci=open(sys.argv[3], mode="wb+")
            main(key, origin, ci)
    except:
        msg='Error: input doesnt exist'
        print(msg)

            
            
      
