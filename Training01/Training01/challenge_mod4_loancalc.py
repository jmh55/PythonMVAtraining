loan_amt = 0
irate = 0
n = 0
print("loan calculator\n")
loan_amt = input("enter loan amount: ")
loan_amt = float(loan_amt)
irate = input("enter interest rate: ")
irate = float(irate)
irate = irate / 100 
print("using " + str(irate) + " as the value")
n = input("number of payments: ")
n = float(n)
Mpay = loan_amt * irate / (1 - (1 + irate)**-n)
print("your monthly payment is {0:.2f}".format(Mpay))
print('\n and your total payments are... ' + str(Mpay * n))
## yay! matches excel =-PMT(0.05,12,1000,0,0) 