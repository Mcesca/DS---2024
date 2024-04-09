letra = 's'
while letra == 's':

    n1 = float(input('Qual o valor?'))
    tx = float(input('A taxação atual:'))
    print('[1] Real para dolar')
    print('[2] Dolar para real')
    inf = float(input('Qual será a conversão?'))

    if inf == 1:
        print('USD: ', (n1 / tx))
    else:
        print('BRL: ', (tx * n1))

    letra = input('Deseja continuar? [S/N]: ')