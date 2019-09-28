#---------------------------------------------------------------------------------------------------
#Autor Igor Gomes Pereira
#Data 01.10.19
#
#Descricao  Calculadora recursiva funcoes
#
#nenhuma funcao considera valores menores que 0
#---------------------------------------------------------------------------------------------------

#
def multiplicacao(n1,n2):
        n2 = -abs(n2) #garante que nao seja usada subtracao na funcao

        if n2 == -1:
            return n1
        elif n1 == -1:
            return n2
        elif n2 == 0 or n1 == 0:
            return 0

        return (n1 + multiplicacao(n1,n2+1))

#
def divivisao(dividendo,divisor):
    quociente = 0
    resto= 0

    while True:
        dividendo -= divisor
        
        if dividendo < 0:
            resto = dividendo + divisor      #ao chegar a 0, a sequencia de subtracoes se
            return [quociente, resto]        #encerra retornando o quociente e o resto
            
        quociente += 1

#retorna o n-esimo termo da sequencia de fibonacci
def fibonacci(n):

    return
