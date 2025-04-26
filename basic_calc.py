# Function to perform the arithmetic operation: Addition
def add(num_1, num_2):
   return num_1 + num_2
# Function to perform the arithmetic operation: Subtraction
def subtract(num_1, num_2):
   return num_1 - num_2
# Function to perform the arithmetic operation: Multiplication
def multiply(num_1, num_2):
   return num_1 * num_2
# Function to perform the arithmetic operation: Division
def divide(num_1, num_2):
   return num_1 / num_2
print("Hi, This is the Basic console based calculator!\n")

num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))
print(add(num_1,num_2))
print(subtract(num_1,num_2))
print(multiply(num_1,num_2))
print(divide(num_1,num_2))

while True:
   print("Please select which of the following arithmetic operation you want me to perform-\n\n" \
   "1. Add\n" \
   "2. Subtract\n" \
   "3. Multiply\n" \
   "4. Divide\n")
   operation = int(input(" Enter your choice of operation you want to perform: 1, 2, 3, 4 :\n"))
   if operation == 1:
    num_1 = int(input('Please, Enter the first number: \n'))
    num_2 = int(input('Please, Enter the second number: \n'))
    print('\nAddition of {} + {} = '.format(num_1, num_2), add(num_1, num_2),"\n")
   elif operation == 2:
    num_1 = int(input('Please, Enter the first number: \n'))
    num_2 = int(input('Please, Enter the second number: \n'))
    print('\nSubtraction of {} - {} = '.format(num_1, num_2), subtract(num_1, num_2),"\n")
   elif operation == 3:
    num_1 = int(input('Please, Enter the first number: \n'))
    num_2 = int(input('Please, Enter the second number: \n'))
    print('\nMultiplication of {} * {} = '.format(num_1, num_2), multiply(num_1, num_2),"\n")
   elif operation == 4:
    num_1 = int(input('Please, Enter the first number: \n'))
    num_2 = int(input('Please, Enter the second number: \n'))
    print('\nDivision of {} / {} = '.format(num_1, num_2), divide(num_1, num_2),"\n")
   elif operation > 4:
    print("Thank you for using calculator.")
    break
   else:
    print("\nPlease enter valid input\n")
