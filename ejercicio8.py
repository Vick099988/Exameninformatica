
print ("SCRIP QUE IDENTIFICA LOS MULTIPLOS DE 3 O 5")
n = int(input("Ingresa un numero multiplo de 5 o 3: "))

if n % 5 == 0:
    print("el numero ",n," es multiplo de 5 pero no de 3")

if n % 3 == 0:
    print("el numero ",n," es multiplo de 3 pero no de 5")

if n < 5 or 3== 0:
    print(f'{n} no es un numero multiplo de 3 o 5')
