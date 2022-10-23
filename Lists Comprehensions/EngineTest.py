# PEP 202 – List Comprehensions
#https://peps.python.org/pep-0202/

tank = 1000
power = 0
eficience = 3
while (tank > 0):
    [(power) for power in range(0,10) if (tank > 0) ]
    tank = tank - 100
    power = (power+1) * eficience   
    print(power,tank)
