#!/usr/bin/python3
import sys

def main(key, origin, cip):
    while cip:
        ci=cip.read(1)
        if not ci:
            break
        k=key.read(1)
        if not k:
            key.seek(0)
            k=key.read(1)
        deccip(origin, k, ci)
    key.close()
    cip.close()
    origin.close()


def deccip(origin,k,ci):
    row = ord(ci)
    col = ord(k)
    cur=row-col
    pos=(cur+256) % 256
    origin.write(int.to_bytes(pos, byteorder= sys.byteorder,length=1))
            
    
if __name__ == "__main__":
    try:
        if (len(sys.argv)) != 4:
            msg='Wrong number of arguments'
            print(msg)
        
        else :
            key=open(sys.argv[1], mode="rb")
            origin=open(sys.argv[3], mode="wb+")
            cip=open(sys.argv[2], mode="rb")
            main(key, origin, cip)
    except:
        msg='Error: input doesnt exist'
        print(msg)

            
            
      
