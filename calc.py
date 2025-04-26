n1 = int(input('Enter first number: '))
op = input('Enter operator(+,-,*,/,^): ')
n2 = int(input('Enter second number: '))
print(n1,op,n2)

def calculate(n1,n2,op):
    if op == '+':
        result = n1+n2
    elif op == '-':
        result = n1-n2
    elif op == '*':
        result = n1*n2
    elif op == '/':
        result = n1/n2
    elif op == '^':
        result = n1**n2
    else:
        print('You did not mention it right! Please check again.')


