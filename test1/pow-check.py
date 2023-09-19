#!/usr/bin/python3 
import sys 
import hashlib

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
    n=0
    try:
        head=open(sys.argv[1], "r")
    except:
        print("Error: unable to open '", sys.argv[1], "'")
        sys.exit()
    try:
        f=open(sys.argv[2], "rb")
    except:
        print("Error: unable to open '", sys.argv[2], "'")
        sys.exit()
    c2=0
    text=f.read()
    hsh = hashlib.sha256(text).hexdigest()

    for line in head:
        if "Initial-hash: " in line:
            i=(line.split(": ")[1]).strip()
            if not i:
                print("ERROR: missing Initial-hash in header")
                c2=c2+1
            elif (hsh!=i):
                print("ERROR: initial hashes don't match\n", "hash in header:", i,"\n","file hash:", hsh)
                c2=c2+1
            else:
                print("PASSED: initial file hashes match")
        elif "Proof-of-work: " in line:
            p=(line.split(": ")[1]).strip()
            if not p: 
                print("ERROR: missing Proof-of-work in header")
                c2=c2+1
        elif "Leading-zero-bits: " in line:
            l2=(line.split(": ")[1]).strip()
            if not l2:
                print("ERROR: missing Leading-zero-bits in header")
                c2=c2+1
        elif "Hash: "in line:
            h= (line.split(": ")[1]).strip()
            if not h:
                print("ERROR: missing Hash in header")
                c2=c2+1

    text1=hsh+p
    text1=str.encode(text1)
    hash = hashlib.sha256(text1).hexdigest()
    checked=check_0(n, hash)

    if int(checked)!=int(l2):
        print("ERROR: Leading-zero-bits value:", l2, ", but hash has", checked, "leading zero bits")
        c2=c2+1
    else:
        print("PASSED: leading bits is correct")

    if h!= hash:
        print("ERROR: pow hash does not match Hash header\n", "expected:", hash,"\n","header has:", h)
        c2=c2+1
    else: 
        print("PASSED: pow hash matches Hash header")
    if c2!= 0:
        print("fail")
    else:
        print("pass")


if __name__ == "__main__":
    cz=len(sys.argv)
    if cz <3: 
        print("Error: missing arguments")
    elif cz>3 : 
        print("Error: too many arguments")
    else :
        main()