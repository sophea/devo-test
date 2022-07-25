#!/usr/bin/env python
#
# Create a function in python that can indicate if each number from a provided list of numbers, is a perfect, abundant, or defective number.
# • A perfect number is one that is equal to the sum of its positive proper divisors, excluding itself. For example 6 = 1+2+3
# • An abundant number is one in which the sum of the proper divisors is greater than the number.
# • A defective number is one in which the sum of the proper divisors is less than the number.
# Please use Python 3.5 or higher. The use of external libraries that obtain number classification is not permitted
#

import sys

# get sum value of divisors
def get_sum(n):
    return sum([i for i in range(1, n) if n % i == 0])

### classify to identify it is perfect, abundant or deficient number
def classify(param):
    num = int(param)
    total_value = get_sum(num)
    print ('sum divisors from {} value is {}'.format(num, total_value))
    divs_sum = total_value
    if divs_sum > num:
        print('{} is abundant number'.format(num))
    elif divs_sum < num:
        print('{} is deficient number'.format(num))
    elif divs_sum == num:
        print('{} is perfect number'.format(num))

if __name__ == "__main__":
    args = sys.argv
    # args[0] = current file
    # args[1] = function name
    # args[2:] = function args : (*unpacked)
    globals()[args[1]](*args[2:])




