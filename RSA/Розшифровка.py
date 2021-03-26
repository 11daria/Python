def power1(x,d,n): # x**d(modn)
    d2=[]
    while d!=0:
        d2.append(d%2)
        d=d//2
    d2.reverse()
    z = 1
    for k in range(len(d2)):
        z = z * z
        if (d2[k]==1): z=z*x
        z = z % n
    return z

def isPrime(n):
    if n%2==0:
        return False
    d=3
    while d*d<=n and n%d!=0:
        d+=2
    return d*d>n

def hen_key():  #Abonent a
    p=int(input("Print p: "))
    while isPrime(p) == False:
        p = int(input("Enter p again:   "))
    q=int(input("Print q: "))
    while isPrime(q) == False:
         q = int(input("Enter again q: "))
    n = p * q
    d = int(input("Print key d: "))
    return n,d

def vved_t():
    file1=open('C:\\Users\\Pingvin\\Desktop\\result.txt', 'r')
    m = file1.read()
    file1.close()
    return m


def shyfr(m,d,n):

    m=[1570]
    f=open('C:\\Users\\Pingvin\\Desktop\\text.txt', 'w')
    for i in range(len(m)):
        c=power1(m[i],d,n) #e -stepin n - modul
        f.write(str(c))
        f.close()
    return c

n,d = hen_key()
m=vved_t()  #B
print(shyfr(m,d,n))
# p=47 q=71 e=79 m=688