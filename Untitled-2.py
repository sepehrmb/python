def salary(ho,hours):
    if(hours>8):
        return("you are not permitited to work more than 8 houts")
    else:
        return("your salary is =",ho*hours)

x=int(input(" please enter how much money do you get for each hours: "))
y=int(input("please enter how many hours do you work: "))

print(salary(x,y))
