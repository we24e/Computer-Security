#print('Hello, world!')
import sys

def last_name():
    with open("users.txt", "r") as f1:
        last= f1.readlines()[-1]
        pp=last.split(", p:")
        lastname=pp[0]
        f1.close()
        return lastname
        
def last_domain():
    with open("domains.txt", "r") as f2:
        last2= f2.readlines()[-1]
        ppd=last2.replace("--", ", ").split(", ")
        lastdo=ppd[0]
        f2.close()
        return lastdo

def last_tp():
    with open("types.txt", "r") as f3:
        lastt=f3.readlines()[-1]
        ppt=lastt.replace("--", ", ").split(", ")
        lasttp=ppt[0]
        f3.close()
        return lasttp
        
def check_user(name):
    try:
        f1=open("users.txt", "r")
        lines=f1.readlines()
        lastl=last_name()
        for line in lines:
            line=line.strip()
            sp=line.split(", p:")
            if sp[0]==name:
                return 1
                break
            elif sp[0]!=lastl:
                pass
            else:
                return 2
    except:
        return 2

def last_ln():
    with open("access.txt", "r") as f4:
        lastln=f4.readlines()[-1]
        f4.close()
        return lastln
        
def AddUser(name, password):
    try:
        f1=open("users.txt", "r")
        lines=f1.readlines()
        lastl=last_name()
        for line in lines:
            line=line.strip()
            sp=line.split(", p:")
            if sp[0]==name:
                print('Error: user exists')
                break
            elif sp[0]!=lastl:
                pass
            else:
                f = open("users.txt", "a")
                f.write(name+', p:'+password+'\n')
                f.close()
                print('Success')
    except:
        f = open("users.txt", "a")
        f.write(name+', p:'+password+'\n')
        f.close()
        print('Success')


def Authenticate(name, password):
    try:
        fa=open("users.txt", "r")
        lines=fa.readlines()
        lastl=last_name()
        for line in lines:
            line=line.strip()
            sp=line.split(", p:")
            if sp[0]==name:
                if sp[1]==password:
                    print('Success')
                    break
                else:
                    print('Error: bad password')
                    break
            elif sp[0]!=lastl:
                pass
            else:
                print('Error: no such user')
    except:
        print('Error: no such user')
        
def SetDomain(name, domain):
    try:
        fdd=open("domains.txt", "r")
        lines=fdd.readlines()
        lastd=last_domain()
        for line in lines:
            line=line.strip()
            spd=line.replace("--", ", ").split(", ")
            if spd[0]==domain:
                if name in spd:
                    print('Success')
                    break
                else:
                    if spd[-1].replace("\n", "")=="":
                        newline=line+name+"\n"
                    else:
                        newline=line+", "+name+"\n"
                    line=line+"\n"
                    fdd.close()
                    #lines=lines.strip().replace(line, newline)
                    fdd=open("domains.txt", "w")
                    
                    for i in range(len(lines)):
                        if lines[i] == line:
                            lines[i]=newline
                            fdd.write(lines[i])
                        else:
                            fdd.write(lines[i])
                    print("Success")
                    break
            elif spd[0]!=lastd:
                pass
            else:
                fd=open("domains.txt", "a")
                fd.write(domain+"--"+name+"\n")
                fd.close()
                print('Success')
 
    except:
        fd=open("domains.txt", "a")
        fd.write(domain+"--"+name+"\n")
        fd.close()
        print('Success')


def DomainInfo(domain):
    try:
        fdi=open("domains.txt", "r")
        lines=fdi.readlines()
        lastd=last_domain()
        for line in lines:
            line=line.strip()
            spd=line.replace("--", ", ").split(", ")
            if spd[0]==domain:
                if spd[1]!="":
                    for elem in spd[1:]:
                        print(elem)
                    break
                else:
                    break
            elif spd[0]!=lastd:
                pass
            else:
                print("Error: domain doesn't exist")
                break
    except:
        print("Error: domain doesn't exist")

def SetType(obj, tp):
    try:
        fds=open("types.txt", "r")
        lines=fds.readlines()
        las=last_tp()
        for line in lines:
            line=line.strip()
            spt=line.replace("--", ", ").split(", ")
            if spt[0]==tp:
                if obj in spt:
                    print("Success")
                    break
                else:
                    if spt[-1].replace("\n", "")=="":
                        nl=line+obj+"\n"
                    else:
                        nl=line+", "+obj+"\n"
                    line=line+"\n"
                    fds.close()
                    #lines=lines.strip().replace(line, newline)
                    fds=open("types.txt", "w")
                    for i in range(len(lines)):
                        if lines[i] == line:
                            lines[i]=nl
                            fds.write(lines[i])
                        else:
                            fds.write(lines[i])
                    print("Success")
                    fds.close()
                    break
            elif spt[0]!=las:
                pass
            else:
                fds=open("types.txt", "a")
                fds.write(tp+"--"+obj+"\n")
                fds.close()
                print('Success')
    except:
        fds=open("types.txt", "a")
        fds.write(tp+"--"+obj+"\n")
        fds.close()
        print('Success')
        
def TypeInfo(tp):
    try:
        fdii=open("types.txt", "r")
        lines=fdii.readlines()
        las=last_tp()
        for line in lines:
            line=line.strip()
            spt=line.replace("--", ", ").split(", ")
            if spt[0]==tp:
                if spt[1]!="":
                    for elem in spt[1:]:
                        print(elem+"_"+spt[0])
                    break
                else:
                    break
            elif spt[0]!=las:
                pass
            else:
                print("Error: type doesn't exist")
                break
    except:
        print("Error: type doesn't exist")


def AddAccess(op,domain,tp):
    try:
        ac=open("access.txt", "r")
        lines=ac.readlines()
        lastln=last_ln()
        ac.close()
        for line in lines:
            line=line.strip()
            acc=line.replace("--", " -> ").split(" -> ")
            if acc[0]==domain and acc[1]==tp and acc[2]==op:
                break
            elif line!=lastln.replace("\n", ""):
                pass
            else:
                ac=open("access.txt", "a")
                ac.write(domain+" -> "+tp+"--"+op+"\n")
                ac.close()
                
                try:
                    ck=open("domains.txt", "r")
                    domains=ck.readlines()
                    ck.close()
                    lastd=last_domain()
                    for line in domains:
                        line=line.strip()
                        dn=line.replace("--", ", ").split(", ")
                        if dn[0]==domain:
                            break
                        elif dn[0]!=lastd:
                            pass
                        else:
                            ck=open("domains.txt", "a")
                            ck.write(domain+"--"+"\n")
                            ck.close()
                except:
                    ck=open("domains.txt", "a+")
                    ck.write(domain+"--"+"\n")
                    ck.close()
                
                try:
                    ck2=open("types.txt", "r")
                    types=ck2.readlines()
                    ck2.close()
                    las=last_tp()
                
                    for line in types:
                        line=line.strip()
                        ty=line.replace("--", ", ").split(", ")
                        if ty[0]==tp:
                            break
                        elif ty[0] != las:
                            pass
                        else:
                            ck2=open("types.txt", "a")
                            ck2.write(tp+"--"+"\n")
                            ck2.close()
                except:
                    ck2=open("types.txt", "a")
                    ck2.write(tp+"--"+"\n")
                    ck2.close()
                
                print("Success")
    except:
        ac=open("access.txt", "a")
        ac.write(domain+" -> "+tp+"--"+op+"\n")
        ac.close()
                        
        try:
            ck=open("domains.txt", "r")
            domains=ck.readlines()
            ck.close()
            lastd=last_domain()
            for line in domains:
                line=line.strip()
                dn=line.replace("--", ", ").split(", ")
                if dn[0]==domain:
                    break
                elif dn[0]!=lastd:
                    pass
                else:
                    ck=open("domains.txt", "a")
                    ck.write(domain+"--"+"\n")
                    ck.close()
        except:
            ck=open("domains.txt", "a+")
            ck.write(domain+"--"+"\n")
            ck.close()
                
        try:
            ck2=open("types.txt", "r")
            types=ck2.readlines()
            ck2.close()
            las=last_tp()
                
            for line in types:
                line=line.strip()
                ty=line.replace("--", ", ").split(", ")
                if ty[0]==tp:
                    break
                elif ty[0] != las:
                    pass
                else:
                    ck2=open("types.txt", "a")
                    ck2.write(tp+"--"+"\n")
                    ck2.close()
        except:
            ck2=open("types.txt", "a")
            ck2.write(tp+"--"+"\n")
            ck2.close()
        print("Success")
                
                
def CanAccess(op, user, obj):
    try:
        ckk=open("domains.txt", "r")
        d_list=[]
        lines=ckk.readlines()
        lastd=last_domain()
        ckk.close()
        for line in lines:
            line=line.strip()
            namez=line.replace("--", ", ").split(", ")
            if user in namez[1:]:
                d_list.append(namez[0])
        if d_list==[]:
            print("Error: access denied")
        else:
            typp=[]
            ckk=open("types.txt", "r")
            lines=ckk.readlines()
            ckk.close()
            for line in lines:
                line=line.strip()
                typ=line.replace("--", ", ").split(", ")
                if obj in typ[1:]:
                    typp.append(typ[0])
            if typp==[]:
                print("Error: access denied")
            else:
                ckk=open("access.txt", "r")
                lines=ckk.readlines()
                ckk.close()
                last_acc=last_ln()
                last_ac=last_acc.replace("\n", "")
                bre=0
                for line in lines:
                    line=line.strip()
                    acc=line.replace("--", " -> ").split(" -> ")
                    for i in d_list:
                        for j in typp:
                            if i==acc[0] and j==acc[1] and op==acc[2]:
                                bre=1
                                break
                    if bre==1:
                        print("Success")
                        break
                    elif last_ac!=line:
                        pass
                    else:
                        print("Error: access denied")
    except:
        print("Error: access denied")
                
            
    
    
if __name__ == "__main__":
    try:
        if sys.argv[1]=="AddUser":
            if sys.argv[2]=="":
                print('Error: username missing')
        #elif sys.argv[3]=="":
            #print('Error: password missing')
            elif len(sys.argv)>4:
                print("Error: too many arguments")
            else:
                AddUser(sys.argv[2],sys.argv[3])
            
        elif sys.argv[1]=="Authenticate":
            if len(sys.argv)>4:
                print("Error: too many arguments")
            else:
                Authenticate(sys.argv[2],sys.argv[3])
        
        
        elif sys.argv[1]=="SetDomain":
            if sys.argv[3]=="":
                print("Error: missing domain")
            elif len(sys.argv)>4:
                print("Error: too many arguments")
            elif check_user(sys.argv[2])==2:
                print("Error: no such user")
            else:
                SetDomain(sys.argv[2],sys.argv[3])
            
            
        elif sys.argv[1]=="DomainInfo":
            if sys.argv[2]=="":
                print("Error: missing domain")
            elif len(sys.argv)>3:
                print("Error: too many arguments")
            else:
                DomainInfo(sys.argv[2])
        
        elif sys.argv[1]=="SetType":
            if sys.argv[2]=="":
                print("Error: missing Object")
            
            elif sys.argv[3]=="":
                print("Error: missing Type")
            elif len(sys.argv)>4:
                print("Error: too many arguments")
            else:
                SetType(sys.argv[2],sys.argv[3])
                
        elif sys.argv[1]=="TypeInfo":
            if sys.argv[2]=="":
                print("Error: missing Type")
            elif len(sys.argv)>3:
                print("Error: too many arguments")
            else:
                TypeInfo(sys.argv[2])
        elif sys.argv[1]=="AddAccess":
            if sys.argv[2]=="" or sys.argv[2]=="null":
                print("Error: missing operation")
            elif sys.argv[3]=="" or sys.argv[3]=="null":
                print("Error: missing domain")
            elif sys.argv[4]=="" or sys.argv[4]=="null":
                print("Error: missing type")
            elif len(sys.argv)>5:
                print("Error: too many arguments")
            else:
                AddAccess(sys.argv[2],sys.argv[3],sys.argv[4])
                
        elif sys.argv[1]=="CanAccess":
            if sys.argv[2]=="":
                print("Error: access denied")
            elif sys.argv[3]=="":
                print("Error: access denied")
            elif sys.argv[4]=="":
                print("Error: access denied")
            elif check_user(sys.argv[3])==2:
                print("Error: access denied")
            elif len(sys.argv)>5:
                print("Error: too many arguments")
            else:
                CanAccess(sys.argv[2],sys.argv[3],sys.argv[4])
            
        else:
            print('Error: not correct function name')
    except:
        print("Error: missing arguments")

