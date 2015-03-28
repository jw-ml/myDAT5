# -*- coding: utf-8 -*-x

# jeremy
# https://gist.github.com/anonymous/d00626b6f29c6093f36a
# https://gist.github.com/d00626b6f29c6093f36a.git

'''
Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
PART 1: read in the data, parse it, and store it in a list of lists called 'data'
Hint: this is a tsv file, and csv.reader() needs to be told how to handle it
'''
import csv 
with open('DAT5/data/chipotle_orders.tsv', 'rU') as f:
    data = [row for row in csv.reader(f, delimiter='\t')]




'''
PART 2: separate the header and data into two different lists
'''
header = data[0]
data = data[1:]




'''
PART 3: calculate the average price of an order
Hint: examine the data to see if the 'quantity' column is relevant to this calculation
Hint: work smarter, not harder! (this can be done in a few lines of code)
'''

num_orders = len(set([row[0] for row in data])) # number of unique order_ids
tot_spent = 0.0

for order in data:
    tot_spent += float(order[4][1:]) # quantity already accounted for in 'item_price'

avg_order_price = tot_spent / num_orders
print 'The average order price is $%s \n' % round(avg_order_price, 2)



    
'''
PART 4: create a list (or set) of all unique sodas and soft drinks that they sell
Note: just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'
'''

# Approach 1 - list
# assumes 'Coke' was encoded by someone from Texas and could, therefore, be any type of soda
sodas = []
for row in data:
    if row[2] == 'Canned Soda' or row[2] == 'Canned Soft Drink':
        if row[3] not in sodas:
            sodas.append(row[3])

# Approach 2 - set
sodas2 = set([row[3] for row in data if row[2] == 'Canned Soda' or row[2]== 'Canned Soft Drink'])

print 'Chipotle sold the following Canned Sodas and Canned Soft Drinks: '
for soda in sodas2:
    print soda[1:-1]
print '\n'






'''
PART 5: calculate the average number of toppings per burrito
Note: let's ignore the 'quantity' column to simplify this task
Hint: think carefully about the easiest way to count the number of toppings
Hint: 'hello there'.count('e')
'''
b_list = [row for row in data if 'Burrito' in row[2] or 'Bowl' in row[2]]
num_top = 0.0
for row in b_list:
    num_top += row[3].count(',') + 1 # it appears all burritos and bowls have at least one topping

avg_num_toppings = num_top / len(b_list)
print 'The average number of toppings per burrito/bowl is %s \n'% round(avg_num_toppings,2)








'''
PART 6: create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: please take the 'quantity' column into account!
Advanced: learn how to use 'defaultdict' to simplify your code
'''

''' APPROACH #1 ''' # got side tracked by naming and pricing ...

# this function cleans the data to have consistent names for the same order
# need to know more about data; not cleaning produces better price consistency
def cleanChipsOrders(ch):
    for order in ch:
        if order[2] == 'Chips and Mild Fresh Tomato Salsa':
            order[2] = 'Chips and Fresh Tomato Salsa'
        elif '-' in order[2]:
            order[2] = order[2].replace('-', ' ')
    return ch

chips_orders = [row for row in data if 'Chips' in row[2]]
#chips_orders = cleanChipsOrders(chips_orders)
d = {}
for order in chips_orders:
    price = float(order[4][1:])/int(order[1]) # = item_price / quantity
    item = order[2]
    quantity = int(order[1])
    if item not in d:
        d[item] = [quantity]
        d[item].append([price])
    else:
        d[item][0] += quantity # add quantity of order
        if price not in d[item][1]:
            d[item][1].append(price)

#print 'Chipotle sold the following quantity of different chips combinations:'
#for k in d:
#    print '%s orders of %s' % (d[k][0], k)
#print '\n'    


''' APPROACH #2 '''
from collections import defaultdict
order_take_two = [(row[2], row[1]) for row in data if 'Chips' in row[2]]
d2 = defaultdict(int)
for k, v in order_take_two:
    d2[k] += int(v)

print 'Chipotle sold the following quantity of different chips combinations:'
for k in d2:
    print '%s orders of %s' % (d[k][0], k)





'''
BONUS: think of a question about this data that interests you, and then answer it!
'''

# Q: How much extra is guacamole on a burrito

# helper function
def hasGuacamole(s):
    if 'Guac' in s:
        return True
    else:
        return False
        
# recall, from above, b_list = [row for row in data if 'Burrito' in row[2]]
no_veg_b_list = [row for row in b_list if 'Veggie' not in row[2]]

# create a dictionary with the form d = {b_type: [[num with guac, totspent], [num wo guac, totspent]], ...
g = {}
for order in no_veg_b_list:
    quantity = int(order[1])
    burrito = order[2]
    hasGuac = hasGuacamole(order[3])
    order_spend = float(order[4][1:])
    # if burrito key not in dict g, initialize with zero values
    if burrito not in g:
        g[burrito] = [[0, 0.0],[0, 0.0]]
    # then, add quantity and spend amt to dict g
    if hasGuac:
        g[burrito][0][0] += quantity
        g[burrito][0][1] += order_spend
    else:
        g[burrito][1][0] += quantity
        g[burrito][1][1] += order_spend

# update g to have avg price instead of total spend
for b in g:
    g[b][0][1] = round(g[b][0][1]/g[b][0][0], 2)
    g[b][1][1] = round(g[b][1][1]/g[b][1][0], 2)

# calc price of guacamole
count, diff = 0, 0.0
for b in g:
    if b != 'Burrito' and b != 'Bowl':
        count += 1
        diff += g[b][0][1] - g[b][1][1]
        print '  price of guacamole add-on for %s is $%s' % (b, g[b][0][1] - g[b][1][1])

avg_p_guac = diff / count
print '\nThe average guacamole premium for a burrito is $%s' % round(avg_p_guac, 2)


