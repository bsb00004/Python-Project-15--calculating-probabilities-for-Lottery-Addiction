## Python Project 15: Mobile App for Lottery Addiction
In this project, we are going to contribute to the development of a mobile app by writing a couple of functions that are mostly focused on calculating probabilities. The app is aimed to both prevent and treat lottery addiction by helping people better estimate their chances of winning.

### Introduction
Many people start playing the lottery for fun, but for some this activity turns into a habit which eventually escalates into addiction. Like other compulsive gamblers, lottery addicts soon begin spending from their savings and loans, they start to accumulate debts, and eventually engage in desperate behaviors like theft.

The app idea comes from a medical institute which is specialized in treating gambling addictions. The institute already has a team of engineers that will build the app, but here we are creating the logical core of the app and calculate probabilities. 

For the first version of the app, we are focusing on the [6/49 lottery](https://en.wikipedia.org/wiki/Lotto_6/49) and build functions that can answer users the following questions:

- What is the probability of winning the big prize with a single ticket?
- What is the probability of winning the big prize if we play 40 different tickets (or any other number)?
- What is the probability of having at least five (or four, or three) winning numbers on a single ticket?

We are also considedring historical data coming from the national 6/49 lottery game in Canada. [The data set](https://www.kaggle.com/datascienceai/lottery-dataset) has data for 3,665 drawings, dating from 1982 to 2018 (we'll come back to this).

The scenario we're following throughout this project is fictional — the main purpose is to practice applying probability and combinatorics (permutations and combinations) concepts in a setting that simulates a real-world scenario.

### Core Functions
Below, we're going to write two functions that we'll be using frequently:

- factorial() — a function that calculates factorials
- combinations() — a function that calculates combinations

### Historical Data Check for Canada Lottery
We also need to consider the data coming from the national _6/49 lottery_ game in Canada. The data set contains historical data for 3,665 drawings, dating from 1982 to 2018 (the data set can be downloaded from [here](https://www.kaggle.com/datascienceai/lottery-dataset)).

The file is saved as `649.csv` and read into the dataframe.

## Note
### - Please see the `lottery.ipynb` file to see whole project in detail.
### - Please see `lottery.py` file to see the python code.
### - `649.csv` is the datasets we used in this project.
