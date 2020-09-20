# Runal Banarse
# Day 5 - 04/09/2020
# Write a program to convert specified days into years, weeks and days. Eg. 1329 days = 3 years 33 weeks 3 days. Note:- Ignore leap year


#user input
dy = int(input("Enter days: "))

#find years from user inputted days
year = int(dy / 365)

#find weeks from user inputted days
week = int( (dy % 365) / 7 )

#find days from user inputted days
day = int(dy % 365) % 7

print("{} years, {} weeks, {} days.".format(year,week,day))
