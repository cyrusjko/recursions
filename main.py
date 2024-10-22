def headrecurse(n,num):
    if n>num:
        return
    headrecurse(n+1,num)
    print(n)
n=int(input("Enter number of recursions: "))
headrecurse(1,n)