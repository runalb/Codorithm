# Runal Banarse
# Day 4 - 03/09/2020
# Write a program to check whether the inputted year is a leap year or not.

#user input
yr = int(input("Enter Year: "))

#checks leap year or not
if (yr % 4 == 0):
    #for century year
    if (yr % 100 == 0):
        if (yr % 400 == 0):
            res = "leap"
        else:
            res = "not a leap"
    else:
        res = "leap"
else:
    res = "not a leap"
#print result
print("{} is {} year".format(yr,res))

