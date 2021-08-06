"""
Part A:
Phil's comment: the answer will be 10.
"""

"""
Part B: 
Edit this code so that it works correctly
"""

def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds 
    up to the nearest whole number
    """
    if n % 2 == 0: # must use // to get a whole number.
        n = n // 2
    else: # if n is an odd, still use //.
        n = (n + 1) // 2
    return n # must return n to pass the information to the caller.

def main():
    n = 10
    result = divide_and_round(n) # assigning a result variable to print.
    print(result) # output to the console.


if __name__ == "__main__":
    main()