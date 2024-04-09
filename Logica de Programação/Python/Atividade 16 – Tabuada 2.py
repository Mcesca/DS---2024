letra = 's'
while letra == 's':

    Inicio = int(input('Tabuada de qual número: '))
    fim = int(input('Começar a tabuada com qual valor: '))
    t = int(input('Fazer a tabuada até qual valor'))

    for i in range (fim, t+1):
        print(Inicio*i)

    letra = input('Deseja continuar? [s/n]: ')


