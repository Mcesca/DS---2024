print ('Descubra sua categoria')
jogador = float(input('Digite sua idade: '))

if jogador <= 13:
    print("Sua categoria é Infantil")
elif jogador <= 17:
    print("Sua categoria é Juvenil")
elif jogador > 17:
    print("Sua categoria é Sênior")