#first sloution
number_list = []
while True:
    num = input("Enter number : ")
    if num == "ok":
        break
    else:
        number_list.append(int(num))
print(number_list)

print(*reversed(sorted(number_list)))

#second solution
number_list = []
while True:
    num = input("Enter number : ")
    if num == "ok":
        break
    else:
        number_list.append(int(num))
print(number_list)

max_numbers = []
while True:
    len_big = len(max_numbers)
    if len_big < 5:
        maxi = max(number_list)
        max_numbers.append(maxi)
        number_list.remove(maxi)
    else :
        print(max_numbers)
        break
