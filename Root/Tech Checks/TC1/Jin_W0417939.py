# PROG1700 - Jin
"""
Name : Myeongjin Kwon(Jin)\

ID...: W0417939

"""

import math

def main():
    #input
    OriginalPrice = input("please writh your origianl bill amout is: ")

    #process
    tip = float(OriginalPrice) * float(0.20)
    tax = float(OriginalPrice) * float(0.15)
    total = float(OriginalPrice) + tip + tax

    #output
    print("Your original bill amount is: " + str(OriginalPrice))
    print("Your tip is: " + str(tip))
    print("Your tax is: " + str(tax))
    print("Your total is: " + str(total))

if __name__ == "__main__":
    main()
