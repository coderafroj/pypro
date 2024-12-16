l=[2,4,16,25,36,49,64,81,100,36]
x=int(input("Enter number to search to list"))
idx=0
while idx<len(l):
    if l[idx]==x:
        print("finding at-",idx)
    else:
        print("finding...")
    
    idx+=1
    
