"""
Dada uma lista de números,
retorne os números duplicados
"""

def get_repeated(nums):
    seen_before = set()
    repeated = set()

    for num in nums:
        if num in seen_before:
            repeated.add(num)
        else:
            seen_before.add(num)

    return repeated

# def get_repeated2(nums):
#     seen_before = []
#     repeated = []

#     for num in nums:
#         if num in seen_before and num not in repeated:
#             repeated.append(num)
#         else:
#             seen_before.append(num)
#     repeated.sort()
#     return repeated

if __name__ == "__main__":
    nums = [1, 6, 3, 9, 6, 6, 3, -1, 4, 5, 7, 1]

    print(get_repeated(nums))
    # print(get_repeated2(nums))