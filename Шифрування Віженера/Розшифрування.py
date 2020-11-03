file1=open('C:/Users/Pingvin/Desktop/zash_text.docx', 'r')
text=file1.read()
file1.close()
print("Зашифрований текст:",text)
file1=open('C:/Users/Pingvin/Desktop/vig_key.docx', 'r')
key=file1.read()
file1.close()
print("ключ:", key)
len_key=len(key)
print("Довжина ключа:",len_key)
len_text=len(text)
print("Довжина шифрованого повідомлення:",len_text)

len_key1=5
stroka=""

stroka1=''
j1=0
while len_key1<=len_key:
    for i in range(len_text):
        kod=ord(text[i])
        kod_key=ord(key[j1])
        stroka1=stroka1+chr((kod-kod_key)%128)
        j1=j1+1
        if j1==len_key1:
            j1=0
    text=text[:0]+stroka1[0:]
    stroka1=stroka1[:0]
    len_key1+=1
print(text)
