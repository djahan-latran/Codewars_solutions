"""Challenge: The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8.
It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

Could you give the sum of the perimeters of all the squares in a rectangle
when there are n + 1 squares disposed in the same manner as in the drawing?

The function perimeter has for parameter n where n + 1 is the number of squares
(they are numbered from 0 to n) and returns the total perimeter of all the squares.

perimeter(5)  should return 80
perimeter(7)  should return 216
"""


# My solution

def perimeter(n):
    a = 1
    b = 1

    if n == 1:
        return 1
    else:
        fib_numbers = [a, b]

        for i in range(2, n + 1):
            c = a + b
            fib_numbers.append(c)
            a = b
            b = c

    return 4 * sum(fib_numbers)