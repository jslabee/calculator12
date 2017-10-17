
operation = raw_input("chose math operation (+,-,*,/): ")
x = int(raw_input("enter the valoe for x: "))
y = int (raw_input("enter the value for y: "))



if operation == "+" :
    print(x+y)
elif operation == "-" :
    print(x-y)
elif operation == "*" :
    print(x*y)
elif operation == "/" :
    print(x/y)
else:
    raise ValueError("WRONG OPERATION!")
#print(x+y)

