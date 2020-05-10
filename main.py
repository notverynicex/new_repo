print('Insert two numbers please (only positives)')
while True:
    a = int(input())
    b = int(input())
    if (a>-1) and (b>-1):
        print(f"Thank you for inputting the numbers {a} and {b}")
        print(f"The sum of the numbers is {a + b}")
        print(f"The difference of numbers is {a - b}")
        break
    elif (a<0) or (b<0):
        print('You made a mistake, please verify the numbers!')

