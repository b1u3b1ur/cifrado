print('''
Este es un programa para encriptar y desencriptar oraciones.
Seleccione lo que desea hacer e ingrese el número correspondiente:
1 - cifrado de numeros a binario;
2 - descifrado de binario a numero;
3 - cifrado de agregado de datos para cadena;
4 - descifrado de agregado de datos para cadena;
5 - cifrado de letras a numeros;
6 - descifrado de numeros a letras;
To exit, enter 0.
''')
question = int(input("¿Que quieres hacer?  "))
while question!=0:
    if question==1:
        nn= int(input("numero a binario"))
        print(format(nn, '0b'))
        question = int(input("¿Que quieres hacer?  "))
    if question==2:
        n= int(input("binario a numero"))
        S=0
        i=0
        print(str(n))
        while n>=1:
            d=n%10
            n= n//10
            S= S+d*pow(2,i);
            i=i+1
        print(str(S))
        question = int(input("¿Que quieres hacer?  "))
    if question ==3:
        a=input("ingrese dato que quiere cifrar")
        xd=input("dato de cifrado")
        x=(a.replace(" ", xd))
        c=(x+x)
        print(c*2)
        question = int(input("¿Que quieres hacer?  "))
    if question==4:
        aa=input("ingrese dato que quiere descifrar")
        x2=(aa.replace(xd," "))
        cb=len(x2)
        bc= ((cb-(cb//2))//2)
        print(x2[0:bc])
        question = int(input("¿Que quieres hacer?  "))
    if question ==5:
        l = (input("Codificar Letras a numeros"))
        n = []
        for i in l:
            n.append(ord(i)-96)
        print(n)
        question = int(input("¿Que quieres hacer?  "))
    if question==6:
        dp= input("Decodificar Letras a numeros")
        print(l)
        question = int(input("¿Que quieres hacer?  "))