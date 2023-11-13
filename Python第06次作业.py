'''
Description:

Calculate the sum of all the positive even numbers in a list.

Using Functional Programming
Using Higher-order function
Using Anonymous Functions and lambda
'''

from functools import reduce

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == "__main__":
    # answer here
    seq = filter(lambda x: x % 2 == 0 and x > 0, list)
    sum = reduce(lambda x, y: x + y, seq)
    print(sum)
