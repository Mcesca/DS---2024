altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = peso / (altura ** 2)
imc = round = round (imc, 2)

print(f"O seu IMC é: {imc}")

if imc > 30:
    print("Cuidado com a saude")
elif imc < 29:
    print("Tudo OK")