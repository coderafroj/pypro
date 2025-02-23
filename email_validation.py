email=input("Enter Your Email:-")
q,w,d=0,0,0
#min len 6
if len(email)>=6:
    #first letter alpha hi ho
    if email[0].isalpha():
        #ek @ ho
        if "@" in email and email.count("@")==1:
            #last se three ya forth postion per . dot ho
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        q=1
                    elif i.isalpha():
                        if i==i.upper():
                            w=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if q==1 or w==1 or d==1:
                      print("wrong email")
                else:
                      print("right email👌👌")
            else:
                print("invalid email")
        else:
            print("@ compulsort")
    else:
        print("first letter alpha")
        
else:
    print("minimum legth 6 charecror")