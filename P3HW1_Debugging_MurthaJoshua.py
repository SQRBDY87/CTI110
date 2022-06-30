# CTI - 110
# P3HW1-Debugging
# Joshua Murtha
# 6/26/2022


def main():

    
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50
    
    print()
    score = input("Please enter score: ")
    
    if score >= "90":
        print("Your grade is: A")

    elif score >= "80":
        print("Your grade is: B")

    elif score >= "70":
        print("Your grade is: C")

    elif score >="60":
        print("Your grade is: D")

    else:
        print("Your grade is: F")

       
main()        
