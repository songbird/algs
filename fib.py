import sys

def slow_fibonacci(number):
    """Computes a given fibonacci number recursively.

    Very slow algorithm. Duplicates a lot of operations. 

    Args:
        number (int): Which fibonacci number to compute.

    Return:
        int: The "number"th number F(n) in the fibonacci sequence where 
            F(n) = F(n-1) + F(n-2) for all n > 1.
                 = n               for all n <= 1.
            
    """
    if number <= 1:
        return number
    else:
        return slow_fibonacci(number - 1) + slow_fibonacci(number - 2)

def fast_fibonacci(number):
    """Compute a number in the fibonacci sequence iteratively.
    
    Computes each number in the fibonacci sequence iteratively and stores
    each number in a list. The next fibonacci number is the sum of the last
    element and the second-to-last element in the list. This is much faster than
    the recursive solution above.

    Args:
        number (int): Which fibonacci number to compute.

    Return:
        int: The "number"th number F(n) in the fibonacci sequence where 
            F(n) = F(n-1) + F(n-2) for all n > 1.
                 = n               for all n <= 1.
    """
    if number < 2:
        return number
    arr = [0,1] 
    for index in range(2, number + 1):
        next_fib = arr[index - 1] + arr[index - 2]
        arr.append(next_fib)
    return arr[-1]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('Missing argument')
    num = int(sys.argv[1])
    print(slow_fibonacci(num))
    print(fast_fibonacci(num))


