qtd_velho_magro= 0
media_id_pequenos= 0
qtd_id_pequenos= 0
por_corolho_azul= 0
ruivos_humildes= 0

for i in range (20):
    idade = int (input ("adade: "))
    peso = float(input("peso: "))
    altura= float(input("altura: "))
    corolho= input("cor do olho:")
    corcabelo= input("cor do cabelo: ")

    if idade > 50 and peso < 60:
        qtd_velho_magro += 1
    if altura < 1.50 :
        qtd_id_pequenos += 1
        media_id_pequenos += idade
    if corolho == "A":
        por_corolho_azul += 1
    if corcabelo == "R" and corolho != "A":
        ruivos_humildes += 1 

media_id_pequenos /= qtd_id_pequenos
por_corolho_azul = (por_corolho_azul / 100) * 20 

print ("quantidade de velhos magros: %d"% (qtd_velho_magro))
print ("media da idade dos pequenos: %d"% (media_id_pequenos))
print ("porcentagem de pessoas com olhos azuis: %d"% (por_corolho_azul))
print ("quantidade de ruivos humildes: %d"% (ruivos_humildes))