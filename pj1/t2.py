python3 auth.py AddUser xy 123
python3 auth.py AddUser sh 456
python3 auth.py AddUser wy 789

python3 auth.py SetDomain cd ""


python3 auth.py SetDomain xy d
python3 auth.py SetDomain xy a
python3 auth.py SetDomain sh c
python3 auth.py SetDomain xy c
python3 auth.py SetDomain sh d
python3 auth.py SetDomain wy n
python3 auth.py DomainInfo b

python3 auth.py SetType "" ""
python3 auth.py SetType apple fruit
python3 auth.py SetType speaker monkey
python3 auth.py SetType monkey animal
python3 auth.py SetType rmb gold
python3 auth.py SetType aqua water
python3 auth.py SetType speaker noise

python3 auth.py SetType rmb gold
python3 auth.py SetType lion animal
python3 auth.py SetType car noise
python3 auth.py SetType dollar gold
python3 auth.py SetType USd gold
python3 auth.py TypeInfo name

python3 auth.py AddAccess write a noise
python3 auth.py AddAccess "" a noise
python3 auth.py AddAccess write a noise
python3 auth.py AddAccess write f noise
python3 auth.py AddAccess read a monkey
python3 auth.py AddAccess read a noise
python3 auth.py AddAccess read fdd bar
python3 auth.py AddAccess read a noise

python3 auth.py SetType chip monkey
python3 auth.py SetType gro monkey
python3 auth.py SetType jz bar
python3 auth.py SetDomain xy fdd
python3 auth.py SetDomain sh fdd
python3 auth.py SetDomain wxy fdd
python3 auth.py SetDomain xy f

python3 auth.py CanAccess write xy aqua
python3 auth.py CanAccess write wxy speaker

python3 auth.py CanAccess write xy car

python3 auth.py AddAccess read c gold
python3 auth.py CanAccess write xy USd
python3 auth.py CanAccess read xy USd
python3 auth.py CanAccess write sh USd
python3 auth.py CanAccess write wy USd
python3 auth.py CanAccess write sh dollar
python3 auth.py CanAccess read sh dollar
python3 auth.py CanAccess read sh bar

python3 auth.py CanAccess read xy speaker






come back for domain infor don't have any name 



def last_name():
    with open("test.txt", "r") as f1:
        last= f1.readlines()[-1]
        pp=last.split(",p:")
        lastname=pp[0]
        print(lastname)


if __name__ == "__main__":
    last_name()


#def last_line():
  #  with open("test.txt", "r") as f2:
    #    last= f2.readlines()[-2]
