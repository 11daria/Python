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

p=int(input("Enter p: "))
q=int(input("Enter q: "))
n=p*q
#Читает текст из файла
C=[]
with open('C:\\Users\\Pingvin\\Desktop\\result.txt', 'r') as f1:
    for line in f1:
        C.append(int(line.strip('\n')))
f1.close()
#print(C)

#4 системы уравнение
# вычисляем степень
k=(p+1)/4
l=(q+1)/4

#s*q+t*p=NSD(q,p) a=q(q**-1modp) b=q(q**-1modg)
nsd,s,t=evklid(q,p)
a=q*s
b=p*t
result=[]
#f = open('C:\\Users\\Pingvin\\Desktop\\text.txt', 'w')
for i in range(len(C)):
    m1 = power1(C[i], k, n) # n - открытый ключ
    m3 = power1(C[i], l, n)
    M1 = (a * m1 + b * m3) % n
    M2 = (a * m1 - b * m3) % n
    M3 = (-a * m1 + b * m3) % n
    M4 = (-a * m1 - b * m3) % n
    if M1 < 0:
        M1 = M1 + n
    result.append(str(M1))
    if M2 < 0:
        M2 = M2 + n
    result.append(str(M2))
    if M3 < 0:
        M3 = M3 + n
    result.append(str(M3))
    if M4 < 0:
        M4 = M4 + n
    result.append(str(M4))
    print(M1, M2, M3, M4)
#   for element in result:
#        f.write(str(element))
#        f.write('\n')
#f.close()


marker=input("First letter: ")

for i in range(len(result)):
    f = open('C:\\Users\\Pingvin\\Desktop\\text.txt', 'w')
    if result[i][0] == marker:
        f.write(str(result[i]))


