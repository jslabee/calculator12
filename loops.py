break_loop = False

while not break_loop:
    x = int(raw_input("enter the value for x : "))
    y = int(raw_input("enter the value for y : "))


    if x % y == 3 :
       print ("0st = 3")
    elif x % y == 0:
        break_loop = True


