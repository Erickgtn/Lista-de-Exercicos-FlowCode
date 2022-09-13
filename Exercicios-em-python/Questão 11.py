'11. Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. '
'Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.'

precoCusto = float(input("Informe o preco de custo do produto: "))
percentual = float(input("Informe o percentual sobre o produto: "))
venda = precoCusto  + precoCusto *(percentual/100)
print("O preço final de venda é de : ",venda)