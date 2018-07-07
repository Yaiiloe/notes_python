def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    sum, idx = 0, 0
    result = []
    n = eval(input())
    while fibonacci(idx) <= n:
        result.append(fibonacci(idx))
        idx += 1
    for ls in result:
        sum += ls
    ave = round(sum / idx)
    result.append(sum)
    result.append(ave)

    str_result = list(map(str, result))
    print(", ".join(str_result))


main()
