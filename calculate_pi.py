def pi_to_the_nth(n):
    if n < 0:
        raise ValueError("The number entered must be not be negative")
    if n > 16:
        print("The maximum number of digits of pi that can be calculated are 16")
    return round(sum([8 / ((4 * i + 1) * (4 * i + 3)) for i in range(10001)]), n) if n > 0 else 3

if __name__ == '__main__':
    n = int(input("Enter the number of digits of pi to be calculated (maximum 16): "))
    result = pi_to_the_nth(n)
    print(result)