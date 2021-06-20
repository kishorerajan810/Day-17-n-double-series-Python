m,x,y=map(int,input("enter :").split())
n=1
for i in range(1,m):
    a=(n*x)+1
    b=(n*y)+1
    n+=1
    c=(n*x)-1
    d=(n*y)-1
    n+=1
    print(a,b,c,d,end=" ")
