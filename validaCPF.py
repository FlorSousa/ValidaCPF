#VALOR = 11 - (n%11)
#se VALOR > 9 = 0
#se VALOR < 9 = VALOR

def DefineDigito(ListaNumeros):
    cont = 10
    atualValor = 0

    for k in ListaNumeros[0]:
        atualValor += int(k)*cont
        cont -= 1

    for k in ListaNumeros[1]:
        atualValor += int(k)*cont
        cont -= 1    
        
    for k in ListaNumeros[2]:
        atualValor += int(k)*cont
        cont -= 1
        
    valor = 11 - (atualValor%11)

    if(valor > 9 ):
        digitoPrimeiro = 0
        return DefineSegundo(ListaNumeros,digitoPrimeiro)
    else:
        digitoPrimeiro = valor
        return DefineSegundo(ListaNumeros,digitoPrimeiro)
        

def DefineSegundo(lista,primeiro):
    cont = 11
    atualValor = 0

    for k in ListaNumeros[0]:
        atualValor += int(k)*cont
        cont -= 1

    for k in ListaNumeros[1]:
        atualValor += int(k)*cont
        cont -= 1    
        
    for k in ListaNumeros[2]:
        atualValor += int(k)*cont
        cont -= 1
    
    for k in ListaNumeros[3]:
        atualValor += int(k)*cont
        cont -= 1
        break
    
    valor = 11 - (atualValor%11)
    
    if(valor > 9 ):
        digitoSegundo = 0
        return DefineSegundo(ListaNumeros,digitoPrimeiro)
    else:
        digitoSegundo = valor
        return Check(digitoSegundo,primeiro,ListaNumeros)

def Check(segundo,primeiro,lista):
    numeros = [primeiro,segundo]
    cont = 0
    Num = False
    Ndois = False
    
    for k in numeros:
        if(k == int(lista[3][cont]) and cont == 0):
            Num = True
            cont += 1
        if(k == int(lista[3][cont]) and cont == 1):
            Ndois = True
        
    if(Num == True and Ndois == True):
        return "Valido"
    else:
        return "Invalido"
       
        
   

cpfString = input("Digite um CPF valido:\n").split(".")
ListaNumeros = [cpfString[0],cpfString[1], cpfString[2].split("-")[0], cpfString[2].split("-")[1]]
print(DefineDigito(ListaNumeros))

