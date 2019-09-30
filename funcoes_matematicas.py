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
    resto = 0
    
    if divisor == 0:
        return 'ERRO: divisao por 0'

    while True:
        dividendo -= divisor
        
        if dividendo < 0:             
            resto = dividendo + divisor      #ao chegar a 0, a sequencia de subtracoes se
            return [quociente, resto]        #encerra retornando o quociente e o resto
            
        quociente += 1

#retorna o n-esimo termo da sequencia de fibonacci
#   versao que exige muito do poder de processamento
def fibonacci(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)

#baseado no algoritmo de euclides
def mdc(n1,n2):
    if (n1 == 0) or (n2 == 0):
        return 'ERRO: divisao por 0'

    dividendo = max(n1,n2)
    divisor = min(n1,n2)
    resto = 0
    while True:
        resto = dividendo % divisor
        dividendo = divisor
        if resto != 0:
            divisor = resto
        else:
            return divisor


#
def primos(n):
    primos = []
    i = 2
    while i <= n + 1:
        primo = True
        for j in range(2,i):
            if (i%j == 0) and (i != j):     #checa se 'i' e divisivel pelos numeros do conjunto [2,i-1]
                primo = False
        
        if primo:
            primos += [i]                   #se nao for divisivel pelo conjunto, e um numero primo
        else:
            n += 1                          #se for divisivel entao precisamos buscar mais valores, somando 1 ao n

        i+=1                                #muda-se o 'i' a cada nova chamada do loop ate conseguir os 'n' numeros primos
    return primos
    
            

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-[extra mile]-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#uma versao otimizada da repeticao do fibonacci (mesmo com recursao).
#       evita passar chamadas de funcao desnecessarias, pode meter uma sequencia de 1000 
#       que nao vai demorar nada pra criar a lista (talvez demore um pouco pra printar apenas)

#funcao recursiva
def fibo_ja_sei(n, ja_sei):
    if n == ja_sei[0]:
        return ja_sei[1]
    if n == ja_sei[0] - 1:
        return ja_sei[2]
    
    return fibo_ja_sei(n-1, ja_sei) + fibo_ja_sei(n-2, ja_sei)

#funcao nao recursiva
def fibo_seq(fim):
    fibo_seq = [0,1]
    ja_sei = [2,1,0]
    
    if fim <3:
        return fibo_seq[:fim]

    for i in range(3,fim + 1):
        fibo_seq += [fibo_ja_sei(i-1,ja_sei)]
        ja_sei = [i-1,fibo_seq[i-1],fibo_seq[i-2]]
    
    return fibo_seq


