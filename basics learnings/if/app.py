weight = float(input("Weight: "))
option = input("(K)g or (L)bs: ")

if option.upper() == "K":
    print("Weight in Kg: ", weight / 0.45) 
elif option.upper() == "L":
    print("Weight in Pounds: ", (weight*450)/1000)
else:
    print("Wrong option")
