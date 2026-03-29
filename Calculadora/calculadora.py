while True:
  #Estrutura para tratamento da entrada do usuário
  try:
    numero1 = float(input("Informe o primeiro número: "))
    numero2 = float(input("Informe o segundo número: "))
  except ValueError:
    print("Erro! Entrada inválida, tente novamente utilizando '.' para valores flutuantes")
    continue
  
  #Imprime instruções para escolha do usuário
  print(f"{'*'*10} Calculadora Simples {'*'*10}")
  print("Qual operação você deseja realizar? \n[1]Soma \n[2]Subtração\n[3]Multiplicação \n[4]Divisão ")
  
  #Recebe opção escolhida pelo usuário
  operacao = int(input("Infome o número referente a operação desejada: "))
  
  #Confere opção e realiza os calculos necessários
  if (operacao == 1):
    resultado = (numero1+numero2)
  elif (operacao == 2):
    resultado = (numero1-numero2)
  elif (operacao == 3):
    resultado = (numero1*numero2)
  elif (operacao == 4):
    if (numero2 == 0): #Condição para não aceitar divisão por zero
      print("Ops! Não é possível dividir por 0, escolha outra operação.")
      continue
    resultado = (numero1/numero2)
  elif (operacao > 4) or (operacao < 1): #Não aceita entradas incorretas
    print("Por favor, informe a opção correta entre 1 e 4.")
    continue
  break

#Imprime o resultado da operação entre os valores informados
print(f"O resultada da operação escolhida entre os números {numero1} e {numero2} é {resultado}")
