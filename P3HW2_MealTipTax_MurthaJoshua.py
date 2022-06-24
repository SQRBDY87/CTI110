#CTI-110
#P3HW2-MealTipTax
#Joshua Murtha
#6/26/2022


cost = float(input("Please enter cost of meal: "))
tip = float(input("Please enter tip amout of 15, 18, or 20: "))
if tip  == 15 or tip == 18 or tip == 20: 
    print() 
    tip_amount = cost * (tip/100)
    print("Meal price: ", cost)
    print("Tax; ", cost * .06)
    print("Tip: ", tip_amount)
    print("Total: ", cost+(cost*.06)+tip_amount)
else:
    print("Error: user input wrong tip amout. Please again with proper tip ")
    

    
