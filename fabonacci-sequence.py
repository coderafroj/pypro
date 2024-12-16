def fabonacci(nth):
    a,b=0,1
    for I in range(nth):
        print(a)
        a,b=b ,a+b
terms=int(input("Enter number to print terms of fabonacci:-\n"))
fabonacci(terms)
