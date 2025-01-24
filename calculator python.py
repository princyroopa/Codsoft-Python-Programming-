def calculate(n1, n2, operation):
    if operation=='add':
        return n1+n2
    elif operation=='subtract':
        return n1-n2
    elif operation=='multiply':
        return n1*n2
    elif operation=='divide':
        if n2!= 0:
            return n1/n2
        else:
            return 'Error! Division by zero'
    else:
        return "operations invalid"
print("Welcome to the simple calculator!")
n1=float(input("Enter the first number: "))
n2=float(input("Enter the second number: "))
print("Choose an operation:add,subtract,multiply,divide")
operation=input("Enter the operation: ").lower()
result=calculate(n1, n2, operation)
print(f"The result of {operation} between {n1} and {n2} is: {result}")
