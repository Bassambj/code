# ESTRUTURAS CONDICIONAIS MÚLTIPLAS

# if elif else - exemplo da calculadora.
# Adaptação/incrementação do exemplo da aula da Pós-Graduação em Python:

print(" C A L C U L A D O R A ")

nro01 = float(input("Digite o primeiro número: "))
nro02 = float(input("Digite o segundo número: "))
resultado = float
print("Menu de operações: \n1 - soma >\n2 - subtração >\n3 - multiplicação >\n4 - divisão >")
operacao =int(input("Informe a operação desejada: "))
sinalOperacao=str

if (operacao==1):
    resultado=nro01+nro02
    sinalOperacao="+"    
elif(operacao==2):
    resultado=nro01-nro02
    sinalOperacao="-"
elif(operacao==3):
    resultado=nro01*nro02
    sinalOperacao="*"
elif(operacao==4):
    resultado=nro01/nro02
    sinalOperacao="/"
else:
    print("Opção",operacao," inválida.")

if(operacao>=1&operacao<=4):
    print("Cálculo:",nro01,sinalOperacao,nro02,"=",resultado)
