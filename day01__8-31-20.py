# Runal Banarse
# Day 1 - 31/08/2020
# Write a program to Convert user inputted characters into ASCII value.


#get characters from users and stored in char var.
char = input("Enter characters: ")
temp = 0

#finding each user inputted character to it's ASCII value.
for x in char:
    #store ASCII value to ascii_value variable.
    ascii_value = ord(x)
    #print ASCII value of each character .
    print("ASCII value of",char[temp], "is", ascii_value)
    #incerment temp to get index position of the character
    temp = temp + 1



