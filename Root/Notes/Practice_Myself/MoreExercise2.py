# PROG1700 - JIN
"""
MoreExercise - round 2

Name : Myeongjin Kwon (Jin)

ID...: W0417939
"""

__AUTHOR__ = "Jin<W0417939@nscc.ca>"

import math

def main():
    #input
    fixedCosts = int(5000)
    pricePerUnit = int(8)
    costPerUnit = int(6)

    #process
    fixedCosts2 = fixedCosts * 2
    pricePerUnit2 = pricePerUnit * 2
    costPerUnit2 = costPerUnit * 2

    divide = (fixedCosts2 / (pricePerUnit2 / costPerUnit2))  
    breakEvenPoint = divide
    
    #output
    print(" :" + str(breakEvenPoint))


    

if __name__ == "__main__":
    main()

