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
    if n%2==0 or n%4!=3:
        return False
    d=3
    while d*d<=n and n%d!=0 :
        d+=2
    return d*d>n
#print(isPrime(151))

def hen_key():  #Abonent a
    p=int(input("Enter p: "))
    while isPrime(p) == False:
        p = int(input("Enter p again:   "))
    q=int(input("Enter q: "))
    while isPrime(q) == False:
         q = int(input("Enter again q: "))
    n = p * q
    return n
#print(hen_key())


m=[]
def vved_t():
     file1=open('C:\\Users\\Pingvin\\Desktop\\text.txt', 'r')
     a = file1.read()
     m.append(int(a))
     file1.close()
     return m

d=2
def shyfr(m,d,n):
    f=open('C:\\Users\\Pingvin\\Desktop\\result.txt', 'w')
    for i in range(len(m)):
        c=power1(m[i],d,n) #e -stepin n - modul
        f.write(str(c))
        f.close()
    return c

n = hen_key()
m=vved_t()  #B
print(shyfr(m,d,n))