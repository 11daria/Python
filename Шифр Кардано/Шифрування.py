def turn(n,stencil):
    stencil1=[]
    r=0
    for i in range(n):
        stencil1.append([])
        for j in range(n):
            stencil1[i].append([r])
    for i in range(n):
        for j in range(n):
            stencil1[j][n-i-1]=stencil[i][j]
    return stencil1

#open key
size=5
stencil=[]
f=open("C:\\Users\\Pingvin\\Desktop\\key.docx", "r")
ind1=0
for line in f:
    stencil.append([])
    for elem in line.strip().split(" "):
        stencil[ind1].append(int(elem))
    ind1=ind1+1
f.close()
print(stencil)

#open text0
#t="перенаправьтеписьмоивану"
file=open("C:\\Users\\Pingvin\\Desktop\\text0.docx", "r")
t=file.read()
file.close()
print(t)

lst_t=[]
r2="."
for i in range(size):
    lst_t.append([])
    for j in range(size):
        lst_t[i].append(r2)


i1=0
for k in range(4):
    for i in range(size):
        for j in range(size):
            if (stencil[i][j]==1):
                lst_t[i][j]=t[i1:i1+1]
                i1=i1+1
    stencil=turn(size,stencil)
print(lst_t)

lst_t2=""
for i in range(size):
    for j in range(size):
        lst_t2=lst_t2+lst_t[i][j]
print(lst_t2)

a=open("C:\\Users\\Pingvin\\Desktop\\text.docx", "w")
for index in lst_t2:
    a.write(index)
a.close()












