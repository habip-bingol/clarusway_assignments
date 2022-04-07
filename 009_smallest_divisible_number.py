# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 10?
i = 1
while True:
    if all(i%j==0 for j in range(1,11)):
        print(i)
        break
    i +=1