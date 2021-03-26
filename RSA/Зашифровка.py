def power1(x,d,n): # x**d(modn) шифрування рса
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

print(power1(1,13,5))

def evklid(a, b):
    r1 = a
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    r = r1 % r2
    while r != 0:
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
    return r2, s2, t2

#print(evklid(161,28))

def isPrime(n):
    if n%2==0:
        return False
    d=3
    while d*d<=n and n%d!=0:
        d+=2
    return d*d>n
#print(isPrime(23))

def hen_key():  #Abonent a
    p=int(input("Print p: "))
    while isPrime(p) == False:
        p = int(input("Enter p again:   "))
    q=int(input("Print q: "))
    while isPrime(q) == False:
         q = int(input("Enter again q: "))

    n = p * q
    el = (p-1)*(q-1)
    print(el,"elier")
    e = int(input("відкритий ключ Ейлера е: "))
    nsd, ss, tt = evklid(el, e)
    while nsd != 1:
        e = int(input("відкритий ключ Ейлера е знову: "))
        nsd, ss, tt = evklid(el, e)
    if tt < 0:
        tt = tt + el  #d=e**-1(mod el)
    print(tt ,"d")
    return n, e


m=[]
def vved_t():
    file1=open('C:\\Users\\Pingvin\\Desktop\\text.txt', 'r')
    a = file1.read()
    m.append(int(a))
    file1.close()
    return m



#print(vved_t())

def shyfr(m,e,n):
    f=open('C:\\Users\\Pingvin\\Desktop\\result.txt', 'w')
    for i in range(len(m)):
        c=power1(m[i],e,n) #e -stepin n - modul
        f.write(str(c))
        f.close()
    return c

n,e = hen_key()
m=vved_t()  #B
print(shyfr(m,e,n))
# p=11 q=5 e=7 d=23 c=5 m=c**d(modn)



