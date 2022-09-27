A = float(input("enter float number A:"))
B = float(input("enter float number B:"))
C = float(input("enter float number C:")) # ввод вещественных переменных float

if A < B < C: # ввод условия, что переменные введены в порядке возрастания
    A = A * 2
    B = B * 2
    C = C * 2 # удвоение переменных в случае выполнения условия
else: # ввод оператора "иначе"
    A = - A
    B = - B
    C = - C # присвоение заданным переменным обратных значений
print(A, B, C)  # вывод результата пользователю

