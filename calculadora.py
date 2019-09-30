#---------------------------------------------------------------------------------------------------
#Autor Igor Gomes Pereira
#Data 01.10.19
#
#Descricao  Calculadora recursiva
#---------------------------------------------------------------------------------------------------


import funcoes_matematicas as mat
#import do modulo criado para lidar com as operacoes

import os



def menu():
    print('--------------------------------------------------------')
    print('que operacao deseja fazer?')
    print('     (1-   |multiplicacao')
    print('     (2-   |divisao')
    print('     (3-   |achar o \'n\' primeiros termos da sequencia de fibonacci')
    print('     (4-   |MDC entre dois numeros inteiros)')
    print('     (5-   |achar os primeiros \'n\' numeros primos')
    print('--------------------------------------------------------')
    opcao = int(input('[digite -1 para sair]-(: '))

    if opcao == -1:
        return 'sair'

    elif opcao == 1:
        print('-------[voce escolheu a multiplicacao]-------')
        n1 = int(input('[entre com o primeiro valor]-(: '))
        n2 = int(input('[entre com o segundo valor]-(: '))
        return mat.multiplicacao(n1,n2)

    elif opcao == 2:
        print('-------[voce escolheu a divisao]-------')
        n1 = int(input('[entre com o dividendo]-(: '))
        n2 = int(input('[entre com o divisor]-(: '))
        print('\n\n\n\n-------[resultado em forma de: \'<quociente>, <resto>\']-------')
        return mat.divivisao(n1,n2)
    
    elif opcao == 3:
        print('-------[voce escolheu os \'n\' termos da sequencia de fibonacci]-------')
        n = int(input('[entre com o \'n\']-(: '))
        return mat.fibo_seq(n)
    elif opcao == 4:
        print('-------[voce escolheu o MDC entre dois numeros inteiros]-------')
        n1 = int(input('[entre com o primeiro valor]-(: '))
        n2 = int(input('[entre com o segundo valor]-(: '))
        return mat.mdc(n1,n2)
    elif opcao == 5:
        print('-------[voce escolheu os \'n\' primeiros numeros primos]-------')
        n = int(input('[entre com o \'n\']-(: '))
        return mat.primos(n)

def main():

    while True:
        resultado = menu()
        if resultado == 'sair':
            print('-------[voce escolheu sair do programa]-------')
            return 0

        resultado_str = str(resultado).replace('[','',1)
        resultado_str = resultado_str.replace(']','.',1)
        print('\n\n-------[RESULTADO]-------')
        print(resultado_str)
        print('-------[RESULTADO]-------\n\n\n\n\n')
        
main()

#demonstracao do poder da otimizacao
def demonstrativo():

    naci = mat.fibo_seq(3000)

    print(len(naci))
    print('terminou')

#demonstrativo()