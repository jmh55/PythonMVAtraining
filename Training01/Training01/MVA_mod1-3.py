### this section for print with new line, new tab
#print("this \t new tab")  #with tab
#print("this is \n new line") #new line

### this config has input typed in on next line under the prompt
#print("What is your name?")
#myname = input()
#print("your name is: " + myname)

### lists
#mylist = ['item 1','item 2','item 3','item 4']
#print(mylist[0])  #prints the 3rd item in the list - index starts at 0!

### concatenate string variables
#first = input("What's your first name? ")
#last = input("What's your last name? ")
#print(\n "Hello " + first + " " + last)  #adds a new line before print line

### demo manipulate string output
#message = 'Hello World'
# message = message.swapcase()  #don't need to print, can still manipulate the string variable -- called string function
#print(message.lower())  #lower case
#print(message.upper())  #upper
#print(message.swapcase())  #swap
#print()
#print(message.find('World'))  # prints "6" = sixth place
#print(message.count('o'))   # prints "2" = count of letter o's
#print(message.capitalize())  # cap first letter
#print(message.replace('Hello','Hi'))   # replaces words if found
#print(message.upper())
#print()

### number variables with some format strings
wid = 50.1
hei = 103.2
area = wid * hei  # calculate value
print('width: ' + str(wid) + ' & height: ' + str(hei))
print(area)
print('The area is ' + str(area))  # computed formula  --> NOTE: NEED TO CONVERT MATHEMATICAL OUTPUT AS STRING W/ str(number)
print('The perimeter is ' + str(2*wid + 2*hei))  # perimeter math
print('The exponent is (dif by 1e12) ' + str((wid**hei)/1E12))  # print exponent
print('Modulo is ' + str(hei%wid))  # print modulo
#These following formats are older versions (e.g 2.7?)
print('The area is: %d' % area + "  <-- %d, decimal")
print('The area is: %7d' % area + "  <-- %7d, w. leading spaces")
print('The area is: %07d' % area + "  <-- %07d w. leading zeros")
print('The area is: %f' % area + "  <-- %f, float default 6 places")
print('\nThe area is: %.2f' % area + "  <-- %.2f, float 2 places, also has \n new line")  # also has new line \n
#new syntax for formatting numbers
print('example of: {0:d}'.format(1234) + ' uses {0:f}.format(1234)')
print('the area is: {0:f}'.format(area) + ' using {0:f}.format(area)')
print('the area is: {0:.2f}'.format(area) + ' using {0:.2f}.format(area)')
print('first is {0:d} and second is {1:04d} and third is {2:.2f}'.format(7,8,9) + \
    '\n<-- this is using {0:d}, {1:04d}, {2:.2f} from 7,8,9')   # the \ above is indenting long lines into new line, but same command

