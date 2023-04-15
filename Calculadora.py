#variavel para receber a opção de operação
operacao = int(input(''' Selecione o número da operacao desejada:
                  1 = Soma
                  2 = Subtração
                  3 = Multiplicação
                  4 = Divisão
                  Digite sua opção (1/2/3/4): '''))

#Inicio do condição de soma
if operacao == 1:
    n1 = int(input('Digite o primeiro numeor: '))
    n2 = int(input('Digite o segundo numero: '))
    resultado_soma = (n1+n2)
    print('A soma de %s + %s é =' %(n1,n2),resultado_soma )

#Condição de subtração
elif operacao == 2:
    n3 = float(input('Digite o primeiro numero: '))
    n4 = float(input ('Digite o segundo numero: '))
    resultado_sub = (n3 - n4)
    print('A subtração de %s - %s é =' %(n3,n4),resultado_sub)

#condição de multiplicação
elif operacao == 3:
    n5 = int(input('Digite o primeiro numero: '))
    n6 = int(input('Digite o segunda numero: '))
    resultado_mult = (n5*n6)
    print('A multiplicação de %s * %s é =',resultado_mult)

#condição de divisão
elif operacao == 4 :
     n7 = int(input('Digite o primeiro numero: '))
     n8 = int(input('Digite o segundo numero: '))
     resultado_div = (n7//n8)
     print('A divisão de %s / %s é  ='%(n7,n8),resultado_div)

#Se o usuário digitar o numero fora da opção, irá retornar esse erro
else:
     print('operação invalida, digite apenas as opções apresentadas')