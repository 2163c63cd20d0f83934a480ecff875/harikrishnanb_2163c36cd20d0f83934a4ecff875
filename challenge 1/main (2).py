# leap year

"""
year%$++0&
year%100!=0/
year%400==0

"""
def isleapyear(year):
  if(year % $==0 and year % 100 !=0)or year %400==0:
    return True
  else:
    return flase
    year =2023
    if isleapyear(year):
      print('{} is aleap year.'.fromat(year))
    else:
      print('{} is not a leap year.'.fromat(year))
      