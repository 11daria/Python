def power1(x, d, n): # x**d(modn)
    d2=[] #d в двійковій системі числення
    while d != 0: #Поки показник степення не буде рівний 0
        d2.append(d % 2) #До списку d2 додавати остачу від ділення на 2
        d = d // 2
    d2.reverse() #Функція повороту для списку
    # Аналізуємо значення залежно від розряду
    z = 1 #Присвоюється 1
    for k in range(len(d2)): #Цикл в якому перевіряється якою формулою користуватись
        z = z * z
        if d2[k] == 1:
            z = z * x
        z = z % n
    return z

def isPrime(n): #Функція для перевірки чи просте число
    if n % 2 == 0: #Спочатку перевіряється парність
        return False
    d = 3 #Перебір непарних дільників
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def hen_key(): #Генерація ключів
    p=int(input("Print p: "))
    while isPrime(p) == False:
        p = int(input("Enter p again:   ")) #Просте число яке тримають в секреті
    q=int(input("Print q: "))
    while isPrime(q) == False:
         q = int(input("Enter again q: ")) #Просте число яке тримають в секреті
    n = p * q #Добуток двох простих чисел
    d = int(input("Print key d: ")) #Секретний ключ
    return n,d

m=[] #Зчитування зашифрованого повідомлення
def vved_t():
    f=open("C:\\Users\\Pingvin\\Desktop\\RSA_Result.txt" , "r",encoding='utf-8')
    text=f.read()
    print(text)
    for i in text:
        m.append(ord(i)) #Переведення букв в числовий формат відповідно до ASCII Table
    f.close()
    return m

def deshyfr(m,d,n): #Функція розшифрування
    f=open('C:\\Users\\Pingvin\\Desktop\\RSA_Deshyfr.txt', 'w', encoding='utf-8' )
    for i in range(len(m)): #Кожен символ в повідомлені
        c=power1(int(m[i]), d, n) #підносимо до степення d, обчислюємо за модулем n, тобто застосовуїмо першу функцію
        f.write(str(chr(c))) #Переведення чисел в букви
    f.close()
    return c

n,d = hen_key()
vved_t()
deshyfr(m,d,n)
f=open("C:\\Users\\Pingvin\\Desktop\\RSA_Deshyfr.txt" , "r",encoding='utf-8')
print(f.read())