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

a=open("C:\\Users\\Pingvin\\Desktop\\text.docx", "r")
text=a.read()
print(text)

lst_t=[]
r2="."
for i in range(size):
    lst_t.append([])
    for j in range(size):
        lst_t[i].append(r2)
print(lst_t)

n1=0
for i in range(size):
    for j in range(size):
        lst_t[i][j]=text[n1]
        n1=n1+1
print(lst_t)

lst=""
i1=0
for k in range(4):
    for i in range(size):
        for j in range(size):
            if (stencil[i][j]==1):
                lst=lst+lst_t[i][j]
                i1=i1+1
    stencil=turn(size,stencil)
print(lst,'\n')
a=open("C:\\Users\\Pingvin\\Desktop\\text0.docx", "w")
for index in lst:
    a.write(index)
a.close()






