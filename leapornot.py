def leapornot(year):
  if(year%4==0):
    return 1
  else:
    return 0
try:
  year = int(input('Enter a year:'))
  print("The year you've entered is:", year)
  if(leapornot(year)):
    print(year,"is a leap year!")
  else:
    print(year,"is not a leap year!")
except:
  print("That's not a valid year!")
