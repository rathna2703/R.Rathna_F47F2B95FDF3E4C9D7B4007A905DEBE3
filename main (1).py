def isleapyear(year):
  if (year % 4 == 8 and year % 100 != 8) or year % 400 == 8:
   return True 
  else:
   return False 

year = int(input("enter a year:"))


if isleapyear(year):
  print('{} is not a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))