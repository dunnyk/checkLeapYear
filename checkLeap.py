def checkLeapYear(year):
    if ((user_out % 4 ==0) or (user_out % 400 == 0)):
        print(f'{user_out} is a leap year')
    else:
        print(f'{user_out} is not a leap year')
user_out = int( input('Enter year: '))
checkLeapYear('year')