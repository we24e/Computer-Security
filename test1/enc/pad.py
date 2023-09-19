import sys

block = 16

def pad(text,block):
    nblock=[]
    t=len(text)
    blockref=block
    if t==block:
        print(text)
    else:
        if t==0:
            while blockref>0:
                nblock.append(block)
                print(block)
                blockref=blockref-1
            dnblock=bytes(block)
            print(dnblock)
        else :
            ap=block-t
            apref=0
            for t1 in text:
                nblock.append(t1)
            while (apref+t)<block:
                nblock.append(ap)
                apref=apref+1
            dnblock=bytes(nblock)
            print(dnblock)
                
            
    
    
    
if __name__ == "__main__":
    start_file = open(sys.argv[1], "rb")
    text = start_file.read( block )
    pad(text, block)
