a = int(input("First number:"))
b = int(input("divided by second number:"))

def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Error: cannot divide by 0.")
    else:
        print(result)
divide(a,b)