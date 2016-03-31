import sys
import fib


def fib_mod(fib_num, mod):
    period_length = find_pisano_period(fib_num, mod)
    fn = fib_num % period_length
    return fast_fibonacci(fn) % mod

def find_pisano_period(fib_num, mod):
    prev_mod = None
    for i in range(2, fib_num):
        ith_seq = fast_fibonacci(i) % mod
        if ith_seq == 1 and prev_mod == 0:
            return i-1
        prev_mod = ith_seq
    
def fast_fibonacci(number):
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
    #Find F(n) % m
    n = int(sys.argv[1])
    m = int(sys.argv[2]) 
    print(fib_mod(n, m))


