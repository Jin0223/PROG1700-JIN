 # PROG1700 - JIN
"""
More Exercise - round 3

Name : Myeongjin Kwon (Jin)

ID...: W0417939
"""

__AUTHOR__ = "Jin<W0417939@nscc.ca>"

import math

def main():
    #input
    balance = int(100)

    #process
    year1 = balance * float(0.05) + 100
    year2 = year1 * float(0.05) + 100
    year3 = year2 + (year2 * float(0.05))
    year_last = round(year3, 2)

    #output
    print("Your original balance is " + str(balance) + " in 2016 ")
    print("Your balance is " + str(year1) + " in 2017 ")
    print("Your balance is " + str(year2) + " in 2018 ")
    print("Your balance is " + str(year_last) + " in 2019 ")

if __name__ == "__main__":
    main()
