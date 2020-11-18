file1=open('C:/Users/Pingvin/Desktop/key.docx', 'r')
key=file1.read()
file1.close()
print(key)

key2=""
pt="j"
for letter in key:
    if key.count(letter)>1:
        if not letter in pt:
            pt=pt+letter
            key2=key2+letter
    else:
        if letter!="j":
            key2=key2+letter
#print(key2)

matrix=[]
for i in range(5):
    row=[]
    for j in range(5):
        row.append("a")
    matrix.append(row)
print(matrix)

#start_ascii=97
alph = []
for start_ascii in range(97,123):
    if chr(start_ascii) in key:
        continue
    else:
        alph.append(chr(start_ascii))
print(alph)
a=0
l=0
for j in range(5):
    for m in range(5):
        if l<len(key2):
            matrix[j][m]=key2[l]
            l=l+1
        else:
            if a<25-len(key2):
                matrix[j][m]=alph[a]
                a+=1

print(matrix)
message="hmubwbiret"
#message="mb"
#message="bpbz"
message=''.join([message[i] for i in range(len(message)-1) if message[i+1]!= message[i]]+[message[-1]])
print(message)
if not len(message)%2==0:
    message=message+"x"


n = 2
ab=[message[i:i+n] for i in range(0, len(message), n)]
print(ab)

lst=[]

for elem in message:
    for i in matrix:
        if elem in i:
            lst.append(matrix.index(i))
            lst.append(i.index(elem))
print(lst)

ab=[lst[i:i+4] for i in range(0, len(lst), 4)]
print(ab)


for i in ab:
    if i[0]==i[2]:
        i[1],i[-1]=i[1]-1,i[-1]-1
        if i[-1]>=len(i):
            i[-1]=i[-1]+len(i)-1
    elif i[1]==i[-1]:
        i[0],i[2]=i[0]-1,i[2]-1
        if i[2]>len(i):
            i[2]=i[2]+len(i)-1
    else:
        i[1],i[-1]=i[-1],i[1]
print(ab)


ind=[]
for i in ab:
    for l in i:
        ind.append(l)
print(ind)

ind2=[ind[i:i+2] for i in range(0, len(ind), 2)]
print(ind2)

shifr=""
for i in ind2:
    shifr+=matrix[i[0]][i[-1]]
print(shifr)




