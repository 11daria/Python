import math
from itertools import combinations

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

key = [] #close key
with open('C:\\Users\\Pingvin\\Desktop\\key_rukzak.txt', 'r') as f:
    for line in f:
        for num in line.strip().split(" "):
            key.append(int(num))
f.close()
print(key)
len_key=len(key)
#m=[]
file1=open('C:\\Users\\Pingvin\\Desktop\\text_rukzak.txt', 'r')
m=file1.read()
#for i in a:
#    m.append(i)
file1.close()
print("message",m)

binary=''.join(format(ord(x), 'b') for x in m)
print(binary)
binary=list(binary)
binary1=[]
for i in binary:
    binary1.append(int(i))
print("binary1:" ,binary1)
print(len(binary1))
if len(binary1)%len(key)!=0:
    a=len(key)-(len(binary1)%len(key))
    binary1=[0]*a+binary1

print(binary1)
print(len(binary1))

sum_key=sum(key)
print(sum_key)


m=int(input("Enter numb that m>s: "))
while (m<sum_key):
    m=int(input("Enter numb that m>s again: "))
n=int(input("Enter n: "))
nsd, s, t=evklid(m, n)
while (nsd!=1):
    n=int(input("Enter n again: "))
    nsd, s, t = evklid(m, n)
if (t<0):
    t=t+m
print("t= ",t)
key_z=[]
for i in key:
    key_z.append((n*i)%m) #open key
print("key_z",key_z)

len_key_z=len(key_z)
ab=[binary1[i:i+len_key] for i in range(0, len(binary1), len_key)]
print(ab)
stroka=[]
for i in ab:
    str1=[]
    for j in range(len(i)-1):
        if i[j]==1:
            str1.append(key_z[j])
    stroka.append(sum(str1))
print(stroka)

print("Розшифрування")
n1=1
while n*n1%m!=1:
    n1+=1
print("n1",n1)

lst_sum=[] #271*61mod105
for i in stroka:
    lst_sum.append((n1*i)%m)
print("lst_sum",lst_sum)

dodanok=[] #розподіл на доданки
for r in lst_sum:
    for i in range(0,len(key)):
        for var in combinations(key,i ):
                 if sum(var) == r:
                     dodanok.append(var)
print(dodanok)
lst_ind1=[]
for x in dodanok:
    lst_ind=[]
    for n in range(len(x)):
        lst_ind.append(key.index(x[n]))
    lst_ind1.append(lst_ind)
print(lst_ind1)

lst1=[]
for i in lst_ind1:
#    print(i)
    lst=[]
    for j in range(0,len(key)):
        if j in i :
            lst.append(1)
        else:
            lst.append(0)
    lst1.append(lst)
print(lst1)
text_message=''

for i in lst1:
    for j in i:
        text_message=text_message+str(j)
b=int(text_message)

for x in range(0, len(str(b)), 7):
    print(str(b)[x:x+7])




