def calculate(n1,n2,op):
    if op == '+':
        return n1+n2
    elif op == '-':
        return n1-n2
    elif op == '*':
        return n1*n2
    elif op == '/':
        return n1/n2
    elif op == '^':
        return n1**n2
    else:
        return None


n1 = int(input('Enter first number: '))
op = input('Enter operator(+,-,*,/,^): ')
n2 = int(input('Enter second number: '))
print(n1,op,n2)
result = calculate(n1,n2,op)
print(result)
