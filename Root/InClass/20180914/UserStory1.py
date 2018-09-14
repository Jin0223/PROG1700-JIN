# PROG1700-JIN
"""
In Class - User Story 1

Name : Myeongjin Kwon (JIN)

ID...: W0417939

"""

__AUTHOR__ = "Jin <w0417939@nscc.ca>"


import math


def main():
    # input
    order = input("Hello. How many cups of coffee do you want to order? ")


    # process
    price = float(1.25)
    tax = float(0.15)
    PreCoffee = float(order) * price
    TaxCoffee = PreCoffee + tax


    # Output
    print("You order " + order + "cup(s) of coffee. ")
    print("Before Pre-tax cost of the order is " + str(PreCoffee) + " dollars. ")
    print("The tax is 15%. ")
    print("So, your total amount of coffee is " + str(TaxCoffee) + " dollars. ")
    print("Thank you for coming today. Have a good day")
    

if __name__ == "__main__":
    main()
