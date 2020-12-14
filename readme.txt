This is a Stock Analysis bot that takes a stock and analyzes its current statistics, assembling a volatility analysis for the user so they can consider whether or not to trade it.

Originally I was going to have the bot predict future stock prices, but considering the ((relatively speaking) astromonical amount of work I would have to do to create my own bot
that did such a task, I decided on current analysis instead with a focus on volatility.

The only thing needed for this bot to work is the "nasdaq3.csv" file to read from and the python libraries it seeks to import (pandas, TimeSeries, Time, and csv).

The application allows the user to query a spreadsheet of stocks to gain their symbol or vice versa before searching the stock's statistics for an analysis.

The only issue I currently have with it is that in order to search a stock by name, the user has to enter it completely correctly. This isn't technically a bug, but in the future
I would like to have it so the user can enter part of a name ans the bot will reply with suggestions that match the segment of the string given.


I hope you enjoy the bot!