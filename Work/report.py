# report.py
#
# Exercise 2.4

import csv


# Take the function you wrote in Exercise 2.4 
# and modify to represent each stock in the portfolio with a dictionary instead of a tuple. In this dictionary use the field names of "name", "shares", and "price" to represent the different columns in the input file.
# def read_profolio(filename):
#     """Read a stock portfolio file and return a list of dictionaries representing the portfolio."""
#     profolio = []
#     with open(filename) as f:
#         reader = csv.reader(f)
#         next(reader) # skip the first row
#         for row in reader:
#             profolio.append
#     return profolio


def read_portfolio(filename):
    """Read a stock portfolio file and return a list of dictionaries representing the portfolio."""
    portfolio = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader) # skip the first row
        for row in reader:
            stock = {
                'name': row[0],
                'shares': int(row[1]),  # Convert shares to integer
                'price': float(row[2])  # Convert price to float
            }
            portfolio.append(stock)
    return portfolio

