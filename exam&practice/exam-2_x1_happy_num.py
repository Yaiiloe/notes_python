def happy_num(num):
    str_num = str(num)
    sum = 0
    try:
        if eval(str_num) == 1:
            return True
        else:
            for i in str_num:
                sum = sum + eval(i)**2
            # print(sum)
            return happy_num(sum)
    except RecursionError:
        return False


def happy_num2(num):
    str_num = str(num)
    sum = 0
    try:
        if eval(str_num) == 1:
            print("True")
        else:
            for i in str_num:
                sum = sum + eval(i)**2
            # print(sum)
            return happy_num2(sum)
    except RecursionError:
        print("False")


def main():
    num = input()
    flag = happy_num(num)
    if flag is True:
        print("True")
    else:
        print("False")


main()
