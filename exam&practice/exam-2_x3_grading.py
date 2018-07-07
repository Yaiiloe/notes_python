def grading(n):
    if n > 100 or n < 0:
        return 1/0
    elif n >= 90:
        return 'A'
    elif n >= 80:
        return 'B'
    elif n >= 70:
        return 'C'
    elif n >= 60:
        return 'D'
    else:
        return 'E'


def main():
    try:
        num = eval(input())
        # error = 1 / (0 <= num <=100)
        result = grading(num)
    except:
        print("输入数据有误！")
    else:
        print("输入成绩属于{}级别。".format(result))
        if result in ['A', 'B', 'C', 'D']:
            print("祝贺你通过考试！")
    finally:
        print("好好学习，天天向上！")


main()
