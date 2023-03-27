# on every year that is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400

# re-using old is_leap_year project code
def is_leap(year):
  """takes any year as input and determines if it is leap.""" # doc-string
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(user_year, user_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

  if is_leap(user_year) == False:
    return month_days[user_month - 1]
  else:
    month_days[1] = 29
    return month_days[user_month - 1]
  
    
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)