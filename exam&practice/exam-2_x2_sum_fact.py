def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


def sum_fact(n):
    sum = 0
    for i in range(1, n + 1):
        sum += fact(i)
    return sum


def main():
    num = input()
    if num.isdigit() is True and eval(num) != 0:
        result = sum_fact(eval(num))
        print(result)
    else:
        print("输入有误，请输入正整数")


main()
