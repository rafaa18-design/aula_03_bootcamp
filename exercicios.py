### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir
# que todos os registros tenham valores positivos para `quantidade` e `preço`.
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos
# forem positivos ou "Dados inválidos" caso contrário.

# qnt = int(input("Digite a quantidade: "))
# preco = float(input("Digite o preço: "))

# if qnt > 0 and preco > 0:
#     print("Dados válidos")
# else:
#     print("Dados inválidos")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT.
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# temp = float(input("Digite a temperatura: "))

# if temp < 18:
#     print("Baixa")
# elif temp >= 18 and temp <= 26:
#     print("Normal")
# else:
#     print("Alta")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`,
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = {
#     "timestamp": "2021-06-23 10:00:00",
#     "level": "ERROR",
#     "message": "Falha na conexão",
# }

# if log["level"] == "ERROR":
#     print(log["message"])
# else:
#     print("Passou sem erro")

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação,
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha
# fornecido um email válido. Escreva um programa que valide essas condições
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# idade = int(input("Digite a idade: "))
# email = input("Digite o email: ")

# if idade >= 18 or idade <= 65:
#     if "@" in email and "." in email:
#         print("Dados de usuário válidos")
#         print(f"Idade: {idade}, Email: {email}")
#     else:
#         print("Email inválido")
# else:
#     print("Idade inválida")

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h).
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# transacao = {"valor": 12000, "hora": 20}

# if transacao["valor"] > 10000 or transacao["hora"] < 9 or transacao["hora"] > 18:
#     print("Transação suspeita")
# else:
#     print("Transação normal")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
# txt = "Olá mundo! Olá a todos. Bem-vindos ao mundo da programação."

# palavras = txt.split()
# novo_txt = txt.replace(".", "")
# contador = {}

# for palavra in palavras:
#     if palavra in contador:
#         contador[palavra] += 1
#         print(f"{palavra}: {contador[palavra]}")
#     else:
#         contador[palavra] = 1
#         print(f"{palavra}: {contador[palavra]}")

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
# numeros = [10, 20, 30, 40, 50]

# for numero in numeros:
#     normalizado = (numero - 10) / 40
#     print(f"{numero} normalizado: {normalizado}")

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": None},
#     {"nome": "Charlie", "email": "charlie@example.com"},
# ]
# for usuario in usuarios:
#     if usuario["email"] and usuario["nome"] is not None:
#         print(usuario)
#     else:
#         print(f"{usuario['nome']} com email faltando ou nome nulo")
# usuarios_filtrados = [usuario for usuario in usuarios if usuario["email"] is not None]
# print(usuarios_filtrados)


### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for numero in numeros:
#     if numero % 2 == 00:
#         print(f"{numero}")

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800},
# ]
# totais_por_categoria = {}

# for venda in vendas:
#     categoria = venda["categoria"]
#     valor = venda["valor"]
#     if categoria in totais_por_categoria:
#         totais_por_categoria[categoria] += valor
#         print(f"Total atualizado para {categoria}: {totais_por_categoria[categoria]}")
#     else:
#         totais_por_categoria[categoria] = valor
#         print(f"Total inicial para {categoria}: {totais_por_categoria[categoria]}")

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
# pergunta = ""
# resposta = "sair"
# while pergunta != resposta:
#     pergunta = input("Digite algo (ou 'sair' para encerrar): ")
#     if pergunta != resposta:
#         print(f"Você digitou: {pergunta}")
#     else:
#         print("Encerrando o programa.")

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# import time

# while True:
#     pergunta = int(input("Digite um número entre 1 e 10: "))
#     if pergunta < 1 or pergunta > 10:
#         print("Número inválido. Tente novamente.")
#     else:
#         print(f"Número válido: {pergunta}")
#         break
#     time.sleep(1)  # Adiciona uma pausa de 3 segundos antes de solicitar novamente

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# import time


# load = 0

# for pagina in range(1, 51):
#     print(f"Carga atual: {pagina}%")
#     time.sleep(0.5)  # Simula o tempo de resposta da API

# import time

# pagina = 1

# while pagina < 50:
#     print(f"Processando página {pagina}...")
#     pagina += 1
#     time.sleep(0.5)  # Simula o tempo de resposta da API

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
# import time

# tentativas = 0

# while tentativas < 3:
#     load = input("Digite seu load: ").lower()
#     senha = input("Digite sua senha: ")
#     if load == "Rafael" and senha == "1234":
#         print("Conexão bem-sucedida!")
#         break
#     else:
#         print("Credenciais incorretas. Tentando novamente...")
#         tentativas += 1
#     time.sleep(1)
# print("Número máximo de tentativas atingido. Conexão falhou!")


### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
import time

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lista:
    print(f"Processando item: {i}")
    if i == 8:
        print("Valor de parada encontrado. Encerrando o processamento.")
        break
    else:
        print(f"item {i} incompatível, processando próximo item...")
        time.sleep(3)  # Simula o tempo de processamento de cada item
