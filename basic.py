def myfun(a,b):
    if(b==1 or b==0):
        return a*1
    else:
        return a*myfun(a,b-1)

print(myfun(2,5))


def myfun1(n):
    if(n==0):
        return
    else:
        myfun1(n - 1)
        print(n,end=" ")

myfun1(10)

def fib(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return fib(n-1)+fib(n-2)

print(fib(0))

def spell(l1,num,st):
    if(num!=0):
        n1=num%10
        st=l1[n1-1]+" "+st
        spell(l1,num//10,st)
    else:
        print(st)
        return st



list=["one","two","three","four","five","six","seven","eight","nine"]
num=421
st=""
st1=spell(list,num,st)
#st1=st1.strip()
print(st1)
