"""
Em jogos de tabuleiro que precisam de dois dados de 6 lados,
é muito comum que quando a soma dos números dá 7, aconteça algo especial.
Isso porque 7 é a soma mais provável.

Receba uma lista de números que representem
várias jogadas de um dado de 6 lados.
Sua missão é combinar as jogadas que somam 7.

Cada jogada só pode ser combinada uma única vez com outra dupla.
"""

def get_seven(rolls):
    seen_before = set()
    lucky_rolls = []
    for roll in rolls:
        if 7-roll in seen_before:
            lucky_rolls.append((7-roll, roll))
            seen_before.discard(7-roll)
        else:
            seen_before.add(roll)

    return lucky_rolls


if __name__ == "__main__":
    rolls = [5, 2, 1, 3, 2, 6, 1, 4, 2, 6, 3, 1]
    print(get_seven(rolls))