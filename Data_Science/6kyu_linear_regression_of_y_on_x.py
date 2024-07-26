"""Challenge: A linear regression line has an equation in the form Y=a+bX, where X is the explanatory variable and
Y is the dependent variable. The parameter b represents the slope of the line, while a is called the intercept
(the value of y when x=0).

Task:
The function that you have to write accepts two list/array, x and y,
representing the coordinates of the points to regress (so that, for example, the first point has coordinates
(x[0], y[0])).

Your function should return a tuple (in Python) or an array (any other language) of two elements:
a (intercept) and b (slope) in this order.

You must round your result to the first 4 decimal digits
"""


# My solution

def regression_line(x, y):
    n = len(x)

    slope_numerator = sum(i ** 2 for i in x) * sum(i for i in y) - sum(i for i in x) * sum(i * j for i, j in zip(x, y))
    slope_denominator = n * sum(i ** 2 for i in x) - sum(i for i in x) ** 2

    intercept_numerator = n * sum(i * j for i, j in zip(x, y)) - sum(i for i in x) * sum(i for i in y)
    intercept_denominator = n * sum(i ** 2 for i in x) - sum(i for i in x) ** 2

    slope = round(slope_numerator / slope_denominator, 4)
    intercept = round(intercept_numerator / intercept_denominator, 4)

    return (slope, intercept)