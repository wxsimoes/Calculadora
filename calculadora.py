num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

num1 = float(num1)
num2 = float(num2)

print("\nEscolha uma operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Sair")

opcao = input("Digite o número da operação desejada: ")

if opcao == '1':
      resultado = num1 + num2
      print(f"A soma de {num1} e {num2} é: {resultado}")
elif opcao == '2':
      resultado = num1 - num2
      print(f"A subtração de {num1} e {num2} é: {resultado}")
elif opcao == '3':
      resultado = num1 * num2
      print(f"A multiplicação de {num1} e {num2} é: {resultado}")
elif opcao == '4':
      if num2 == 0:
       print("Erro: Divisão por zero!")
      else:
       resultado = num1 / num2
      print(f"A divisão de {num1} por {num2} é: {resultado}")
elif opcao == '5':
   'break'
else:
     print("Opção inválida!")

  
     print("Entrada inválida. Digite apenas números.")