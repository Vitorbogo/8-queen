Repositório contendo um programa em Python que soluciona o problema das 8 rainhas no xadrez. O programa utiliza um algoritmo genético para encontrar uma disposição válida das rainhas, evitando que elas se ataquem horizontalmente, verticalmente ou diagonalmente. A implementação é flexível e permite ajuste dos parâmetros do algoritmo para diferentes tamanhos de tabuleiro.

Explicação do código:

# Declarações

Na primeira parte do código, são definidas as variáveis N, tamanho_populacao, num_geracoes, taxa_cruzamento e taxa_mutacao através da entrada do usuário.

N vai definir o tamanho do tabuleiro, o tamanhor mínimo possível é 4, e se não for informado nenhum dado de entrada o tamanho padrão será 8, no qual é o tamanho original de um tabuleiro de xadrez

# criar_populacao

A função criar_populacao é responsável por gerar uma população inicial de configurações de tabuleiro aleatórias.

É criada uma lista de tabuleiros, onde cada tabuleiro é uma permutação dos números de 0 a tamanho_tabuleiro.

# calcular_fitness

A função recebe um tabuleiro como entrada e calcula o fitness desse tabuleiro, ou seja, uma medida de quão bom é esse tabuleiro em relação ao problema das "Oito Rainhas".

Ela percorre todas as rainhas no tabuleiro e verifica se há conflitos entre elas.

Quanto menor o número de conflitos, maior será o fitness atribuído ao tabuleiro.

O valor retornado é uma pontuação que indica o quão bom é o tabuleiro em termos de resolução do problema.

# selecionar_pais

Essa função recebe uma população de tabuleiros e um número desejado de pais para seleção.

Ela utiliza a técnica da roleta viciada para selecionar os pais.

No qual a probabilidade de um indivíduo ser selecionado é proporcional à sua aptidão, por isto a escolha desta técnica.

O valor retornado é uma lista contendo os tabuleiros selecionados como pais.

# cruzar

Essa função recebe dois tabuleiros e realiza o processo de cruzamento entre eles.

Ela escolhe aleatoriamente um ponto de corte no tabuleiro e cria dois filhos combinando as partes dos pais antes e depois desse ponto.

O valor retornado é uma tupla contendo os dois filhos resultantes do cruzamento.

# mutar

Essa função recebe um tabuleiro e uma taxa de mutação.

Ela realiza uma mutação aleatória no tabuleiro, com base na taxa de mutação fornecida.

A mutação consiste em trocar aleatoriamente duas posições no tabuleiro.

A taxa de mutação determina a probabilidade de ocorrer uma mutação em um tabuleiro.

Não há valor de retorno, pois a mutação é aplicada diretamente no tabuleiro fornecido como argumento.

# algoritmo_genetico

Essa função implementa o algoritmo genético, recebendo os parâmetros das funções anteriores para resolver o problema das oito Rainhas

Ela gera uma população inicial de tabuleiros aleatórios.

Em cada geração, seleciona os pais, realiza o cruzamento e aplica mutação nos filhos.

O processo é repetido por um número definido de gerações.

Ao final das gerações, o melhor tabuleiro (com o maior fitness) é retornado como a solução encontrada.

# imprimir_tabela

Exibir visualmente o resultado encontrado.

# parte final

Na parte final do código, é chamado o algoritmo genético com os parâmetros fornecidos.

O tabuleiro resultante com a melhor solução é exibido,

O valor de fitness, o número de conflitos esperado para o problema

E se a solução encontrada é ótima (fitness igual a 1).

___

# Eight Queens Problem Solver
This repository contains a Python program that solves the Eight Queens problem in chess. The program utilizes a genetic algorithm to find a valid arrangement of the queens on the chessboard, ensuring that they do not attack each other horizontally, vertically, or diagonally. The implementation is flexible and allows for adjusting the algorithm's parameters to solve the problem for different board sizes.

# Code Explanation

# Declarations
In the first part of the code, the following variables are defined through user input: N, population_size, num_generations, crossover_rate, and mutation_rate.

N determines the size of the chessboard, with a minimum size of 4. If no input is provided, the default size is set to 8, which represents the standard chessboard size.

# create_population
The create_population function generates an initial population of random board configurations. It creates a list of boards, where each board is a permutation of the numbers from 0 to board_size.

# calculate_fitness
The calculate_fitness function takes a board as input and calculates its fitness, which represents how good the board is in solving the Eight Queens problem. It checks for conflicts between the queens on the board by iterating through each queen. The fitness value is determined by the number of conflicts: the fewer the conflicts, the higher the fitness.

# select_parents
The select_parents function receives a population of boards and a desired number of parents for selection. It implements the biased roulette technique to select the parents. The selection probability is proportional to the fitness of each individual, ensuring a higher chance of selecting fitter boards.

# crossover
The crossover function takes two parent boards and performs the crossover process between them. It randomly selects a crossover point on the board and creates two children by combining the parent's sections before and after the crossover point.

# mutate
The mutate function applies a random mutation to a board based on the provided mutation rate. It swaps two positions on the board randomly. The mutation rate determines the probability of a mutation occurring in a board.

# genetic_algorithm
The genetic_algorithm function implements the genetic algorithm to solve the Eight Queens problem. It generates an initial population of random boards and iteratively selects parents, performs crossover, and applies mutation to create new generations. This process continues for a defined number of generations. The best board with the highest fitness value is considered the solution.

# print_board
The print_board function visually displays the resulting board, representing the best solution found.

# Usage
To run the program, make sure you have Python installed. Simply execute the main.py file and follow the prompts to provide the required parameters. The program will output the best solution found, along with the fitness value and the number of conflicts.

Feel free to adjust the algorithm parameters and try different board sizes to solve the Eight Queens problem!
