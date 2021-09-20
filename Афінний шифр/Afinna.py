import numpy as np
s=np.array([[5],[6]])
key_a = np.array([[1,2], [3,5]]) #1235 матриця
print(key_a)
print(s)


w=round(np.linalg.det(key_a)) #детермінант key_a
print("визначник: ",w)

a_ob=np.linalg.inv(key_a)*w #обернена матриця key помножена на детермінант w
print(a_ob)

add_alph=[" ", ".", ","]
a = ord('а')
alph=''.join([chr(i) for i in range(a,a+32)]) #Алфавіт
print("алфавіт: ",alph) #алфавіт

lst_alph = list(alph) #список з алфавіту
for i in add_alph:
    lst_alph.append(i)
print(lst_alph)
n=len(lst_alph) #довжина алфавіту
print("довжина алфавіту: ",n)

def evklid(a,b):
     r1=a
     r2=b
     s1=1
     s2=0
     t1=0
     t2=1
     r=r1%r2
     while (r!=0):
         q=r1//r2
         s=s1-q*s2
         t=t1-q*t2
         r1=r2
         r2=r
         s1=s2
         s2=s
         t1=t2
         t2=t
         r=r1%r2
     return r2,t2,s2
func=evklid(w,n)  #Застосування розширеного алгоритма Евкліда для пошуку оберненого значення детермінанта
print(func)

w_ob=func[2] #обернене значення до детермінанта w на 2 позиції в списку
print("Обернений елемент: ",w_ob)

main_matrix=(a_ob*w_ob)%n #Обчислення розшифровуючого ключа за допомогою оберненої матриці та оберненого детермінанта
print(main_matrix)

d = {a: lst_alph[a] for a in range(35)}  #Створення словника номерованих літер
print("Словник",d)


f1=[]
f=open("C:\\Users\\Pingvin\\Desktop\\afin_text.txt" , "r",encoding='utf-8') #Зчитування повідомлення для шифрування
text=f.read()
if len(text)%len(key_a)==1: #Якщо довжина повідомлення менша ніж порядок даної матриці ключа, то додати "a"
    word=text+"а"
else:
    word=text  #Інакше залишити текст без змін
print("Текст повідомлення для зашифрування: ",word)

word1=list(word) #Перетворення строки в список сиволів повідомлення
print("Список символів повідомлення: ",word1)

len_main_matrix=len(main_matrix) #Визначення довжини матриці обчислювального ключа, тобто основної
print("Довжина основної матриці: ",len_main_matrix)

word_k=[] #Список переведеного повідомлення в числовий формат відповідно до словника
for x in range(len(word)): #Для x в діапазоні довжини повідомлення -1
    for key,value in d.items():
        if word[x] in value: #Якщо буква повідомлення є в значеннях словника
            k=key
            word_k.append(k) #То необхідно додати ключ словника в список, тобто числове значення букви повідомлення відповідно до словника

print(word_k)

ab=[word_k[i:i+len_main_matrix] for i in range(0, len(word_k), len_main_matrix)] #Поділ числових значень утвореного списку по 2 символа
print(ab)

ab=np.array(ab) #Зображення у вигляді матриці
ab=ab.T #Транспонування матриці
print(ab)

bigram=((key_a.dot(ab)+s)%n) #Ключ матриця множиться на матрицю числових значень повідомлення + ключ s і все це за модулем довжини алфавіту
print('Bigram:',bigram)

bigram=(bigram.T).tolist() #Зображення транспонованої матриці зашифрованих числових значень повідомлення у вигляді списку
print(bigram)


shifr=[] #Список числових значень зашифрованого повідомлення
for i in range(len(bigram)):
    for j in range(len_main_matrix):
        shifr.append(bigram[i][j])
print(shifr)

result='' #Пошук в словнику літер по ключам, які утворились в результаті шифрування повідомлення
for x in range(len(shifr)):
    t=d[shifr[x]] #Визначення букви по ключу словника
    result=result+t
print(result)


#РОЗШИФРУВАННЯ

#Переведення текстового зашифрованого повідомлення в числовий формат відповідно до словника
word_k1=[]
for x in range(len(result)):
    for key,value in d.items():
        if result[x] in value:
            k=key
            word_k1.append(k)
print(word_k1)

ab1=[word_k1[i:i+len_main_matrix] for i in range(0, len(word_k1), len_main_matrix)] #Поділ числових значень відповідно до довжини матриці, тобто 2
print(ab1)

ab1=np.array(ab1) #Зображення у вигляді матриці
ab1=ab1.T #Транспонування матриці
print(ab1)

bigram1=(main_matrix.dot(ab1-s))%n #Ключ матриця множиться на матрицю числових значень зашифрованого повідомлення - ключ s і все це за модулем довжини алфавіту
print(bigram1)

bigram1=(bigram1.T).tolist() #Зображення транспонованої матриці розшифрованих числових значень повідомлення у вигляді списку
print(bigram1)

shifr1=[] #Cписок числових значень розшифрованого повідомлення
for i in range(len(bigram1)): #В діапазоні кількості біграм
    for j in range(len_main_matrix): #В діапазоні довжини матриці ключа, тобто 2
        if round(bigram1[i][j])==35: #Якщо числове значення після округлення рівне 35 => замінити на 0, оскільки воно виходить за межі довжини словника
            shifr1.append(0)
        else:
            shifr1.append(round(bigram1[i][j])) #В іншому випадку просто додати до списку округленого значення
print(shifr1)

result1=''
for x in range(len(shifr1)): #В діапазоні довжини списку числових значень
    t=d[shifr1[x]] #Співставлення числових значень з буквами відповідно до ключив словника
    result1=result1+t
print(result1) #Результат розшифрування

