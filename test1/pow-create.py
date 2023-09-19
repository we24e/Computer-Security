#!/usr/bin/python3 
import sys 
import hashlib
import time

def check_0(n3, hashed):
    for i in hashed: 
        if i!=str(0): 
            if i==str(1):
                n3=n3+3
            elif i==str(2) or i==str(3):
                n3=n3+2
            elif i==str(4) or i==str(5) or i==str(6) or i==str(7):
                n3=n3+1
            else:
                pass
            break
        else:
            n3=n3+4
    return n3

def main():
    time_start = time.time()
    n=0
    hex2=None
    lst=[chr(33)]
    last=chr(126)
    start=33
    i2=start
    start_chr=chr(33)
    try:
        c=open(sys.argv[2], "rb")
    except:
        print("Error: unable to open '", sys.argv[2], "'")
        sys.exit()
    text=c.read()
    diff=int(sys.argv[1])
    if diff<0 :
        print("Error: negative bit value")
        sys.exit()
    hsh = hashlib.sha256(text).hexdigest()
    c2=0
    b2=True
    #nz=0
    #n=check_0(n, hsh)
    #print(n)
    c0=1

    '''while n<= diff:
        #if diff>=4:
        for i in range(33,127):
            c2=c2+1
            j=chr(i)
            j=bytes(j,'utf-8')
            text2=text+j
            print(text2)
            hsh=hashlib.sha256(text2).hexdigest()
            print(hsh)
            n2=check_0(n, hsh)
            if n2>nref:
                nref=n2
                textz=j
            text=textref
            if n2>=diff:
                b=True
                break
            if i==126:
                print(textz)
                i=33
                textref=text+bytes(chr(33), 'utf-8')
                text=textref
                nref=0
                 #   for i2 in rangerange(33,126):
               # c2=c2+1
               # j=chr(i)
        if b==True:
            break
       # else: 

'''

    hex2= hsh+"".join (lst)
    hex2=str.encode(hex2)
    #print(hex2)
    hashed=hashlib.sha256(hex2).hexdigest()
    #print(hashed)
    n2=check_0(0, hashed)
    while n2<diff:
        i2=i2+1
        if i2>=127:
            i2=start
            for i in reversed(range(0,c2+1)):
                if lst[i]==last:
                    lst[i]=start_chr
                    b2=True
                else:
                    cur=ord(lst[i])
                    lst[i]=chr(cur+1)
                    b2=False
                    break
            if b2== True:
                lst.append(start_chr)
                c2=c2+1
        else:
            lst[c2]=chr(i2)

        hex2=hsh+"".join(lst)
        hex2=str.encode(hex2)
        hashed=hashlib.sha256(hex2).hexdigest()
        n2=check_0(0, hashed)
        c0=c0+1
    f=sys.argv[2]
    prf="".join(lst)
    ti = (time.time() - time_start)
    prt(f, hsh, prf, hashed, n2, c0, ti)
        
    c.close()


def prt(c1, cz, c3, c4, c5, c6, c7):
    print("File:", c1)
    print("Initial-hash:", cz)
    print("Proof-of-work:", c3)
    print("Hash:", c4)
    print("Leading-zero-bits:", c5)
    print("Iterations:", c6)
    print("Compute-time:", c7)



if __name__ == "__main__":
    cz=len(sys.argv)
    if cz <3: 
        print("Error: missing arguments")
    elif cz>3 : 
        print("Error: too many arguments")
    else:
        main()
