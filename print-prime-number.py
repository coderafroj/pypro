def printPrimeNumber(n):
    for num in range(1,n):
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                print(num)
n=int(input("Enter  number to print  prime number:-\n"))
printPrimeNumber(n)
