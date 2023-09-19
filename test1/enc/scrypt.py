#!/usr/bin/python3
import sys

def main(pw, origin, cip):
    newkey=gen(sbdm(pw))
    while origin:
        o=origin.read(1)
        if not o:
            break
        App (newkey,o,cip)
        newkey=gen(newkey)
    origin.close()
    cip.close()
    
def gen(nk):
    a = 1103515245
    m = 256
    cr = 12345
    res = (a*nk + cr)% m
    return(res)
    
def sbdm(password):
    Lhash=0
    long=2 ** 64
    for i in pw:
        Lhash = ord(i) +(Lhash << 6) + (Lhash <<16)-Lhash
        Lhash=Lhash % long
    return Lhash


def App(newkey, o, cip):
    cur=ord(o)
    xord=cur ^ newkey
    cip.write(int.to_bytes(xord, byteorder= sys.byteorder,length=1))


if __name__ == "__main__":
    try:
        if (len(sys.argv)) > 4:
            msg='Error: too many arguments'
            print(msg)
        elif (len(sys.argv)) < 4:
            msg='Error: missing arguments'
            print(msg)

        else :
            pw=sys.argv[1]
            origin=open(sys.argv[2], mode="rb")
            cip=open(sys.argv[3], mode="wb+")
            main(pw, origin, cip)
    except:
        msg='Error: input doesnt exist'
        print(msg)
