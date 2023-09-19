#!/usr/bin/python3
import sys


def main(pw, origin, cip, block):
    newkey=gen(sbdm(pw))
    newl=[newkey]
    i=1
    while i<block:
        # another sequence maybe?
        newkey=gen(newkey)
        newl.append(newkey)
        i=i+1
    w=0
    stm=[]
    d=0
    while w==0:
        o= origin.read (block)
        padded=o
        t=len(o)
        if t!=block:
            padded=(padding (o, block))[0]
            w=1
            
        if d==0:
            xoredf=app(padded, newl)
            d=1
            newl=newl[-1]
            newkey=gen(newl)
            newl=[newkey]
            i=1
            while i<block:
            # another sequence maybe?
                newkey=gen(newkey)
                newl.append(newkey)
                i=i+1
        else:
            xoredf=app(padded, stm)
            newl=newl[-1]
            newkey=gen(newl)
            newl=[newkey]
            i=1
            while i<block:
            # another sequence maybe?
                newkey=gen(newkey)
                newl.append(newkey)
                i=i+1
        
        stm=encode (xoredf, newl)
        
    origin.close()
    cip.close()
    
def byte_sw (xoredf, newl):
    j=0
    #swap
    xoredf= list(xoredf)
    
    while j<16:
        first= newl[j] & 0xf
        second= (newl[j]>>4) & 0xf
        xoredf [first], xoredf [second] = xoredf [second], xoredf [first]
        j=j+1
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



def padding(text,block):
    nblock=[]
    t=len(text)
    blockref=block
    if t==block:
        return text, False
    else:
        if t==0:
            while blockref>0:
                nblock.append(block)
                blockref=blockref-1
            dnblock=bytes(block)
            return dnblock, True
        else :
            ap=block-t
            apref=0
            for t1 in text:
                nblock.append(t1)
            while (apref+t)<block:
                nblock.append(ap)
                apref=apref+1
            dnblock=bytes(nblock)
            return dnblock, True
                

def encode (x, y) :
    z= byte_sw (x, y)
    stm = app(z, y)

    cip.write (stm)
    return stm
    

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
            block=16
            main(pw, origin, cip, block)
    except:
        msg='Error: plaintext file does not exist'
        print(msg)
