import math


def evklid(a, b):
    r1 = a
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    r = r1 % r2
    while (r != 0):
        q = r1 // r2
        s = s1 - q * s2
        t = t1 - q * t2
        r1 = r2
        r2 = r
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t
        r = r1 % r2
    return r2, t2, s2

def read_key():
    key = []
    with open('C:\\Users\\Pingvin\\Desktop\\key_rukzak.txt', 'r') as f:
        for line in f:
            for num in line.strip().split(" "):
                key.append(int(num))
    f.close()
    return key

def vved_t():
    file1=open('C:\\Users\\Pingvin\\Desktop\\text_rukzak.txt', 'r')
    m=file1.read()
    file1.close()
    return m

def gen_sec(key):
    print("s=", sum(key))
    m=int(input("Enter numb that m>s: "))
    while (m<sum(key)):
        m=int(input("Enter numb that m>s again: "))
    n=int(input("Enter n: "))
    nsd, s, t=evklid(m, n)
    while (nsd!=1):
        n=int(input("Enter n again: "))
        nsd, s, t = evklid(m, n)
    if (t<0):
        t=t+m
    print("t= ",t)

    return m,n,t


def key_open(key,m,n):
    key_z=[]
    for i in key:
        key_z.append((n*i)%m)
    print(key_z)
    return key_z

def binar(d,k):
    d2=[]
    for i in range(k):
        d2.append(d%2)
        d=d//2
    d2.reverse()
    return d2

def desyat(b,k):
    s=0
    for i in range(k):
        s=s+b[i]*pow(2,k-i-1)
    return s

def shyfr():
    text=vved_t()
    key=read_key()
    m,n,n_ob=gen_sec(key)
    key_v=key_open(key,m,n)
    dov=len(key)
    b=[]
    for sym in text:
        b.append(binar(ord(sym),7))
    print((b))
    text_b=sum(b,[])
    print(text_b)

    k=math.ceil(len(text_b)/dov)
    if k*dov>len(text_b):
        for i in range(k*dov-len(text_b)):
            text_b.append(0)

    c=[]
    f1=open('C:\\Users\\Pingvin\\Desktop\\file_rukzak.txt', 'w')
    for i in range(k):
        nar=text_b[i*dov:(i+1)*dov]
        d=0
        for j in range(dov):
            d=d+key_v[j]*nar[j]
        f1.write(str(d))
        f1.write("")
        c.append(d)
    f1.close()

    return c
c=shyfr()
print(c)

#Розшифрування
def gen(key):
    print("s=", sum(key))
    m=int(input("Enter numb that m>s: "))
    while (m<sum(key)):
        m=int(input("Enter numb that m>s again: "))
    n=int(input("Enter n: "))
    nn=1
    while n*nn%m!=1:
        nn+=1
    n1.append(nn)
#    print("nn",nn)
    return nn,m
n1,m=(gen(read_key()))

lst_sum=[]
for i in c:
    lst_sum.append((n1*i)%m)
print(lst_sum)