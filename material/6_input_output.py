# Entrada e saída de dados são fundamentais em programação.

# Em Python:
# - input() é utilizado para receber dados do usuário
# - print() é utilizado para exibir informações na tela

print("Entrada de Dados com input():")

# A função input() sempre retorna uma string.

name = input("Qual é o seu nome? ")
print("Olá, " + name + "!")

print("-" * 20)

# Podemos converter a entrada para outros tipos, como int e float.

print("Conversão de Tipos:")

age = int(input("Qual é a sua idade? "))
print(age)

height = float(input("Qual é a sua altura? "))
print(height)

print("-" * 20)

# Também podemos armazenar múltiplos valores digitados em uma única linha.

print("Múltiplos Valores na Mesma Linha:")

# Exemplo de entrada:
# 10 20

a, b = input("Digite dois números: ").split()

print(a)
print(b)

print("-" * 20)

print("Lendo uma Lista de Inteiros:")

# Exemplo de entrada:
# 1 2 3 4 5

list = []

for i in input("Digite vários números inteiros: ").split():
    list.append(int(i))

print(list)

print("-" * 20)

# Se quisermos que os valores sejam números inteiros, precisamos converter os dados.

print("Convertendo Múltiplos Valores:")

# Exemplo de entrada:
# 10 20

x, y = map(int, input("Digite dois números inteiros: ").split())

print(x + y)

print("-" * 20)

# A função map() aplica uma função para cada elemento de um conjunto de dados.

# Nesse exemplo:
# map(int, ...) converte cada valor para inteiro.

# A função print() pode exibir vários valores ao mesmo tempo.

print("Exibindo Múltiplos Valores:")

a = 10
b = 20

print(a, b)

print("-" * 20)

# Podemos utilizar f-strings para formatar textos. Esse é o método mais utilizado em Python moderno.

print("Usando f-strings:")

name = "Alice"
score = 95

print(f"Nome: {name}")
print(f"Pontuação: {score}")

x = 1.2345

print(f"Valor Verdadeiro: {x}; Valor Truncado {x:.2f}")

print("-" * 20)

# Também podemos controlar o separador utilizado pelo print().

print("Separador Personalizado:")

print(1, 2, 3, sep=" - ")

print("-" * 20)

# O parâmetro end altera o caractere exibido ao final do print().

print("Parâmetro end:")

print("Hello", end=" ")
print("World")

print("-" * 20)
