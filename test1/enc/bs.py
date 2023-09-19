import sys
block=16
def main(pw):
    newkey=gen(sbdm(pw))
    print(newkey)
    newl=[newkey]
    i=1
    while i<block:
        newkey=gen(newkey)
        newl.append(newkey)
        i=i+1
    print(newl)
        

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


if __name__ == "__main__":
    pw = sys.argv[1]
    main(pw)
