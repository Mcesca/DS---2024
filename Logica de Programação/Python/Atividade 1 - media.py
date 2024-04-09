n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = ((n1 + n2 + n3) / 3)

print(f"A média do aluno é: {round(media, 2)}")

if media >= 7:
    print("Aprovado")
elif media >= 3:
    print("Recuperação")
else:
    print("Reprovado")



