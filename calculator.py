print("Если ввести ноль"
      "\nзавершит работу программы") # if x or y = 0 - function ends
while True:
    s = input("Ввдите знак (+,-,*,/): ") # user enters action sign
    if s == '0':
        break # 0 == break
    if s in ('+', '-', '*', '/'): # s in array +,-,*,/
        x = float(input("x: "))
        y = float(input("y: ")) # enter float number or for example: 4 = 4.00
        if s == '+':
            print("%.2f" % (x+y)) # operation +
        elif s == '-':
            print("%.2f" % (x-y)) # operation -
        elif s == '*':
            print("%.2f" % (x*y)) # operation *
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Ну, лучше не надо")
    else:
        print("Неверный знак операции!")