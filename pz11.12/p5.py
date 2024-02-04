

a = int(input("Введите первое число"))
b = int(input("Введите второе число"))

choise=int(input('1 - сумма или 2 - разность 3 - произведение 4 - ср арифмитическое '))
print( (a + b) if choise==1 else print(a - b) if choise==2 else print(a * b) if choise==3 else sum([a,b,])/2 if choise==4 else print())



