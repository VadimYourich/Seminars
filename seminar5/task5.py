# 5.	Дан список, вывести отдельно буквы и цифры.
# a = ( ‘1’, "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

sp = ['1', "a", 'b', '2', '3', 'c']
a = list(filter(lambda x: x.isdigit(), sp))
print(a)
c = list(filter(lambda x: x.isalpha(), sp))
print(c)