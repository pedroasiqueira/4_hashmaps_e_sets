from collections import Counter

# Encontre o número mais frequente. Se houver empate, retorne qualquer um
arr = [3, 2, 5, 4, 1, 2, 3, 1, 3, 4, 1]

def count(nums):
  count = {}
  most_frequent = nums[0]
  for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
    
    if count[num] > count[most_frequent]:
       most_frequent = num
  return most_frequent


print(count(arr))

# OU:

def count2(nums):
   return Counter(nums).most_common()[0][0]

print(count2(arr))


