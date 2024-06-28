import timeit

# Traditional method to find GCD
def gcd_steins(a, b):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a

    if a % 2 == 0:
        if b % 2 == 1:
            return gcd_steins(a >> 1, b)
        else:
            return gcd_steins(a >> 1, b >> 1) << 1
    if b % 2 == 0:
        return gcd_steins(a, b >> 1)

    if a > b:
        return gcd_steins((a - b) >> 1, b)
    return gcd_steins((b - a) >> 1, a)

# Euclidean method to find GCD
def gcd_euclidean(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def main():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))

    # Measure time for traditional method
    traditional_time = timeit.timeit(lambda: gcd_steins(a, b), number=10000)
    gcd_traditional_result = gcd_steins(a, b)

    # Measure time for Euclidean method
    euclidean_time = timeit.timeit(lambda: gcd_euclidean(a, b), number=10000)
    gcd_euclidean_result = gcd_euclidean(a, b)

    print(f"Traditional GCD of {a} and {b} is {gcd_traditional_result}")
    print(f"Euclidean GCD of {a} and {b} is {gcd_euclidean_result}")

    print("Time taken for steins method:", traditional_time)
    print("Time taken for Euclidean method:", euclidean_time)
    print("Time difference:", abs(traditional_time - euclidean_time))

if __name__ == "__main__":
    main()
