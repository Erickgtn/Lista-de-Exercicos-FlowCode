'Esturuta de Repetição'
'22. Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos. Mostre como resultado se houve lucro, prejuízo ou empate para cada produto. Informe media de preço de custo e do preço de venda.'


precoCusto = 0
precoVenda = 0
acumCusto = 0
acumVenda = 0
contCusto = 0
contVenda = 0

n=int(input("Informe quantidade de produtos: "))
for i in range(n):
  precoCusto=float(input("Informe o preço de custo: "))
  precoVenda=float(input("Informe o preço de venda: "))
  acumCusto =acumCusto + precoCusto 
  acumVenda =acumVenda + precoVenda
  contCusto+=1
  contVenda+=1
  if(precoCusto > precoVenda):
    print(" Prezuizo\n")
    
  elif (precoCusto < precoVenda):
    print("Lucro\n")
    
  elif(precoCusto == precoVenda):
    print("Empate\n")

print("total de venda: ",acumVenda)
print("total de custo: ",acumCusto)
print("Média de preço de custo: ",acumCusto / contCusto)
print("Total de não aptos a servir: ",acumVenda / contVenda)