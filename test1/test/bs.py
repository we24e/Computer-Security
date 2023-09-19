import sys
BLOCK_SIZE = 16

def create_IV(seed):
    iv = []
    val = lcg( seed )
    print(val)
    iv.append( val )
    for idx in range( BLOCK_SIZE - 1 ):
        val = lcg( val )
        iv.append( val )
    # print(iv)
    return iv

# linear congruential generator
def lcg(x_n):
    return (1103515245 * x_n + 12345) % 256

# sbdm hash
def sbdm(str):
    max = 18446744073709551615 + 1
    hash, c = 0, 0
    for char in str:
        c = ord(char)
        hash = c + (hash << 6) + (hash << 16) - hash
        # print("{}: {}".format(c, hash))

    # have to mod by max because I am using python
    return hash % max
    
def main():
    password = sys.argv[1]

    seed = sbdm( password )

    # create the iv
    iv = create_IV( seed )
    print(iv)


if __name__ == "__main__":
    main()
