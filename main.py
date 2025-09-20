while True:
    res = ''
    # Menu.
    print('-' * 50)
    print('GERADOR DE TABUADA'.center(50))
    print('-' * 50)
    try:
        # Irá tentar ler um número inteiro, caso não seja ou o número seja menor que 0, será exibido uma mensagem de erro.
        num = int(input('Digite um número: '))
    except:
        print('ERRO! Valor digitado inválido')
    else:
        if num < 0:
            print('ERRO! Valor digitado inválido')
        else:
            # Exibição da tabuada.
            print('-' * 50)
            for c in range(1, 11):
                print(f'{num} x {c} = {num * c}')
            print('-' * 50)
            # Perguntar ao usúario se ele quer continuar, caso sim, o programa continua, caso não, o programa termina.
            while res not in ('S', 'N'):
                res = str(input('Quer continuar [S/N]? ').strip().upper())
                # Caso não seja S ou N será exibido uma mensagem de erro.
                if res not in ('S', 'N'):
                    print('ERRO! Valor digitado inválido')
                    print('-' * 50)
            if res in 'N':
                break
# Final do programa.
print('-' * 50)
print('OBRIGADO POR USAR O MEU GERADOR DE TABUADA.'.center(50))
print('-' * 50)
