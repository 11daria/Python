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

"""Витягую з алфавіту букви яких нема в ключи"""
alph = []
for start_ascii in range(97,123):
    if chr(start_ascii) in key:
        continue
    else:
        alph.append(chr(start_ascii))
print(alph)

"""Створюєм матрицю разом з ключем"""
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

message="forexample"
#message="fx"
#message="tree"
"""Перевірка на подвоєння букв"""
message=''.join([message[i] for i in range(len(message)-1) if message[i+1]!= message[i]]+[message[-1]])
print(message)

"""Перевірка на парність букв/ У випадкунепарності додати х"""
if not len(message)%2==0:
    message=message+"x"

"""Розбиваємо на букви пари"""
n = 2
ab=[message[i:i+n] for i in range(0, len(message), n)]
print(ab)

"""Індекси повідомлення букв повідомлення """
lst=[]
for elem in message:
    for i in matrix:
        if elem in i:
            lst.append(matrix.index(i)) #рядки
            lst.append(i.index(elem))  #стовпці
print(lst)
"""Розбиваємо індекси на списки по 4"""
ab=[lst[i:i+4] for i in range(0, len(lst), 4)]
print(ab)


for i in ab:
    if i[0]==i[2]:                  #якщо в одному рядку
        i[1],i[-1]=i[1]+1,i[-1]+1   #індекси стовпців збільшуються на 1
        if i[-1]>len(i):            # якщо останній індекс >4
            i[-1]=i[-1]-len(i)-1    # [0, 4, 0, 5] => 5-4-1=0 => [0, 4, 0, 0]
    elif i[1]==i[-1]:               #якщо в одному стовпці
        i[0],i[2]=i[0]+1,i[2]+1     #індекси рядків збільшуються на 1
        if i[2]>len(i):             #якщо останній індекс >4
            i[2]=i[2]-len(i)-1      #[2, 2, 5, 2] => 5-4-1=0 => [2, 2, 0, 2]
    else:
        i[1],i[-1]=i[-1],i[1]
print(ab)

"""Створюємо список індексів"""
ind=[]
for i in ab:
    for l in i:
        ind.append(l)
print(ind)

"""Групуємо їх по 2"""
ind2=[ind[i:i+2] for i in range(0, len(ind), 2)]
print(ind2)

shifr=""
for i in ind2:
    shifr+=matrix[i[0]][i[-1]]
print(shifr)

