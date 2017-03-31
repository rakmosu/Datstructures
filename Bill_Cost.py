import sys
import os

bill= float(input('The cost of the meal before tax and tip ='))
tip= int(input('The percentage of meal cost being added as tip ='))
tax= int(input('The percentage of meal cost being added as tax ='))

total_cost = (bill + (bill * (tip/100)) + (bill * (tax/100)))


print ('The total meal cost is ',int(round(total_cost,0)),'dollars')