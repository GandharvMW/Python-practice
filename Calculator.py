first_number=float(input('this a calculator give a number:'))
second_number=float(input('this a calculator give 2nd number:'))

operation=input('which operation you want to perform :')


if operation== '+':
    result=first_number+second_number

elif operation== '-':
    result=first_number-second_number

elif operation == '*':
    result=first_number*second_number

elif operation == '/':
    if second_number!=0:
        result=first_number/second_number
    else:
        result="Error: Invalid Operation"
else:
    result="Invalid Operation"


print("Result:", result)



