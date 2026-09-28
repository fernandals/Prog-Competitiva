# Operadores são símbolos especiais utilizados para realizar operações com valores e variáveis.

# Em Python existem vários tipos de operadores, como:
# - Operadores aritméticos
# - Operadores de comparação
# - Operadores lógicos

# Os operadores aritméticos são utilizados para realizar cálculos matemáticos.

print("Operadores Aritméticos:")

# Adição (+)
print(2 + 3) # Imprime 5

# Subtração (-)
print(10 - 4) # Imprime 6

# Multiplicação (*)
print(5 * 2) # Imprime 10

# Divisão (/)
print(10 / 2) # Imprime 5.0

# Também podemos combinar várias operações na mesma expressão. O Python respeita a prioridade matemática das operações.

number = 1 + 2 * 3 / 4.0
print(number) # Imprime 2.5

# Podemos usar parênteses para alterar a ordem das operações.

print((1 + 2) * 3) # Imprime 9

print("-" * 20)

# O operador ** representa potenciação.

print("Potenciação:")

squared = 7 ** 2
print(squared) # Imprime 49

print("-" * 20)

# A divisão inteira (//) descarta a parte decimal do resultado.

print("Divisão Inteira:")

print(7 // 2) # Imprime 3

print("-" * 20)

# O operador % retorna o resto de uma divisão.

print("Operador Módulo (Resto da Divisão):")

remainder = 11 % 3
print(remainder) # Imprime 2

print("-" * 20)

# Operadores de comparação são utilizados para comparar valores.
# O resultado dessas comparações sempre será True ou False.

print("Operadores de Comparação:")

x = 10

print(x > 5)   # Imprime True
print(x < 5)   # Imprime False
print(x >= 10) # Imprime True
print(x <= 5)  # Imprime False
print(x == 10) # Imprime True
print(x != 10) # Imprime False

print("-" * 20)

# Operadores lógicos permitem combinar condições booleanas.

print("Operadores Lógicos:")

print(True and False) # Imprime False
print(True or False)  # Imprime True
print(not True)       # Imprime False

print("-" * 20)

# Alguns operadores também funcionam com strings.

print("Operações com Strings:")

# O operador + realiza concatenação de strings.

helloworld = "hello" + " " + "world"
print(helloworld) # Imprime "hello world"

# O operador * repete a string várias vezes.

lotsofhellos = "hello" * 3
print(lotsofhellos) # Imprime "hellohellohello"

print("-" * 20)
# Operadores também podem ser utilizados com listas.

print("Operações com Listas:")

even_numbers = [2, 4]
odd_numbers = [1, 3]

# O operador + junta duas listas.

all_numbers = odd_numbers + even_numbers
print(all_numbers) # Imprime [1, 3, 2, 4]

# O operador * repete os elementos da lista.

print([1, 2, 3] * 3)
# Imprime [1, 2, 3, 1, 2, 3, 1, 2, 3]

print("-" * 20)