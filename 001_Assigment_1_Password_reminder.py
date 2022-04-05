password = """W@12!'1"""
name  = "Habip"
your_name = str(input("enter your name for accessing password :  "))
your_name = your_name.title()
if your_name == name :
  print(f"Hello {your_name}! The password is {password}")
else :
  print(f"hello {your_name}! See you later.")