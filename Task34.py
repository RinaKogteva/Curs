#  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
# и “Пам парам”, если с ритмом все не в порядке


# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

# if str(stroka).find(" ")==-1:
#     print("Количество фраз должно быть больше одной!")
# else:
#     stroka=str(stroka).split(" ")
#     sqp=[]
#     for v in range(len(stroka)):
#         s=list(str(stroka[v]).lower())
#         k=int(0)
#         for p in range(len(s)):
#             if s[p] in ["а","е","ё","и","о","у","ы","э","ю","я"]:
#                 k+=1
#         sqp.append(k)
#     if len(set(sqp))==1:
#         print("Парам пам-пам")
#     else:
#         print("Пам парам")