import sys

BLOCK_SIZE = 16

def pad( m ):
    if len( m ) == 0:
        # return a whole block worth of padding
        temp_list = []
        for i in range( BLOCK_SIZE ):
            temp_list.append( BLOCK_SIZE )
        m = bytes( temp_list )
        print( m)
    # return amount based on how many bytes left out of BLOCK_SIZE

    # add the curr values in m to a temp list that we are
    # then going to add the padding to
    temp_list = []
    for val in m:
        temp_list.append( val )

    # tack on the remaining padding
    for idx in range( BLOCK_SIZE - len(m) ):
        temp_list.append( BLOCK_SIZE - len(m) )

    m = bytes( temp_list )

    print( m)
                
            
    
    
    
if __name__ == "__main__":
    start_file = open(sys.argv[1], "rb")
    m = start_file.read( BLOCK_SIZE )
    pad(m)
