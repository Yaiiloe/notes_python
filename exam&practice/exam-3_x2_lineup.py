def lineup(ls):
    ls.sort(key=lambda x: x[1])
    # print(ls)
    ls.sort(key=lambda x: x[0], reverse=True)
    # print(ls)
    lt = []
    for item in ls:
        lt.insert(item[1], item)
    return lt


def main():
    ls = eval(input())
    result = lineup(ls)
    print(result)


main()
