
import time
import asyncio

ml_list = [(char) for char in 'hello']                          # ['h', 'e', 'l', 'l', 'o']
ml_list2 = [(num * 2) for num in range(0,10)]                   # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
ml_list3 = [(num * 2) for num in range(0,10) if (num%2 == 0)]   # [0, 4, 8, 12, 16]

print(ml_list)
print(ml_list2)
print(ml_list3)




