print("1 de dolares a pesos chilenos")
print("2 de pesos chilenos a dolares")
print("3 de dolares a euros")
print("4 de euros a dolares")
print("5 de pesos mexicanos a dolares")
print("6 de dolares a quetzales")
print("7 de euros a pesos mexicanos")
print("8 de dolares a pesos dominicanos")
print("9 de pesos dominicanos a dolares")
print("10 de Dolar canadiense a Lempira")
print ("")
hl=int(input("coloque aqui opcion"))
print ("")
if hl==1:
    dol1=int(input("introduzca cantidad de dolares"))
    pesc=dol1*756.70
    print ("")
    print ("pesos chilenos=", pesc)
if hl==2:
    pesc1=float(input("introduzca pesos chilenos"))
    dol2=pesc1/756.7
    print("")
    print("dolares=", dol2)
if hl==3:
    dol3=int(input("introduzca cantidad de dolares"))
    euros=dol3*1.18
    print("")
    print("dolares=", euros)
if hl==4:
    euros1=int(input("introduzca dolares"))
    dol4=euros1/1.18
    print("")
    print("euros=", dol4)
if hl==5:
    pesm=int(input("coloque pesos mexicanos"))
    dol5=pesm/22.27
    print("")
    print("dolares=", dol5)
if hl==6:
    dol6=int(input("coloque cantidad de dolares"))
    quetz=dol6/1.13
    print("")
    print("quetzales=", quetz)
if hl==6:
    dol6=int(input("coloque cantidad de dolares"))
    quetz=dol6/1.13
    print("")
    print("quetzales=", quetz)
if hl==7:
    euros7=int(input("coloque cantidad de euros"))
    pesm=euros7*19.97
    print("")
    print("pesos mexicanos=", pesm)
if hl==8:
    dol8=int(input("coloque cantidad de dolares"))
    pesd=dol8*54.95
    print("")
    print("pesos dominicanos=", pesd)
if hl==9:
    pesd9=int(input("coloque pesos dominicanos"))
    dol9=pesd9*0.018
    print("")
    print("dolares=", dol9)
if hl==10:
    lemp10=int(input("coloque cantidad de dolares canadiense"))
    dolc10=lemp10*18.03
    print("")
    print("lempira=", lemp10)

























    print("*******CONVERTIDOR DE UNIDADES*********")
print("1 - Libras a Kilos\n2 - Kilos a Libras\n3- Hectogramo a Decagramo\n4- Decagramos a Gramos\n5- Gramos a Libras\n6- Libras a Decigramo\n7- Decigramos a Centigramo\n8- Centigramos a Miligramo\n9- Miligramos a Kilogramos\n10- Kilogramos a Centigramos\n11")
opcion = int(input("Ingrese la opción de conversión que desea utilizar: "))
resultado = 0
 
if opcion == 1:
    print("Libras a Kilos")
    entrada = float(input("Ingresa la cantidad en Libras: "))
    resultado = round(entrada*0.453592,2)
elif opcion == 2:
    print("Kilos a Libras")
    entrada = float(input("Ingresa la cantidad en Kilogramos: "))
    resultado = round(entrada*2.20462,2)
elif opcion == 3:
    print("Hectogramo a Decagramo")
    entrada = float(input("Ingresa la cantidad en Hectogramos: "))
    resultado = round(entrada*10,2)
elif opcion == 4:
    print("Decagramos a Gramos")
    entrada = float(input("Ingrese la cantidad en Decagramos: "))
    resultado = round(entrada*10,2)
elif opcion == 5:
    print("Gramos a Libras")
    entrada = float(input("Ingrese la cantidad en Gramos: "))
    resultado = round(entrada*0.00220462,2)
elif opcion == 6:
    print("Libras a Decigramos")
    entrada = float(input("Ingrese la cantidad en Libras: "))
    resultado = round(entrada*4535.92,2)
elif opcion == 7:
    print("Decigramos a Centigramos")
    entrada = float(input("Ingrese la cantidad en Decigramos: "))
    resultado = round(entrada*10,2)
elif opcion == 8:
    print("Centigramos a Miligramos")
    entrada = float(input("Ingrese la cantidad en Cemtigramos: "))
    resultado = round(entrada*10,2)
elif opcion == 9:
    print("Miligramos a Kilogramos")
    entrada = float(input("Ingrese la cantidad en Miligramos: "))
    resultado = round(entrada*0.000001,2)
elif opcion == 10:
    print("Kilogramos a Centigramos")
    entrada = float(input("Ingrese la cantidad en Kilogramos: "))
    resultado = round(entrada*100000,2)    

    
    
print("El resultado de la conversión es: {} ".format(resultado))

    
    
