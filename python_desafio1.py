# MISSÃO 1
# Alguns exemplos de materias que eu usei para testar o código:
# Portugues. Matematica, Historia, Geografia, Ciencias, Fisica, Quimica, Filosofia, Informatica, Educacao Fisica;
# Deixei algumas funções print pra visualizar a dinamica por trás do código.

print("ESCOLA VAI NA WEB")
media = 6
materias = []
total_de_notas = 0
nome_aluno = input("Digite o nome do aluno: ")

while len(materias) < 10:
    nome_materia = input(f"Digite o nome da materia: ")
    nota_materia = float(input("Digite a nota da materia: "))
    materias.append({nome_materia : nota_materia})
    print(materias)
    total_de_notas += nota_materia
    print(f"{total_de_notas:.2f}")

media_aluno = total_de_notas / len(materias)
if media_aluno >= media:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")

print(f"Nome do aluno: {nome_aluno}")
print(f"Notas em cada materia:\n{materias}")
print(f"Total das notas: {total_de_notas:.2f}")

# MISSÃO 2
# Importei o módulo datetime para pegar o ano e usar o valor para calcular com o ano de nascimento da pessoa e descobrir a idade dela.
# Usei por um motivo claro. O ano pode se passar e os valores se alterar. Evitar fazer manutenção no código sempre.

from datetime import datetime

data_atual = datetime.now()
ano_atual = data_atual.year

print("Sistema Eleitoral Vai na Web")
nome_eleitor = input("Digite seu nome, eleitor: ")
data_eleitor = input("Digite sua data de nascimento - [Ex: 01/01/1991]: ")

idade = int(ano_atual) - int(data_eleitor[6:10])

if idade >= 16:
    print(f"Caro eleitor(a) {nome_eleitor}, sua idade é {idade} e está dentro dos requisitos solicitados. Você pode votar.")
else:
    print(f"Caro eleitor(a) {nome_eleitor}, sua idade é {idade} e não está de acordo com requisitos solicitados para votar.")

# MISSÃO 3

print("CLASSIFICAÇÃO DE NOTAS VAI NA WEB")

inserir_nota = int(input("Insira a sua nota: "))

if inserir_nota >= 90 and inserir_nota <= 100:
    print(f"Parabens! Voce tirou A.")
elif inserir_nota >= 80 and inserir_nota <= 89:
    print(f"Muito bem! Você tirou B.")
elif inserir_nota >= 70 and inserir_nota <= 79:
    print(f"Bom trabalho! Voce tirou C.")
elif inserir_nota >= 60 and inserir_nota <= 69:
    print(f"Fique atento! Voce tirou D.")
elif inserir_nota < 60:
    print(f"Estude um pouco mais. Voce tirou F.")

# MISSÃO 4

print("SISTEMA DE CALCULO VAI NA WEB")

primeiro_numero = input("Digite o primeiro numero: ")
operador_numerico = input(
    "Digite o operado numerico. Ex['+', '-', '*', '/', '%', '**', '//']: ")
segundo_numero = input("Digite o segundo numero: ")

if (operador_numerico == "+"):
    calcular_numero = eval(
        primeiro_numero + operador_numerico + segundo_numero)
if (operador_numerico == "-"):
    calcular_numero = eval(
        primeiro_numero + operador_numerico + segundo_numero)
if (operador_numerico == "*"):
    calcular_numero = eval(
        primeiro_numero + operador_numerico + segundo_numero)
if (operador_numerico == "/"):
    calcular_numero = eval(
        primeiro_numero + operador_numerico + segundo_numero)
if (operador_numerico == "%"):
    calcular_numero = eval(
        primeiro_numero + operador_numerico + segundo_numero)
if (operador_numerico == "//"):
    calcular_numero = eval(
        primeiro_numero + operador_numerico + segundo_numero)
if (operador_numerico == "**"):
    calcular_numero = eval(primeiro_numero + operador_numerico + segundo_numero)

print(f"O resultado dos dois numeros é {calcular_numero}")


# MISSÃO 5
# Acrescentei mais algumas coisas, pra simular o processamento dos dados da conta, com login e senha.
print("BEM-VINDO(A) A PAGINA DE LOGIN VAI NA WEB")

usuarios = [{"login": "admin", "password": "Python123"}]

for indice in usuarios:
    print("Faça seu login!")
    login = input("Login: ")
    password = input("Password: ")

    if login == indice.get("login") and password == indice.get("password"):
        print("Sua requisicao de acesso foi feita com sucesso! Você sera redirecionado para a proxima pagina.")
    else:
        print("Nao foi possivel processar sua requisicao de acesso! Verifique se o login ou senha estao corretos.")

# MISSÃO 6

print("SEGURANCA E CONTAGEM DO SISTEMA VAI NA WEB")
contagem_sistema = 1
while contagem_sistema < 11:
    print(contagem_sistema)
    contagem_sistema += 1

# MISSÃO 7

print("ORGANIZACAO DE LISTA VAI NA WEB")
minha_lista = [8, 3, 10, 1, 5]
minha_lista.sort()
print(minha_lista) # lista organizada [1, 3, 5, 8, 10]

# MISSÃO 8

print("ACESSO DE REGISTRO DE ALUNOS VAI NA WEB")
nome_alunos = ("Ana", "Bruno", "Daniel", "Eduardo")
print(nome_alunos[0], nome_alunos[3])

# MISSÃO 9

print("CALCULANDO DOBRO DE NUMERO VAI NA WEB")
inserir_numero = int(input("Digite um numero: "))
xnumero = inserir_numero * 2
print(f"O dobro do numero {inserir_numero} é {xnumero}.")

# MISSÃO 10

print("CONTADOR DE LETRAS VAI NA WEB")
print("Insira o seu nome para o sistema verificar quantas letras tem.")
cont_letras = input("Digite o seu nome: ")
nome_format = cont_letras.replace(" ", "") # Remove todos os backspace caso a pessoa digite o nome completo
print(len(nome_format), "\n" + nome_format)
