# CodeAlpha Stock Tracker

A simple stock portfolio calculator written in Python, built as part of my CodeAlpha Python internship.

## About
The user enters stock names and quantities. Prices come from a hardcoded dictionary, and the program calculates the value of each holding and the total investment. The result can optionally be saved to a text file.

## Features
- Hardcoded dictionary of stock prices (AAPL, TSLA, GOOGL, MSFT, AMZN)
- Add as many stocks as you like, type `done` to finish
- Validates stock names and quantities
- Combines quantities if the same stock is entered twice
- Displays value per stock and total investment
- Optional save to `investment.txt`

## Concepts Used
Dictionary, input/output, basic arithmetic, file handling

## How to Run
Make sure Python 3 is installed, then run:

```
python stock_tracker.py
```

## Sample Output
```
Enter stock name: aapl
Enter quantity: 10
Enter stock name: tsla
Enter quantity: 5
Enter stock name: done

--- Your Investment ---
AAPL - 10 x 180 = 1800
TSLA - 5 x 250 = 1250
-----------------------
Total investment: 3050
```

## Author
Your Name - Python Intern at CodeAlpha
