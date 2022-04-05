number = int(input("enter a number please : "))
division_list = []
for i in range(1, int(number/2+1)):
    if number%i == 0:
        division_list.append(i)
              
if sum(division_list) == number:
    print("it's an excellent number.")
else:
    print("it's not excellent number.")


