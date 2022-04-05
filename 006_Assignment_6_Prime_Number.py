#first solution
number = int(input("please enter a number : "))
kalan = []
if number > 1:
    for i in range(2,number):
        a = number%i
        kalan.append(a)

    if 0 in kalan:
        print(f"{number} is not a prime number.")
    
    else   :
        print(f"{number} is  a prime number.")
else:
    print("please enter a number higher than 1.")
        

#second solution
num = int(input("please enter a number : "))
if num > 1 :
    for i in range(2,num):
        if (num % i) == 0:
         print(num,"is not a prime number")
         break
    else:
        print(num,"is a prime number")
else :
    print("please enter a number higher than 1.")