n = int(input("Quantos alunos deseja calcular a média? "))

nomes  = []
medias = []

for i in range(n):
    nota1 = float(input("Insira a nota 1:"))
    nota2 = float(input("Insira a nota 2:"))
    
    nome = input("Insira o nome do aluno:")
    
    media = (nota1+nota2)/2
    medias.append(media)
    nomes.append(nome)
    
posicao = int (input("Qual aluno você deseja ver a média?"))
    
if posicao < n:
     print("A média deste aluno é", medias[posicao])