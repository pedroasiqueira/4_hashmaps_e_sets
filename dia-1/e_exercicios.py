dict = {x: x * 2 for x in range(3, 21)}
print(dict.keys())

str = "bbbbaaaacccaaaaaaddddddddccccccc"
dictstr = {}

for item in str:
    if item in dictstr:
        dictstr[item] += 1
    else:
        dictstr[item] = 1

print(dictstr)

for i in dict.keys():
    if i % 2 is not 0:
        dict[i] = i * 3

print(dict)