#!/usr/bin/env python
# coding: utf-8

### Python Project 15: Mobile App for Lottery Addiction
# For the first version of the app, we are focusing on the 6/49 lottery and 
# build functions that can answer users the following questions:
# - What is the probability of winning the big prize with a single ticket?
# - What is the probability of winning the big prize if we play 40 different tickets (or any other number)?
# - What is the probability of having at least five (or four, or three) winning numbers on a single ticket?
 
# We are also considedring historical data coming from the national 6/49 lottery game in Canada. 
# The data set has data for 3,665 drawings, dating from 1982 to 2018.

#### Core Functions
# We're going to write two functions that we'll be using frequently:
# - factorial() — a function that calculates factorials
# - combinations() — a function that calculates combinations
def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i
    return final_product

def combinations(n, k):
    numerator = factorial(n)
    denominator = factorial(k) * factorial(n-k)
    return numerator/denominator

#### One-ticket Probability
# We need to build a function that calculates the probability of winning the big prize for any given ticket. 
def one_ticket_probability(user_numbers):
    
    n_combinations = combinations(49, 6)
    probability_one_ticket = 1/n_combinations
    percentage_form = probability_one_ticket * 100
    
    print('''Your chances to win the big prize with the numbers {} are {:.7f}%.
In other words, you have a 1 in {:,} chances to win.'''.format(user_numbers,
                    percentage_form, int(n_combinations)))


# We now test a bit the function on two different outputs.
test_input_1 = [2, 43, 22, 23, 11, 5]
one_ticket_probability(test_input_1)

test_input_2 = [9, 26, 41, 7, 15, 6]
one_ticket_probability(test_input_2)

#### Historical Data Check for Canada Lottery
# We also need to consider the data coming from the national 6/49 lottery game in Canada. 
# The data set contains historical data for 3,665 drawings, dating from 1982 to 2018.
# The file is saved as `649.csv` and read into the dataframe.
import pandas as pd

lottery_canada = pd.read_csv('649.csv')
lottery_canada.shape
lottery_canada.head(3)
lottery_canada.tail(3)


#### Function for Historical Data Check
# writing a function that can help users determine whether they would have ever won by now using a certain combination of six numbers. 
# Extracting all the winning numbers from the lottery data set. 
# The `extract_numbers()` function will go over each row of the dataframe and extract the six winning numbers as a Python set.
def extract_numbers(row):
    row = row[4:10]
    row = set(row.values)
    return row

winning_numbers = lottery_canada.apply(extract_numbers, axis=1)
winning_numbers.head()

# Below, we wrote the `check_historical_occurrence()` function that takes in the user numbers and the historical numbers and 
# prints information with respect to the number of occurrences and the probability of winning in the next drawing.
def check_historical_occurrence(user_numbers, historical_numbers):   
    '''
    user_numbers: a Python list
    historical numbers: a pandas Series
    '''
    
    user_numbers_set = set(user_numbers)
    check_occurrence = historical_numbers == user_numbers_set
    n_occurrences = check_occurrence.sum()
    
    if n_occurrences == 0:
        print('''The combination {} has never occured.
This doesn't mean it's more likely to occur now. Your chances to win the big prize in the next drawing using the combination {} are 0.0000072%.
In other words, you have a 1 in 13,983,816 chances to win.'''.format(user_numbers, user_numbers))
        
    else:
        print('''The number of times combination {} has occured in the past is {}.
Your chances to win the big prize in the next drawing using the combination {} are 0.0000072%.
In other words, you have a 1 in 13,983,816 chances to win.'''.format(user_numbers, n_occurrences,
                                                                            user_numbers))

# We now test a bit the function on two different outputs.
test_input_3 = [33, 36, 37, 39, 8, 41]
check_historical_occurrence(test_input_3, winning_numbers)

test_input_4 = [3, 2, 44, 22, 1, 44]
check_historical_occurrence(test_input_4, winning_numbers)

#### Multi-ticket Probability
# The function below takes in the number of tickets and prints probability information depending on the input.
def multi_ticket_probability(n_tickets):
    n_combinations = combinations(49, 6)
    probability = n_tickets / n_combinations
    percentage_form = probability * 100
    if n_tickets == 1:
        print('''Your chances to win the big prize with one ticket are {:.6f}%.
In other words, you have a 1 in {:,} chances to win.'''.format(percentage_form, int(n_combinations))
    else:
        combinations_simplified = round(n_combinations / n_tickets)   
        print('''Your chances to win the big prize with {:,} different tickets are {:.6f}%.
In other words, you have a 1 in {:,} chances to win.'''.format(n_tickets, percentage_form,
                                                               combinations_simplified))

# Below, we run a couple of tests for our function.
test_inputs = [1, 10, 100, 10000, 1000000, 6991908, 13983816]
for test_input in test_inputs:
    multi_ticket_probability(test_input)
    print('------------------------') # output delimiter

#### Less Winning Numbers — Function
# The function below calculates the probability that a player's ticket matches exactly the given number of winning numbers. 
# If the player wants to find out the probability of having five winning numbers, the function will return the probability 
# of having five winning numbers exactly (no more and no less). The function will not return the probability of having at least five winning numbers.
def probability_less_6(n_winning_numbers):
    
    n_combinations_ticket = combinations(6, n_winning_numbers)
    n_combinations_remaining = combinations(43, 6 - n_winning_numbers)
    successful_outcomes = n_combinations_ticket * n_combinations_remaining
    
    n_combinations_total = combinations(49, 6)    
    probability = successful_outcomes / n_combinations_total
    
    probability_percentage = probability * 100    
    combinations_simplified = round(n_combinations_total/successful_outcomes)    
    print('''Your chances of having {} winning numbers with this ticket are {:.6f}%.
In other words, you have a 1 in {:,} chances to win.'''.format(n_winning_numbers, probability_percentage,
                                                               int(combinations_simplified)))

# Now, let's test the function on all the three possible inputs.
for test_input in [2, 3, 4, 5]:
    probability_less_6(test_input)
    print('--------------------------') # output delimiter

### Above code has four main functions:
# - one_ticket_probability() — calculates the probability of winning the big prize with a single ticket
# - check_historical_occurrence() — checks whether a certain combination has occurred in the Canada lottery data set
# - multi_ticket_probability() — calculates the probability for any number of of tickets between 1 and 13,983,816
# - probability_less_6() — calculates the probability of having two, three, four or five winning numbers exactly
