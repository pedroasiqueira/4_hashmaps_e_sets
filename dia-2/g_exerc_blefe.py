import random
# entrada = {
#     'Clara': [0, 1, 5, 9, 10],
#     'Marco': [0, 2, 8, 9, 10]
# }

entrada = {
    'Clara': random.sample(range(0,11), 5),
    'Marco': random.sample(range(0,11), 5)
}
print(entrada.items())

# saída: 'Marco'

def blefe(dict):
    jogador_1 = list(entrada)[0]
    jogador_2 = list(entrada)[1]
    cartas_Jogador_1 = set(dict.get(jogador_1))
    cartas_Jogador_2 = set(dict.get(jogador_2))
    print(cartas_Jogador_1)
    print(cartas_Jogador_2)
    maior_carta_jog_1 = (max(cartas_Jogador_1.difference(cartas_Jogador_2)))
    menor_carta_jog_1 = (min(cartas_Jogador_1.difference(cartas_Jogador_2)))
    maior_carta_jog_2 = (max(cartas_Jogador_2.difference(cartas_Jogador_1)))
    menor_carta_jog_2 = (min(cartas_Jogador_2.difference(cartas_Jogador_1)))

    if maior_carta_jog_1 - menor_carta_jog_1 > maior_carta_jog_2 - menor_carta_jog_2:
        return jogador_1
    elif maior_carta_jog_1 - menor_carta_jog_1 < maior_carta_jog_2 - menor_carta_jog_2:
        return jogador_2
    else:
        None


print(blefe(entrada))