somaalt = 0
jog=int(input("Digite o numero de jogadores:  "))
for i in range(jog):
    altura=float(input("Digite a altura:  "))
    somaalt+=altura
    media=somaalt/jog
    print("A media das alturas é : " ,media)