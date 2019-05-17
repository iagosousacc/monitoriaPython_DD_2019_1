qtd = 0
mediaIdades = 0

for i in range(7):
    idade = int(input("idade: "))
    peso = float(input("peso: "))
    
    
    
    if peso > 90:
        qtd = qtd + 1
    
    mediaIdades += idade

mediaIdades = mediaIdades // 7

print("Pesam mais que 90: %d" % qtd)
print("Media das idades: %d" % mediaIdades)
