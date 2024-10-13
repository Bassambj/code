L=[7,4,3,12,8]
print("========================================")
print("Lista original:",L)
print("========================================")
fim=len(L)                              #1
while fim > 1:                          #2
    trocou=False                        #3
    x=0                                 #4
    while x<(fim-1):                    #5
        if L[x] > L[x+1]:               #6
                    print("........................................")
                    print("x:",L[x]," x+1:",L[x+1])
                    trocou=True         #7
                    print(L[x],">",L[x+1],"trocar: ",trocou)
                    temp= L[x]          #8
                    L[x]=L[x+1]
                    L[x+1]=temp                    
                    print(" Trocou:",trocou,"/ Lista:",L)                    
        x+=1
    if not trocou:                      #9
          break
    fim-=1                              #10
print("========================================")
print("Lista Final:",L)
print("========================================")

#1 Utilizamos len para verificar o tamanho da lista e marcar fim com esse nro.
#2 Aqui verificando fim >1
#3 utilizamos o troucou para indicar que não realizamos troca
#4 variável x será utilizada como índice começando em zero
#5 garantir um próximo elemento para comparar,condição:
    # Que x seja anterior ao último elemento.
#6 O próximo elemento x+1 , que deve ser sempre maior que o anteriorself.
    # Se a condição for verdadeira estão fora de ordem e devem ser trocados
#7 Marcamos que efetuamos uma troca.
#8 UItilizamos uma variável temporária para trocar os elementos de posição
#9 Verificamos se algo foi trocado na repetição anterior
#10 Caso contrário diminuimos o valor de fim para que não precisemos mais verificá-lo 
