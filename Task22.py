# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо


#var1 = '5 4' 
#var2 = '1 3 5 7 9' 
#var3 = '2 3 4 5' 


# var4=[] 
# var2=[int(a) for a in str(var2).split(" ")] 
# var3=[int(a) for a in str(var3).split(" ")] 
# var4.extend(var2) 
# var4.extend(var3) 
# var4=list(set(var4)) 
# var4.sort() 
# lsp=[] 
# for v in range(len(var4)): 
#     if var4[v] in var2 and var4[v] in var3: 
#         lsp.append(var4[v]) 
# lsp=[str(a) for a in lsp] 
# print(" ".join(lsp))