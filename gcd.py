import sys

def slow_gcd(num1, num2):
    """Uses a slow iterative approach to computing greatest common divisor.

    Args:
        num1 (int): First integer.
        num2 (int): Second integer.

    Returns:
        int: The greatest common divisor of two numbers.
    """
    best = 0
    for answer in range(1, num1 + num2):
        if num1 % answer == 0 and num2 % answer == 0:
            best = answer
    return best

def euclidian_gcd(num1, num2):
    """Uses the euclidian algorithm to compute greatest common divisor.
    
    Proof:
    Let a' be the remainder when a is divided by b, then
        gcd(a, b) = gcd(a', b) = gcd(b, a')

    a = a' + bq for some q
    d divides a and b if and only if it divides both a' and b

    Args:
        num1 (int): First integer.
        num2 (int): Second integer.

    Returns:
        int: The greatest common divisor of two numbers.
    """
    if num2 == 0:
        return num1
    
    num1_prime = num1 % num2
    return euclidian_gcd(num2, num1_prime)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        raise Exception('Missing argument')

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    print(slow_gcd(num1, num2))
    print(euclidian_gcd(num1, num2))

