def e_to_the_nth(n):
    if n < 0:
        raise ValueError("The number entered must be not be negative")
    if n > 16:
        print("The maximum number of digits of e that can be calculated are 16")
    result, fac = 0, 1
    for i in range(1, 100001):
        result += 1 / fac
        fac *= i
    return round(result, n) if n > 0 else 2

if __name__ == '__main__':
    n = int(input("Enter the number of digits of e to be calculated (maximum 16): "))
    result = e_to_the_nth(n)
    print(result)