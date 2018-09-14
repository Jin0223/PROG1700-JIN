# PROG1700-JIN
"""
In Class - User Story 2 

Name : Myeongjin Kwon (JIN)

ID...: W0417939

"""

__AUTHOR__ = "Jin <w0417939@nscc.ca>"

import math

def main():
    # Input
    length = input("please write to your length ")
    width = input("please write to your width ")
    height = input("please write to your height ")

    # Process
    length2 = int(length)
    width2 = int(width)
    height2 = int(height)    
     
    wall1 = length2 * height2 * 2
    wall2 = width2 * height2 * 2
    sqft = wall1 + wall2
    gallons = sqft / 150

    # Output
    displayGallons = str(gallons)
    displayGallons = "You will need " + displayGallons + " gallons." + "Thank you!"
    print(displayGallons)

if __name__ == "__main__":
    main()
 