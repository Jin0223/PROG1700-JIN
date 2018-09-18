# PROG1700 - Jin
"""
Name : Myeongjin Kwon(Jin)

ID...: W0417939
"""

__AUTHOR__ = "Jin<W0417939@nscc.ca>"

import math

def main():
    #input 
    costPerShare = float(25.625)
    numberOfShares = int(400)


    #process
    original = costPerShare * numberOfShares
    markdown = float(original) / 2

    #output
    print("The orginal amount of a stock purchase is " + str(original) + " dollars. ")
    print("The markdown amount of a stock purchase is " + str(markdown) + " dollars. ")
    print("Oh my gosh! ")

if __name__ == "__main__":
    main()
