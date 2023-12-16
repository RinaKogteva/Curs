# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по 
# счету числом Фибоначчи оно является, то есть 
# выведите такое число n, что φ(n)=A. Если А не 
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6


# A = int(input("Введите число: ")) 
# fib1 = 0
# fib2 = 1 
# i = 3 
# if A == fib1: 
#     print("№1") 
# while A >= i:
#     fibsum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fibsum
#     if fibsum == A:
#         print(f"№{i}")
#         break     
#     elif A < fibsum:
#         print("-1")
#         break
#     else: i += 1


# n = int(input())  # 3
# first = 0
# second = 1
# if n == 0:
#     print(1)
#     exit()
# if n == 1:
#     print(2, 3)
#     exit()
# summ = 1
# k = 2
# while n > sum:  # 3 > 3
#     first = second # 1
#     second = summ # 2
#     summ = first + second # 3
#     k += 1  #4
# if summ == n:
#     print(k+1)
# else:
#     print(-1)
    
    
#     n = 4
# summ = 0
# f_1 = 1
# f_2 = 1
# num = 3

# while summ < n:
#     summ = f_1 + f_2
#     f_1 = f_2
#     f_2 = summ
#     num += 1
# print(f'{num}' if summ == n else '-1')

a = int(input("Введите число: "))
first_fibo, second_fibo = 0, 1 
n = 2
while a > second_fibo:
    first_fibo, second_fibo = second_fibo, first_fibo + second_fibo 
    n += 1
if a == second_fibo:
    print(n)
else:
    print(-1)
    
