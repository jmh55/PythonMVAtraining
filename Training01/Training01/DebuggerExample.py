# new py file in solution.  Right clicked and selected 'set as startup file'
#<-- click to add break.  then you can step into...  hover over variable gives clues
salary = input('enter salary ')
bonus = input('enter bonus ')
totalpay = salary + bonus
print(totalpay)

#functions to convert string to numeric
#  int(value) = conver to integer
#  long(value) = convert to long integer
#  float(value) = number that can hold decimal places
#  str(value) = convert to string

salary = float(salary)
bonus = float(bonus)
totalpay = salary + bonus
print('{0:.2f}'.format(totalpay))  #<-- this formats float into 2 decimal points for cents


