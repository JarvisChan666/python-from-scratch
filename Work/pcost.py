# pcost.py
#
# Exercise 1.27

# open file

# total_cost = 0

# f = open('Data/portfolio.csv', 'rt')
# # read all lines
# with open('Data/portfolio.csv', 'rt') as file:
#     header = next(file)
#     for line in file:
        
#         row = line.split(',')
#         print(row[1], row[2])
#         cost = float(row[1]) * float(row[2])
#         total_cost += cost
# print('Total cost:', total_cost)



# calculates how much it cost to purchase all of the shares in the profolio

# Exercise 1.28

import gzip
with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
    
    for line in f:
        print(line, end='')