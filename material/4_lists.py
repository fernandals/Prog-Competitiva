# Listas são estruturas utilizadas para armazenar múltiplos valores em uma única variável.

# Em Python, listas:
# - Mantêm a ordem dos elementos
# - Podem ser modificadas
# - Permitem elementos repetidos
# - Podem armazenar diferentes tipos de dados

print("Criando uma Lista:")

mylist = [1, 2, 3]

print(mylist) # Imprime [1, 2, 3]

print("-" * 20)

# Cada elemento da lista possui uma posição chamada índice.
# Os índices começam em 0.

print("Acessando Elementos da Lista:")

print(mylist[0]) # Imprime 1
print(mylist[1]) # Imprime 2
print(mylist[2]) # Imprime 3

print("-" * 20)

# Podemos adicionar novos elementos utilizando o método append().

print("Adicionando Elementos:")

mylist.append(4)
mylist.append(5)
mylist.append(6)

print(mylist) # Imprime [1, 2, 3, 4, 5, 6]

print("-" * 20)

# A função len() retorna a quantidade de elementos da lista.

print("Comprimento da Lista:")

print(len(mylist)) # Imprime 6

print("-" * 20)

# Também podemos acessar elementos usando índices negativos.
# Nesse caso, a contagem começa pelo final da lista.

print("Índices Negativos:")

print(mylist[-1]) # Imprime 6
print(mylist[-2]) # Imprime 5
print(mylist[-3]) # Imprime 4

print("-" * 20)

# O slicing permite acessar intervalos da lista.

print("Slicing de Listas:")

print(mylist[0:3]) # Imprime [1, 2, 3]
print(mylist[3:6]) # Imprime [4, 5, 6]

# Se omitirmos o início, o Python começa do primeiro elemento.

print(mylist[:3]) # Imprime [1, 2, 3]

# Se omitirmos o final, o Python vai até o último elemento.

print(mylist[3:]) # Imprime [4, 5, 6]

print("-" * 20)

# Listas podem ser modificadas após a criação.

print("Alterando Elementos:")

mylist[0] = 10

print(mylist) # Imprime [10, 2, 3, 4, 5, 6]

print("-" * 20)

# Podemos remover elementos de diferentes formas.

print("Removendo Elementos:")

# remove() remove um valor específico da lista.

mylist.remove(10)

print(mylist) # Imprime [2, 3, 4, 5, 6]

# pop() remove o último elemento da lista
# e retorna o valor removido.

last = mylist.pop()

print(last)   # Imprime 6
print(mylist) # Imprime [2, 3, 4, 5]

print("-" * 20)

# O operador in verifica se um elemento existe na lista.

print("Verificando Elementos:")

print(3 in mylist) # Imprime True
print(10 in mylist) # Imprime False

print("-" * 20)

# Python permite listas heterogêneas, ou seja, listas com diferentes tipos de dados.

print("Listas Heterogêneas:")

mixed = [1, "hello", True]

print(mixed) # Imprime [1, 'hello', True]

print("-" * 20)