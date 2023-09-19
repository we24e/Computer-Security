import sys


def main(pw):
    long=2 ** 64
    Lhash=0
    c=0
    for i in pw:
        c=ord(i)
        Lhash = c+(Lhash << 6) + (Lhash << 16)-Lhash
        Lhash=Lhash % long
    gen(Lhash)

def gen(nk):
    a = 1103515245
    m = 256
    cr = 12345
    res = (a*nk + cr)% m
    print(res)
    
def hello(pw):
    while True:
        main(pw)
            
if __name__ == "__main__":
    pw=sys.argv[1]
    hello(pw)
