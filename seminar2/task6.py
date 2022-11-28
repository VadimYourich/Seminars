# 6.	Напишите программу, в которой пользователь будет задавать две строки, а программа -
# определять количество вхождений одной строки в другой.

# n1 = 'vvrrjklffggdddtttedssswaaaajjjfffgghhbbbvvvccccccxxxddeeerttyyuuiiokkjjhhgg'
# n2 = 'c'
# print(n1.count(n2))

n1 = 'vvrrjklffggdddtttedssswaaaajjjfffgghhbbbvvvccccccxxxddeeerttyyuuiiokkjjhhgg'
n2 = 'vv'
count = 0
i = 0
while i < len(n1):
    if n1[i:i + len(n2)] == n2:
        count += 1
        i += len(n2)
    else:
        i += 1
print(count)
