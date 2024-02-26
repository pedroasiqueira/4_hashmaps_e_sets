"""
Separe as palavras de acordo com a sua letra inicial.
"""

text = ['Ana', 'ana', 'Joao', 'que', 'ama', 'Jose', 'mais', 'Jose', 'nao', 'ama', 'Ana']



def screening(arr):
    screen = {}

    for word in arr:
        first_char = word[0].lower()
        if first_char not in screen:
            screen[first_char] = [word]
        else:
            screen[first_char].append(word)
    return screen

print(screening(text))
