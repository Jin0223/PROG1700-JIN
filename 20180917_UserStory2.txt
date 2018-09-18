# PROG1700 - JIN
"""
Practice Myself - 20180917

Name : Myeongjin Kwon (Jin)

ID...: W0417939

"""

__AUTHOR__ = "Jin<W0417939@nscc.ca>"

import math

def main():
    #input
    order = input("How width is it? ")
    order2 = input("How length is it? ")
    order3 = input("How height is it? ")


    #process
    gallon = 150

    width = int(order)
    length = int(order2)
    height = int(order3)

    wall_width = width * height * 2
    wall_length = length * height * 2
    total = wall_width + wall_length
    paint = total / gallon

    #output
    print("You need to buy " + str(paint) + " gallons ")


if __name__ == "__main__":
    main()


