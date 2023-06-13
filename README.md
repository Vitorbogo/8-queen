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
