# Variáveis são as caixinhas onde guardamos valores importantes para nosso código!

# Em Python podemos ter variáveis para guardar vários tipos de dados, como: números, booleanos, strings e até listas! 

# Uma das convenções dessa linguagem é nomear variáveis com letras minúsculas e, quando necessário, separar palavras com underscode (_).

print("Tipos de Variáveis:")

myint = 7
myfloat = 7.0
mybool = True
mystring_1 = 'hello'
mystring_2 = "world"
mylist = [1, 2, 3]

print("-" * 20)

# Como o nome já diz, os valores armazenados em uma variável podem mudar sempre que necessário:

print("Mudança de Valor:")

var = 2
print(var)

var = 10
print(var)

print("-" * 20)

# As variáveis podem ser utilizadas em diversos tipos de operações

# Podemos adicionar variáveis que contem números, e o resultado será a soma dos números armazenados:

print("Resultado da Adição de Variáveis:")

one = 1
two = 2
three = one + two
print(three) # Imprime 3

print("-" * 20)

# Quando usamos o operador + com strings, o Python junta os textos (concatenação).

print("Resultado da Adição de Strings (Concatenação):")

hello = "hello"
world = "world"
helloworld = hello + world
print(helloworld) # Imprime "helloworld"

print("-" * 20)

# Não podemos usar + entre tipos incompatíveis, como lista + int ou string + float.

# Uma exceção dessa regra é a adição entre dois tipos numéricos:

print("Resultado da Conversão de Tipos Automática (Coerção Implicita):")

print(2 + 2.0) # Imprime 4.0

print("-" * 20)

# Se desejamos fazer uma operação dessas e temos tipos diferentes podemos simplesmente converter a variável para o tipo desejado:

print("Resultado da Conversão de Tipos Manual (Coerção Explícita):")

num = 5
num_str = str(num)
print("Idade: " + num_str) # Imprime "Idade: 5"

# Isso causaria um erro:
# print("Idade: " + 5)

print("-" * 10)

num_str = "5"
print(5 + int(num_str)) # Imprime 10
    
print("-" * 20)

# Por último, podemos também atribuir valores múltiplos valores a variáveis diferentes simultaneamente:

print("Resultado da Atribuição Múltipla:")

a, b = 3, 4
print(a, b) # Imprime 3 4

print("-" * 20)
