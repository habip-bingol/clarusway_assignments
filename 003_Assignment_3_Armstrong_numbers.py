number = input('Enter a number please : ')
while not number.isdigit():
    number = input('Wrong answer. Please enter a number :  ')
power = len(number)
total = 0
for i in range(len(number)):
    total += int(number[i]) ** power
if total == int(number):
    print('It is armstrong number.')
else:
    print('It is NOT armstrong number.')