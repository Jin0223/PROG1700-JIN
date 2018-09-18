# PROG1700 - JIN
"""
More Exercise - round 4 

Name : MyeongJin Kwon

ID...: W0417939

"""
__AUTHOR__ = "Jin<W0417939@nscc.ca>"

import math

def main():

    #input
    ask = input("Do you know how many slices of pizza American eat? y or n ? ")
    if ask == ("y"):
        print("How did you know that? ")
    else:
        print("Do you know ")
    #process
    pizzaPerSecond = int(350)
    second = int(60)
    hour = int(60)
    aDay = int(24)
    perDay = second * hour * aDay
    sellPizza = pizzaPerSecond * perDay

    #output
    print(" Americans eat an average of 350 slices of pizza per second ")
    print(" They are eat " + str(sellPizza) + " per day. " )
    print("Surprise!")
  
if __name__ == "__main__":
    main()

