import sys

def main():
    list1=["1","2"]
    list_plain="".join(list1)
    #print(list_plain)
    i=0
    while (int(list_plain) - 98 !=0):
        list1[(i+1)] = str(int(list1[(i+1)]) +1)
        if int(list1[(i+1)]) > 9:
            list1[(i+1)]=str(1)
            list1[(i)]=str(int(list1[(i)]) +1)
        if int(list1[(i)]) > 9 :
            print("not found")
            break
            sys.exit()
        list_plain="".join(list1)
        print(list1)



if __name__ == "__main__":
    main()