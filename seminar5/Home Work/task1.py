# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# [‘ПРИВЕТ’, ‘ЗАБВЕНИЕ’, 'ПОКА’] ->[‘ПРИВЕТ’, 'ПОКА’]

sp = input().split()

sp = list(filter(lambda x:'abc' not in x, sp))

print(' '.join(sp))