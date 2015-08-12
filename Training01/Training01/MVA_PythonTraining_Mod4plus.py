import datetime

curdate = datetime.date.today()  #YYYY-MM-DD
print(curdate)
print(curdate.year)  #property of the item, gives YYYY
print(curdate.month)
print(curdate.day)

#strftime allows to specify the date format --> 'string from time'

print (curdate.strftime('%a, %B %d %Y'))
# %b = month (Jun)
# %B = full month name (June)
# %y = 2-digit year,  %Y = 4 digit year
# %a = day of week abbreviated (Mon)
# %A = day of the week (Monday)
# strftime.org = doc
print()
print(curdate.strftime('%d-%b-%y').lower())  #11-aug-2015

#strptime allows to specify the date from input --> string input time
birthday = input('What is your birthday? (e.g. mm/dd/yyyy) ')
birthdate = datetime.datetime.strptime(birthday, "%m/%d/%Y")
#   datetime/datetime class -> module -> function, so need twice
#                             birthday = input
#                                       format expected 12/18/1974

# Find the difference of 2 days
print('Your birth month is ' + birthdate.strftime('%B'))
print() 
print()
futuredate = input('enter a future date: (e.g. 12/25/2020) ')
nextBday = \
    datetime.datetime.strptime(futuredate,'%m/%d/%Y').date()
                 # the .date() above = date specifically needed
currentDate = datetime.date.today()
difference = nextBday - currentDate
print(str(difference.days) + ' days from then')  #.days = just the days
print()

# also checkout dateutil

#  %H = hours (24hr)  %l = hours (12) %p (AM/PM) %m min %S sec
rightnow = datetime.datetime.now()
print(datetime.datetime.strftime(rightnow, 'The time is: %H:%M'))
# .hour  .minute  .second


