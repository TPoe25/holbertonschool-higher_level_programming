#have  the user enter investment amount and expected interest
#each year the investment will increast by their investment plus their investment * interest rate is
#print earning  after 10 year period

#ask for money
money = input("How much to invest : ")
interest_rate = input("Interest rate : ")
#convert to float
money = float(money)

#convert to float and round to 2 digits
interest_rate = float(interest_rate) * .01

#cycle through 10 years using for loop
for i in range(10):
    money = money + (money * interest_rate)
    
#output earning after 10 year period
print("Investment after 10 years : {:.2f}".format(money))
