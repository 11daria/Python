#Ель-Гамаля
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
    while d*d<=n and n%d!=0 :
        d+=2
    return d*d>n

p= int(input("Enter p: "))
while isPrime(p) == 0:
        p=int(input("Enter p: "))
q=int(input("Enter q: "))
while isPrime(q) == 0:
        q=int(input("Enter q: "))

ka= int(input("Enter ka<p: "))
while ka >= p:
        ka=int(input("Enter ka<p: "))

kb= int(input("Enter kb: "))
while kb>=p:
        kb=int(input("Enter kb: "))
#Yb-open key abonent B
Yb=power1(q,kb,p)
print("yb",Yb)

#C=M+(Yb**ka(modp))
yy=power1(Yb,ka,p)
print("yy",yy)

m=[]
with open("C:\\Users\\Pingvin\\Desktop\\shyfr_gam.txt","r") as f:
    for line in f:
        for num in line.strip().split(" "):
            m.append(int(num))
f.close()
print("m=",m)

#Зашифрування Абонентом В для абонента А
f1=open("C:\\Users\\Pingvin\\Desktop\\deshyfr_gam.txt ","w")
for i in range(len(m)):
    C = m[i] ^ yy
    print("c=",C)
    f1.write(str(C))
    f1.write(" ")
f1.close()