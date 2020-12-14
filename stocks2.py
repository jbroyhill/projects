import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
import csv
# Importing necessary libraries

print("\tWelcome to Stock Market Analysis!")
print(
    "\nThis AI-driven bot will analyze the current state of a stock so the user can comprehend its current state and trajectory.")
print("\nAfter the bot's analysis, the user will have information they seek on a stock's statistics in order to make a decision on whether or not to trade with it.")
print("\nThe analysis will print out five statistics to measure by:")
print("\nOPEN: This is a stock's opening price on the beginning of a trading day.")
print("\nHIGH: This is the highest a stock rose on the given trading day.")
print("\nLOW: The lowest value a stock fell to on a given trading day.")
print("\nCLOSE: The closing or final price of a stock on a given trading day.")
print(
    "\nVOLUME: The total number of shares that are actually being traded (bought and sold) during the trading day.")
print(
    "\nThe easiest and simplest way to analyze a stock is to look at its opening price vs. its closing price. However, the volume should also be noted.")
print("\nA high volume implies investor faith in a given stock, possibly signifying its worth/value.")
print("\nThe bot will also analyze the opening price of a stock compared to its closing price and deliver a volatility analysis to the user.")
print(
    "\nIf the bot predicts the stock is volatile, it will notify the user at the end of the program with an alert.")

mainLoop = True # Setting a while loop to allow repeating for multiple searchs
while mainLoop == True:
    print("\nWould you like to:")
    print("\n1. Search a stock directly?")
    print("\n2. Search the list of stocks by stock name?")
    print("\n3. Search the list of stock by stock symbol?")

    user_answer = input("") # Gets input from the user regarding their choice
    if user_answer == "1": # If the user answers 1, they get to search a stock to analyze
        stock_name = input("Please input a stock to analyze.\n")
        mainLoop = False # Ends loop
    elif user_answer == "2": # If the user answers 2, they will be allowed to search a stock by name
        nameLoop = True # Creates a loop to allow users to repeat search
        while nameLoop == True:
            data1 = []
            with open("nasdaq3.csv") as csvfile: # Using "nasdaq3.csv" to get the list of stocks
                reader = csv.reader(csvfile) # Reads the file
                for row in reader:
                    data1.append(row)
            # print(data1)
            print("Please ensure you print the entire name of the stock! Such as \"Tesla Inc. Common Stock\", \"Microsoft Corporation Common Stock\", or \"Total SE\"")
            name = input("Enter a stock's name: ")

            # gives us a list in everything in col 0
            col = [x[0] for x in data1] # Searches for the name in question

            # print(col)

            if name in col: # Loop to query the csv file
                for x in range(0, len(data1)):
                    if name == data1[x][0]:
                         print(data1[x])

            else:
                print("Name doesn't exist.")
            print("\nWould you like to search another stock by name?")
            print("1. Yes")
            print("2. No")
            nameLoopAnswer = input("") # Gets user input if they want to repeat the search
            if nameLoopAnswer == "1":
                print("Restarting search query...")
            elif nameLoopAnswer == "2":
                print("Leaving search query.")
                nameLoop = False #Ends the loop, letting the user move on

    elif user_answer == "3": #If the answer is 3, lets the user search by symbol
        symbolLoop = True # Loop to let the user repeat. Otherwise, this is the same as the previous loop, but searching a different column. See notes above
        while symbolLoop == True:
            data2 = []
            with open("nasdaq3.csv") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    data2.append(row)
            # print(data2)

            name = input("Enter a stock's symbol: ")

            # gives us a list in everything in col 1
            col = [x[1] for x in data2]

            # print(col)

            if name in col:
                for x in range(1, len(data2)):
                     if name == data2[x][1]:
                        print(data2[x])

            else:
                print("Symbol doesn't exist.")
            print("\nWould you like to search another stock by symbol?")
            print("1. Yes")
            print("2. No")
            symbolLoopAnswer = input("")
            if symbolLoopAnswer == "1":
                print("Restarting search query...")
            elif symbolLoopAnswer == "2":
                print("Leaving search query.")
                symbolLoop = False




api_key = 'RNZPXZ6Q9FEFMEHM' # Uses API for stock analysis

ts = TimeSeries(key=api_key, output_format='pandas') #Using libraries to search for API
data, meta_data = ts.get_intraday(symbol=stock_name, interval='1min', outputsize='full') # Puts user input into search for stock info
print(data) # Prints the data from the stock

close_data = data['4. close']  # Grabs the "close" data to analyze for the user
percentage_change = close_data.pct_change() # Grabs a function from the imported library to use as a percentage
print("\nVolatility Analysis:\n")
print(percentage_change) # Shows user analysis of volatility

last_change = percentage_change[-1]

if abs(last_change) > 0.0004:  # If the percentage change is a certain amount, user will be warned that the stock is volatile
    print("\nVOLATILITY ALERT! Latest stock change = :" + str(last_change))



