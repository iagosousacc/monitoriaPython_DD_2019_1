n = int(input("informe n: "))
maior = n
menor = n

while(n != 0):
    n = int(input("informe n: "))
    if n < 0:
        print("Nao aceitamos numeros negativos")
    else:
        if n > maior and n != 0:
            maior = n
        if n < menor and n != 0:
            menor = n
    
print("Maior: %d\nMenor: %d" % (maior, menor))