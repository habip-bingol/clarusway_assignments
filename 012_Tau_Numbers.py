# Let's print the tau numbers between 1-100 and the result will be => 1,2,8,9,12,18,24,36,40,56,60,72,80,84,88,96.
# WHAT DOES TAU NUMBER RULE AND TAU NUMBER MEAN?
#Tau numbers as a rule that Numbers divisible by the number of positive divisors are called numbers.
#The positive integer divisors of 9 are 1,3,9. Therefore, the number of positive integer divisors is 3.
#Since it is exactly divisible by 3, which is a divisor of 9, The number 9 is a Tau number.

list_tau = list()
n = int(input("Enter an integer: "))
for i in range(1, n + 1):
  list_i = []
  for j in range(1, n):
    if i % j == 0:
      list_i.append(j)
  if i % len(list_i) == 0:
    list_tau.append(i)
print(list_tau)
