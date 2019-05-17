n = int(input("Informe n: "))

resultado = 1

for i in range(2, n+1):
    resultado += 1.0/i

print("resultado: %f" % resultado)