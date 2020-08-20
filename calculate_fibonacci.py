def fibonacci(n):
    if n < 0:
        raise ValueError("The number entered must be not be negative")
    if n == 0:
        return [0]
    seq = [0, 1]
    for i in range(n):
        if seq[-1] == n:
            break
        seq.append(seq[-1] + seq[-2])
    return seq

if __name__ == '__main__':
    n = int(input("Enter number to calculate the fibonacci sequence: "))
    result = " ".join([str(num) for num in fibonacci(n)])
    print(result)