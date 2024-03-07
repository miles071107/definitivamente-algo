x = float(input('Digite a média de um aluno: '))
if x > 7.0:
  print('Aprovado')
elif x < 0.0 and x > 10.0:
  print('Erro, tente novamente')
else:
  print('Reprovado')
