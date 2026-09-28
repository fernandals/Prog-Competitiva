# Loops são estruturas utilizadas para repetir blocos de código.

# Em Python os principais tipos de loops são:
# - for
# - while

print("Loop for com range():")

# A função range() gera uma sequência de números. Nesse exemplo, os números vão de 0 até 4.

for i in range(5):
    print(i)

print("-" * 20)

# Também podemos definir o início e o fim da sequência.

print("range() com Início e Fim:")

# Nesse caso, os números vão de 2 até 4. O valor final não é incluído.

for i in range(2, 5):
    print(i)

print("-" * 20)

# O loop for também pode percorrer elementos de listas diretamente.

print("Percorrendo uma Lista:")

primes = [2, 3, 5, 7]

for prime in primes:
    print(prime)

print("-" * 20)

# Podemos utilizar range() e len() para acessar os índices de uma lista.

print("Percorrendo Índices da Lista:")

for i in range(len(primes)):
    print(primes[i])

print("-" * 20)

# A função enumerate() permite acessar
# o índice e o valor ao mesmo tempo.

print("Usando enumerate():")

for index, value in enumerate(primes):
    print(f"Índice: {index}, Valor: {value}")

print("-" * 20)

# O loop while executa enquanto uma condição for verdadeira.

print("Loop while:")

count = 0

while count < 5:
    print(count)

    # count += 1 é equivalente a:
    # count = count + 1

    count += 1

print("-" * 20)

# O comando break encerra o loop imediatamente.

print("Usando break:")

count = 0

while True:
    print(count)

    count += 1

    if count >= 5:
        break

print("-" * 20)

# O comando continue interrompe apenas
# a iteração atual do loop.

print("Usando continue:")

# Nesse exemplo, números pares serão ignorados.

for x in range(10):

    if x % 2 == 0:
        continue

    print(x)

print("-" * 20)