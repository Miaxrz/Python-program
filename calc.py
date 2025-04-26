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

result = calculate(n1,n2,op)
print(n1,op,n2,'=',result)

continue_calculating = True
while continue_calculating is True:
       n1 = int(input('Enter first number: '))
       op = input('Enter operator(+,-,*,/,^): ')
       n2 = int(input('Enter second number: '))
       result = calculate(n1,n2,op)
       print(n1,op,n2,'=',result)
       yes_or_no = input('Continue? (y/n): ')
       if yes_or_no == 'n':
            continue_calculating = False
