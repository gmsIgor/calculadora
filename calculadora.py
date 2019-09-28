#Autor Igor Gomes Pereira
#Data 01.10.19
#
#Descricao  Calculadora recursiva

import funcoes_matematicas as mat
#import do modulo criado para lidar com as operacoes

def menu():
    print('--------------------------------------------------------')
    print('que operacao deseja fazer?')
    print('     (1-   |multiplicacao')
    print('     (2-   |divisao')
    print('     (3-   |achar o n primeiros termos da sequencia de fibonacci')
    print('     (4-   |MDC entre 2 numeros inteiros)')
    print('     (5-   |achar os primeiros n numeros primos')
    print('--------------------------------------------------------')
    opcao = int(input('[digite -1 para sair]-(: '))

def main():
    menu()

main()


def debug():
    mult = mat.multiplicacao(3,3)
    print(mult)

#debug()