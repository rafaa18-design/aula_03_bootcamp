### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

CONSTANTE_BONUS = 1000

nome = False
salario = False
bonus = False

while nome is False:
    nome = input("Informe seu nome: ")
    if nome.isdigit():
        print("Nome escrito errado!")
        nome = False
    elif len(nome) == 0:
        print("Nome não pode ficar vazio")
        nome = False
    elif nome.isspace():
        print("Nome não pode conter apenas espaços")
        nome = False
    else:
        nome = True

while salario is False:
    try:
        salario = float(input("Informe seu salário: "))
        if salario < 0.0:
            print("Salário não pode ser negativo")
        else:
            pass
    except ValueError:
        print("Formato inválido de salário")

while bonus is False:
    try:
        bonus = float(input("Informe o valor do bônus: "))
        if bonus <= 0:
            print("Bônus não pode ser negativo")
    except ValueError:
        print("Formato inválido de bônus")
        bonus = False

valor_bonus = (salario * bonus) - salario
kpi = (valor_bonus + salario) / CONSTANTE_BONUS

print(
    f"Olá {nome} seu salário é de {salario:,.2f}$, ganhou um bônus de {valor_bonus:,.1f}$ e seu KPI é de {kpi:.1f}"
)
