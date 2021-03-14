year = int(input("Enter a number: "))
if (year % 4) == 0:
   print("{0} is leap year".format(year))
else:
   print("{0} is not leap year".format(year))