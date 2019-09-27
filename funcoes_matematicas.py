#Autor Igor Gomes Pereira
#Data 01.10.19
#
#Descricao  Calculadora recursiva funcoes

#nenhuma funcao considera valores menores que 0

def multiplicacao(n1,n2):
        n2 = -abs(n2) #garante que nao seja usada subtracao na funcao

        if n2 == -1:
            return n1
        elif n1 == -1:
            return n2
        elif n2 == 0 or n1 == 0:
            return 0

        return (n1 + multiplicacao(n1,n2+1))

def divivisao(n1,n2):
    
    return