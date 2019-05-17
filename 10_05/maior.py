def maior(x, y):
    if x > y:
        return x
    else:
        return y

def menor(x, y):
    if x < y:
        return x
    else:
        return y

def nome():
    return "Iago"
def sobrenome():
    return "Sousa"

def fatorial(n):
        resultado = 1
        for i in range(1,n+1):
                resultado*= i
        return resultado

def somatorio(m):
        soma = 0
        for i in range(1, m+1):
                soma += i
        return soma



def safadeza(dia, mes, ano, nome):
        saf = somatorio(mes) + (ano/100) * (50 - dia)
        anjo = 100 - saf
        print("%s eh %.2f safado e %.2f anjo" % (nome, saf, anjo))






def nomeAlternado():
    for i in range(50):
        print(nome())
        print(sobrenome())



a = int(input("informe um numero: "))
b = int(input("informe um numero: "))

print(maior(a,b))
print(menor(a,b))
print(nome())
print(nomeAlternado())
safadeza(24, 8, 00, "Cintia")
safadeza(16, 6, 00, "Mirella")
safadeza(23, 5, 99, "Carlos")
safadeza(19, 6, 94, "Iago")
safadeza(6, 1, 98, "Almeidao")












