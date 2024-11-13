##Coloque na documentação a explicação de como executar o arquivo .sh;##

 # Calculadora em Python
 
## Executando o Script Bash (.sh)

#Como executar o arquivo.sh

--Antes de repeti-lo, dê permissão de execução ao arquivo com o comando:
chmod +x executar_calculadora.sh

--Execute o arquivo .shcom o comando:
./executar_calculadora.sh


##Coloque a documentação para explicar seu código em python.##

# Calculadora em Python

Este projeto contém um script Python que permite realizar operações matemáticas básicas como soma, subtração, multiplicação e divisão.

## Explicação do Código Python

O código Python permite ao usuário:

1. **Inserir dois números**.
2. **Escolher uma operação** entre soma, subtração, multiplicação, divisão ou sair do programa.
3. **Executar a operação** escolhida e ver o resultado.

### Estrutura do Código

1. **Entrada de Dados**:
   - O código solicita que o usuário insira dois números (`num1` e `num2`).
   - Converte esses números para `float`, permitindo operações com casas decimais.

2. **Menu de Operações**:
   - Apresenta um menu com as seguintes opções:
     - `1`: Soma
     - `2`: Subtração
     - `3`: Multiplicação
     - `4`: Divisão
     - `5`: Sair do programa

3. **Lógica de Operação**:
   - Dependendo da opção escolhida pelo usuário:
     - Soma (`opcao == '1'`): Realiza a soma dos dois números e exibe o resultado.
     - Subtração (`opcao == '2'`): Realiza a subtração e exibe o resultado.
     - Multiplicação (`opcao == '3'`): Calcula o produto dos números e exibe o resultado.
     - Divisão (`opcao == '4'`): Verifica se o divisor (`num2`) é diferente de zero antes de dividir, para evitar erro de divisão por zero.
     - Sair (`opcao == '5'`): Encerra o programa.

4. **Validação de Entradas**:
   - Caso o usuário insira algo que não seja um número, o código exibe uma mensagem de erro.
   - Se o usuário inserir uma operação inválida, o código informa que a opção não é válida.

### Exemplo de Execução

Aqui está um exemplo de como o código funciona:

Digite o primeiro número: 5
Digite o segundo número: 3

Escolha uma operação:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
5. Sair

Digite o número da operação desejada: 1
A soma de 5.0 e 3.0 é: 8.0

Fim.
