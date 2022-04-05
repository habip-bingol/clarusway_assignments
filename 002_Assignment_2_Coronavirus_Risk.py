#we assume that if you have two of the amoung below criterias, you're in risky group. If not, you're not in risky group 
print(" ANSWER THE QUESTİONS AS YES/NO ")
age = input("Are you a cigarette addict older than 75 years old?  : ").capitalize()
chronic = input(" Do you have a severe chronic disease? : ").capitalize()
immune = input("Is your immune system too weak? :  ").capitalize()

if (age == "yes" and chronic == "yes" ):
  print("you're in risky group")

elif (immune == "yes" and chronic == "yes" ):
  print("you're in risky group")

elif (age == "yes" and chronic == "yes" ):
  print("you're in risky group")
else :
  print("You are not in risky group")
