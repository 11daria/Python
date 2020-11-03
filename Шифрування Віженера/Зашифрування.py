file1=open('C:/Users/Pingvin/Desktop/text_en.docx', 'r')
message=file1.read()
file1.close()
print("Повідомлення:",message)

file1=open('C:/Users/Pingvin/Desktop/vig_key.docx', 'r')
key=file1.read()
file1.close()
print("Ключ:", key)

len_key=len(key)
print("Довжина ключа:",len_key)
len_message=len(message)
print("Довжина повідомлення:",len_message)

len_key1=5 #Перша довжина ключа
stroka1=''
j1=0
while len_key1<=len_key: #Цикл буде виконуватись поки довжина ключа не стане 9, тобто кількість зашифрування періодами 5,6,7,8,9
    for i in range(len_message):
        kod=ord(message[i]) #код літери в повідомлені
        kod_key=ord(key[j1]) #код літери ключа
        stroka1=stroka1+chr((kod+kod_key)%128)
        j1=j1+1
        if j1==len_key1:
            j1=0
    message=message[:0]+stroka1[0:]  #Для продовження шифрування в циклі змінюємо вхідне повідомлення на зашифроване попереднє

    stroka1=stroka1[:0]  #Стираємо строку аби повідомлення не додавалося в кінець попереднього
    len_key1+=1
print("Довжина зашифрованого повідомлення:",len(message))
print(message)
file1=open('C:/Users/Pingvin/Desktop/zash_text.docx', 'w')
t=file1.write(message)
file1.close()
