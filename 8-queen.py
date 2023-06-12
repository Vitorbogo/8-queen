import random

N = int(input("Digite o tamanho do tabuleiro: "))
tamanho_populacao = 100
num_geracoes = 100
taxa_cruzamento = 0.8
taxa_mutacao = 0.2


def criar_populacao(tamanho_populacao, tamanho_tabuleiro):
    populacao = []
    for _ in range(tamanho_populacao):
        tabuleiro = list(range(tamanho_tabuleiro))
        random.shuffle(tabuleiro)
        populacao.append(tabuleiro)
    return populacao


def calcular_fitness(tabuleiro):
    conflitos = 0
    tamanho_tabuleiro = len(tabuleiro)
    for i in range(tamanho_tabuleiro):
        for j in range(i + 1, tamanho_tabuleiro):
            if tabuleiro[i] == tabuleiro[j] or abs(tabuleiro[i] - tabuleiro[j]) == abs(i - j):
                conflitos += 1
    return 1 / (conflitos + 1)


def selecionar_pais(populacao, num_pais):
    pais_selecionados = []
    fitness_total = sum(calcular_fitness(tabuleiro) for tabuleiro in populacao)
    for _ in range(num_pais):
        roleta = random.uniform(0, fitness_total)
        soma_fitness = 0
        for tabuleiro in populacao:
            soma_fitness += calcular_fitness(tabuleiro)
            if soma_fitness >= roleta:
                pais_selecionados.append(tabuleiro)
                break
    return pais_selecionados


def cruzar(tabuleiro1, tabuleiro2):
    ponto_corte = random.randint(1, len(tabuleiro1) - 1)
    filho1 = tabuleiro1[:ponto_corte] + tabuleiro2[ponto_corte:]
    filho2 = tabuleiro2[:ponto_corte] + tabuleiro1[ponto_corte:]
    return filho1, filho2


def mutar(tabuleiro, taxa_mutacao):
    if random.random() < taxa_mutacao:
        indice1, indice2 = random.sample(range(len(tabuleiro)), 2)
        tabuleiro[indice1], tabuleiro[indice2] = tabuleiro[indice2], tabuleiro[indice1]


def algoritmo_genetico(tamanho_populacao, tamanho_tabuleiro, num_geracoes, taxa_cruzamento, taxa_mutacao):
    populacao = criar_populacao(tamanho_populacao, tamanho_tabuleiro)
    for geracao in range(num_geracoes):
        nova_populacao = []
        for _ in range(tamanho_populacao // 2):
            pais = selecionar_pais(populacao, 2)
            filho1, filho2 = cruzar(pais[0], pais[1])
            mutar(filho1, taxa_mutacao)
            mutar(filho2, taxa_mutacao)
            nova_populacao.append(filho1)
            nova_populacao.append(filho2)
        populacao = nova_populacao
    melhor_tabuleiro = max(populacao, key=calcular_fitness)
    return melhor_tabuleiro


def imprimir_tabuleiro(tabuleiro):
    tamanho_tabuleiro = len(tabuleiro)
    linha_divisoria = "+ " + "─ " * tamanho_tabuleiro + "+"

    print(linha_divisoria)
    for i in range(tamanho_tabuleiro):
        linha = "| "
        for j in range(tamanho_tabuleiro):
            if tabuleiro[j] == i:
                linha += "Q "
            else:
                linha += ". "
        linha += "|"
        print(linha)
    print(linha_divisoria)


melhor_tabuleiro = algoritmo_genetico(
    tamanho_populacao, N, num_geracoes, taxa_cruzamento, taxa_mutacao)

imprimir_tabuleiro(melhor_tabuleiro)

print("Fitness:", calcular_fitness(melhor_tabuleiro))

print("Conflitos:", N * (N - 1) / 2)

print("Solução ótima:", calcular_fitness(melhor_tabuleiro) == 1)
