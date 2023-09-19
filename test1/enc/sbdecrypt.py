#!/usr/bin/python3
import sys
import os

def main(pw, origin, cip, block, limit):
    newkey=gen(sbdm(pw))
    newl=[newkey]
    i=1
    while i<block:
        # another sequence maybe?
        newkey=gen(newkey)
        newl.append(newkey)
        i=i+1
    newl2=newl
    cj=None
    w=0
    stm=[]
    d=0
    curs=0
    num=0
    while w==0:
        o= origin.read (block)
        t=len(o)
        curs=curs+t
        if t!=block:
            if t==0:
                w=1
                break
            else: 
                w=1
                o=padding(o, block, num)
                break
        if d==0:
            newl=newl[-1]
            newkey=gen(newl)
            newl=[newkey]
            i=1
            while i<block:
            # another sequence maybe?
                newkey=gen(newkey)
                newl.append(newkey)
                i=i+1
            xoredf=app(o, newl)
            z=byte_sw (xoredf,newl)
            #print(newl2)
            cj = app(z, newl2)
            
            d=1
        else:
            
            newl=newl[-1]
            newkey=gen(newl)
            newl=[newkey]
            i=1
            while i<block:
            # another sequence maybe?
                newkey=gen(newkey)
                newl.append(newkey)
                i=i+1
            xoredf=app(o, newl)
            z=byte_sw (xoredf,newl)
            cj = app(z, stm)
            #print(cj)
    
        stm=o
        num=check_limit(curs, limit)
        if num==1:
            w=1
        cj=decode(cj, block, num)
        if num==1: 
            cip.close()

    origin.close()

def check_limit(curs, limit):
    if curs==limit:
        return 1
    else: 
        return 0
    
def byte_sw (xoredf, newl):
    j=15
    #swap
    xoredf= list(xoredf)
    
    while j>=0:
        first= newl[j] & 0xf
        second= (newl[j]>>4) & 0xf
        xoredf [first], xoredf [second] = xoredf [second], xoredf [first]
        j=j-1
    c=bytes(xoredf)
    return c
        
        

def app(padded,stream):
    
    p1=len(padded)
    s=0
    xored=[]
    while s<p1:
        cur=padded[s]
        next=stream[s]
        xord=cur ^ next
        xored.append(xord)
        s=s+1
    return bytes(xored)
        
        
        


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



def padding(text,block, num):
    t=len(text)
    textref=text
    if num==1:
        
        """text=text.rstrip(b"\x0e")
        text=text.rstrip(b"\x01")
        text=text.rstrip(b"\x02")
        text=text.rstrip(b"\x03")
        text=text.rstrip(b"\x04")
        text=text.rstrip(b"\x05")
        text=text.rstrip(b"\x06")
        text=text.rstrip(b"\x07")
        text=text.rstrip(b"\x08")
        text=text.rstrip(b"\x09")
        text=text.rstrip(b"\x0a")
        text=text.rstrip(b"\x0b")
        text=text.rstrip(b"\x0c")
        text=text.rstrip(b"\x0d")
        text=text.rstrip(b"\x0f")
        text=text.rstrip(b"\t\t")
        text=text.rstrip(b"\x00")
        """
        text=text.replace(b"\x0e", b"")
        text=text.replace(b"\x01", b"")
        text=text.replace(b"\x02", b"")
        text=text.replace(b"\x03", b"")
        text=text.replace(b"\x04", b"")
        text=text.replace(b"\x05", b"")
        text=text.replace(b"\x06", b"")
        text=text.replace(b"\x07", b"")
        text=text.replace(b"\x08", b"")
        text=text.replace(b"\x09", b"")
        text=text.replace(b"\t\t", b"")
        text=text.replace(b"\x00", b"")
        text=text.replace(b"\x0b", b"")
        text=text.replace(b"\x0c",b"")
        text=text.replace(b"\x0d", b"")
        text=text.replace(b"\x0f", b"")
        
        if text!=textref:
            return text
        else:
            text=text.replace(b"\x0a",b"")
            return text
        """
       

        """
        
        
    else:
        return text
            


        

                

def decode (x, y, c) :
    
    #print(cj)
    cj=padding(x, block, c)
    #print(cj)
    cip.write (cj)
    return cj
    

if __name__ == "__main__":
    #try:
        if (len(sys.argv)) > 4:
            msg='Error: too many arguments'
            print(msg)
        elif (len(sys.argv)) < 4:
            msg='Error: missing arguments'
            print(msg)

        else :
            pw=sys.argv[1]
            origin=open(sys.argv[2], mode="rb")
            limit=os.path.getsize(sys.argv[2])
            cip=open(sys.argv[3], mode="wb+")
            block=16
            main(pw, origin, cip, block, limit)
    #except:
      #  msg='Error: plaintext file does not exist'
       # print(msg)

