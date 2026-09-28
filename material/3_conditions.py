# Estruturas condicionais permitem que o programa tome decisões com base em condições específicas.

# Em Python utilizamos principalmente:
# - if
# - elif
# - else

# O comando if executa um bloco de código apenas se a condição for verdadeira.
# O comando elif permite verificar uma nova condição caso a condição anterior seja falsa.
# O comando else executa um bloco caso nenhuma condição anterior seja verdadeira.

print("Estrutura Condicional if-elif-else:")

name = "Alice"

if name == "Alice":
    print("Hello, Alice!")
elif name == "Bob":
    # O comando pass indica que nenhuma ação será executada.
    pass
else:
    print("Hello, stranger!")

print("-" * 20)

# Em Python também podemos usar valores booleanos diretamente em condições.

print("Condição Direta com Booleanos:")

is_on = True

if is_on:
    print("O dispositivo está ligado.")

print("-" * 20)

# Podemos utilizar operadores de comparação e operadores lógicos para criar condições mais complexas.

print("Condições com Operadores Lógicos:")

x = 10

if x > 5 and x % 2 == 0:
    print("x é maior que 5 e é par!")
elif x <= 5 or x % 2 != 0:
    print("x é menor ou igual a 5 ou é ímpar!")
else:
    print("x não atende às condições.")

print("-" * 20)

# O operador 'in' verifica se um valor está presente dentro de uma lista, string ou outro objeto iterável.

print("Operador in:")

fruits = ["maçã", "banana", "cereja"]

if "maçã" in fruits:
    print("A maçã está na lista!")
else:
    print("A maçã não está na lista.")

print("-" * 20)

# Também podemos comparar strings utilizando operadores de comparação.

print("Comparação de Strings:")

password = "1234"

if password == "1234":
    print("Senha correta")
else:
    print("Senha incorreta")

print("-" * 20)