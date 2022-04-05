#Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements and range() function.
fibonacci_list = [1,1]
i = 1
while True:
    fibo = fibonacci_list[i]+fibonacci_list[i-1]
    if fibo <= 55:
        fibonacci_list.append(fibo)
        i+=1
    else:
        break
print(fibonacci_list)

#second solution 
last_number = int(input("Write the last Fibonacci number you want to see in the list: "))
Fibo_numbers = []
a = 0
b = 1
for i in range(1,55):
    Fibo_numbers.append(b)
    a , b = b, a + b
    if b > last_number:
        break
    
print(f"Fibonacci numbers you want to list = {Fibo_numbers}")