import sys
import gcd

def lcm(num1, num2):
    
    gcd_n = gcd.euclidian_gcd(num1, num2)
    return (num1 * num2) / gcd_n


if __name__ == '__main__':

    if len(sys.argv) < 3:
        raise Exception('Missing argument')

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    print(lcm(num1, num2))

