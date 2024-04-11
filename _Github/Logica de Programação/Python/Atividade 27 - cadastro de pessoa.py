def adicionar_pessoa():
    nome = input('Digite o nome da pessoa: ')
    email = input('Digite o email da pessoa: ')

    with open("pessoas.txt", 'a') as arquivos:
        arquivos.write(f'{nome}, {email}\n')

        print('pessoa cadastrada com sucesso!!!')

def listar_pessoas():
    with open("pessoas.txt", 'r') as arquivos:
        print("pessoas cadastradas: ")
        for linha in arquivos:
            nome, email = linha.strip().split(',')
            print(f'nome: {nome}, email: {email}\n')

#adicionar_pessoa()
listar_pessoas()