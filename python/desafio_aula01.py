'''
Suponha que você está gerenciando uma competição esportiva e tem uma lista de tuplas representando
os resultados das equipes em diferentes modalidades. Cada tupla contém o nome da equipe, seguido
por uma lista de pontuações obtidas em cada rodada da competição.

1. Calcule a média das pontuações de cada equipe e armazene esses valores em uma nova lista
chamada medias.
2. Ordene a lista medias em ordem decrescente.
3. Crie uma nova lista chamada classificação que contém tuplas, onde cada tupla contém o nome
da equipe e a sua média de pontuações.
4. Exiba na tela a classificação final das equipes, mostrando o nome da equipe e sua média, da equipe
com a pontuação mais alta para a mais baixa.
'''

resultados = [("Equipe A", [10, 10, 20]),
              ("Equipe B", [15, 25, 35]),
              ("Equipe C", [10, 30, 50]),
              ("Equipe D", [40, 20, 10])
]

medias = []
for equipe in resultados:
    nome_equipe = equipe[0]
    pontuacoes = equipe[1]

    soma = 0
    for pontuacao in pontuacoes:
        soma += pontuacao
    
    media = soma / len(pontuacoes)
    medias.append((nome_equipe, media))

for i in range(len(medias)):
    for j in range(i + 1, len(medias)):
        if medias[i][1] < medias[j][1]:
            temp = medias[i]
            medias[i] = medias[j]
            medias[j] = temp

classificacao = medias

for equipe in classificacao:
    nome_equipe, media = equipe
    print(f"{nome_equipe}: {media:.2f}")
