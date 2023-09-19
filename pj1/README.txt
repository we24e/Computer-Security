1. To run my project, use  python3 auth.py  as the command line
   For example, python3 auth.py AddUSer alice password

2. My program is case Sensitive, so 'Alice' != 'alice'


Other notices: 

(1) For this project, I used separate txt files(domains.txt, users.txt, access.txt, types.txt) that generated in the same directory as auth.py, no need to create files in advance.
 
(2) In these txt files, I sued different symbols to separate different entries, for instance, in users.txt, I used ", p:" as splitter. Similarly, I used "--" in domains as domain_name separator and ", "as separator of different entries. 

(3) The key idea for my project is to iterate through the lists to find the results, so I defined some last_line functions for different txt files at the beginning of auth.py. 

(4)'Error: wrong/missing arguments' refers to when putting too many arguments or less arguments than expected when using running the program by command. 

(5)In typeinfo and domaininfo, if a type or domain contains no strings, the program will not print anything and will not report an error as project description required. 


Sample test cases + results: 

-----------------------------------------
python3 auth.py AddUser Alice pass
python3 auth.py AddUser Bob word
python3 auth.py AddUser "" word

Success
Success
Error: username missing
-----------------------------------------
python3 auth.py Authenticate Bob word
python3 auth.py Authenticate cat password123
python3 auth.py Authenticate Alice word

Success
Error: no such user
Error: bad password
-----------------------------------------
python3 auth.py SetDomain Alice subscriber
python3 auth.py SetDomain cat subscriber
python3 auth.py SetDomain Bob subscriber
python3 auth.py SetDomain Bob admin

Success
Error: no such user
Success
Success
-----------------------------------------
python3 auth.py DomainInfo subscriber
python3 auth.py DomainInfo super

Alice
Bob
Error: domain doesn't exist
-----------------------------------------
python3 auth.py SetType disney tv
python3 auth.py SetType apple fruit
python3 auth.py SetType hbo tv

Success
Success
Success
-----------------------------------------
python3 auth.py TypeInfo tv
python3 auth.py TypeInfo game

disney_tv
hbo_tv
Error: type doesn't exist
-----------------------------------------
python3 auth.py AddAccess watch subscriber tv
python3 auth.py AddAccess buy admin fruit

Success
Success
-----------------------------------------
python3 auth.py CanAccess watch Bob hbo
python3 auth.py CanAccess eat Bob apple

Success
Error: access denied

-----------------------------------------
-----------------------------------------


Using 'cat' to display contents of my files: 
-----------------------------------------
cat users.txt

Alice, p:pass
Bob, p:word
-----------------------------------------
cat domains.txt:

subscriber--Alice, Bob
admin--Bob
-----------------------------------------
cat types.txt:

tv--disney, hbo
fruit--apple
-----------------------------------------
cat access.txt:

subscriber -> tv--watch
admin -> fruit--buy

