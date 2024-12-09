def salary(ho,hours):
    if(hours>8):
        return("you are not permitited to work more than 8 houts")
    else:
        return("your salary is =",ho*hours)

print(salary(12.75,7))