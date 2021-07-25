print('*********** WELCOME TO MY CALCULATOR ************')
while True:
  print()
  print("Please select the operation you want to perform : \n\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit\n")
  option = int(input("Enter pption here -> "))

  if option==1:
    no1=int(input("Enter First Number -> "))
    no2=int(input("Enter Second Number -> "))
    print(no1,' + ',no2,' = ',no1+no2)
    

  elif option==2:
    no1=int(input("Enter First Number -> "))
    no2=int(input("Enter Second Number -> "))
    print(no1,' - ',no2,' = ',no1-no2)
  
  elif option==3:
    no1=int(input("Enter First Number -> "))
    no2=int(input("Enter Second Number -> "))
    print(no1,' * ',no2,' = ',no1*no2)

  elif option==4:
    no1=int(input("Enter First Number -> "))
    no2=int(input("Enter Second Number -> "))
    print(no1,' / ',no2,' = ',no1/no2)

  elif option==5:
    print("Thanks for using my calculator!")
    break
  
  else:
    print("""Operation is not available....Try something else!""")