# PROG1700 - Jin
"""
Name : Myeongjin Kwon(Jin)\

ID...: W0417939

"""

import math

def main():
    #input
    ask = input("Please enter your original bill amout: ")
    
    #process
    bill = int(85)
    tax = float(ask) * float(0.15)
    tip = float(ask) * float(0.20) 
    total = float(ask) + float(tax) + float(tip)

    #output
    print("Your original bill amount is: " + str(ask))
    print("Your tip is: " + str(tip))
    print("Your tax is: " + str(tax))
    print("Your total is: " + str(total))


if __name__ == "__main__":
    main()
