# Lista de Exercícios — Revisão de Python

Esta lista tem como objetivo revisar os principais conceitos básicos de Python. As questões combinam interpretação de código, identificação de erros e implementação de pequenos programas.

---

## 1. Olá, Mundo!

### Questão 1
Escreva um programa que exiba na tela a mensagem:

```text
Bem-vindo ao curso de Python!
````

### Questão 2

Qual será a saída do código abaixo?

```python
print("Python" + " é " + "legal!")
```

### Questão 3

Encontre e corrija o erro no código:

```python
print("Olá, mundo!)
```

---

## 2. Variáveis e Tipos

### Questão 4

Crie três variáveis para armazenar:

* seu nome;
* sua idade;
* sua altura.

Depois, exiba os três valores na tela.

### Questão 5

Qual é o tipo de cada uma das variáveis abaixo?

```python
nome = "Maria"
idade = 20
altura = 1.65
estudante = True
```

### Questão 6

Qual será a saída do código abaixo?

```python
x = 10
y = x
x = 20

print(y)
```

---

## 3. Listas

### Questão 7

Crie uma lista contendo cinco linguagens de programação. Depois, exiba:

* a primeira linguagem;
* a última linguagem;
* a quantidade de linguagens na lista.

### Questão 8

Dada a lista:

```python
numeros = [10, 20, 30, 40, 50]
```

Adicione o número `60`, remova o número `20` e exiba a lista resultante.

### Questão 9

Qual será a saída do código abaixo?

```python
frutas = ["maçã", "banana", "laranja"]

frutas.append("uva")
frutas[1] = "morango"

print(frutas)
```

---

## 4. Operadores Básicos

### Questão 10

Sem executar o código, determine o resultado de cada expressão:

```python
10 + 3 * 2
20 / 4
17 // 3
17 % 3
2 ** 4
```

### Questão 11

Escreva um programa que receba o preço de um produto e uma quantidade e calcule o valor total da compra.

### Questão 12

Um aluno possui três notas. Escreva um programa que receba as três notas e calcule a média.

---

## 5. Formatação de Strings

### Questão 13

Dada a variável:

```python
nome = "Fernanda"
```

Exiba a mensagem abaixo utilizando uma **f-string**:

```text
Olá, Fernanda!
```

### Questão 14

Crie variáveis para armazenar o nome, idade e curso de uma pessoa. Depois, exiba uma frase utilizando f-string, como:

```text
João tem 20 anos e estuda Python.
```

### Questão 15

Dadas as variáveis:

```python
produto = "Notebook"
preco = 3500
```

Exiba:

```text
O Notebook custa R$ 3500.
```

utilizando uma f-string.

---

## 6. Operações Básicas com Strings

### Questão 16

Qual será a saída do código abaixo?

```python
texto = "Python"

print(texto[0])
print(texto[-1])
print(len(texto))
```

### Questão 17

Dada a string:

```python
frase = "Python é uma linguagem de programação"
```

Escreva um programa que:

* exiba a frase em letras maiúsculas;
* exiba a frase em letras minúsculas;
* verifique se a palavra `"Python"` está presente na frase.

### Questão 18

Escreva um programa que receba uma palavra e exiba:

* a quantidade de caracteres;
* o primeiro caractere;
* o último caractere.

---

## 7. Condições

### Questão 19

Escreva um programa que receba uma idade e informe se a pessoa é menor ou maior de idade.

### Questão 20

Escreva um programa que receba uma nota e informe:

* `"Aprovado"` se a nota for maior ou igual a 7;
* `"Recuperação"` se a nota estiver entre 5 e 6.9;
* `"Reprovado"` caso contrário.

### Questão 21

Qual será a saída do código abaixo?

```python
idade = 18

if idade > 18:
    print("A")
elif idade == 18:
    print("B")
else:
    print("C")
```

---

## 8. Loops

### Questão 22

Escreva um programa que exiba os números de 1 a 10 utilizando um `for`.

### Questão 23

Escreva um programa que exiba apenas os números pares entre 1 e 20.

### Questão 24

Dada a lista:

```python
nomes = ["Ana", "Carlos", "João", "Maria"]
```

Utilize um loop para exibir:

```text
Olá, Ana!
Olá, Carlos!
Olá, João!
Olá, Maria!
```

---

## 9. Funções

### Questão 25

Crie uma função chamada `saudacao` que receba um nome e exiba:

```text
Olá, João!
```

### Questão 26

Crie uma função chamada `dobro` que receba um número e **retorne** o seu dobro.

### Questão 27

Crie uma função chamada `eh_par` que receba um número e retorne `True` caso ele seja par e `False` caso contrário.

---

## 10. Dicionários

### Questão 28

Crie um dicionário representando um aluno, contendo:

* nome;
* idade;
* curso;
* nota.

Depois, exiba cada informação.

### Questão 29

Dado o dicionário:

```python
aluno = {
    "nome": "João",
    "idade": 20,
    "nota": 8.5
}
```

Altere a nota para `9.0` e adicione uma nova chave chamada `"aprovado"`.

### Questão 30

Qual será a saída do código abaixo?

```python
pessoa = {
    "nome": "Maria",
    "idade": 21
}

print(pessoa["nome"])
print(pessoa.get("cidade"))
```

---

## 11. Entrada e Saída

### Questão 31

Escreva um programa que peça o nome e a idade do usuário e exiba:

```text
Olá, João! Você tem 20 anos.
```

### Questão 32

Crie um programa que receba dois números e exiba:

* soma;
* subtração;
* multiplicação;
* divisão.

### Questão 33

Por que o código abaixo apresenta um problema?

```python
idade = input("Digite sua idade: ")
print(idade + 1)
```

Corrija o código para que ele funcione corretamente.
