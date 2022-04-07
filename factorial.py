# Factorial using recursion.
# if tried to calcutaed factorial of very big number using recursion , error will generate "Maximum recursion depth exceeded in comparison"


def factorial(number):
    if number==1 or number==0:
        return 1
    else:
        return number*factorial(number-1)

def trailingZeroCount(number):

    # Counting Zero's of number after calculating the factorial
    """zero_count = 0
    fact = factorial(number)
    while fact%10==0:
        zero_count = zero_count+1
        fact = fact/10
    return zero_count"""

    # Counting Zero's of number without calculating the factorial , helpful for large numbers
    zero_count = 0
    i = 5
    while(number//i!=0):
        zero_count = zero_count+ int(number/i)
        i = i*5

    return zero_count   


number = int(input("Enter the number: \n"))

# Function Call
#fact_calc = factorial(number)


# print(f"Factorial of Number is {fact_calc}")
print(f"The Zero's in Number is {(trailingZeroCount(number))}")