'5. Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética)'

nome = input("Informe o nome do aluno\n")
nota1= float(input("Informe as primeira nota do semestre: "))
nota2= float(input("Informe as segunda nota do semestre: "))
nota3= float(input("Informe as terceira nota do semestre: "))

print("Nome: ",nome)
print("A média das notas é de:",(nota1+nota2+nota3)/3)
