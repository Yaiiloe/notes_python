def brackets(n):
    ls, lt = [], []
    if n == 1:
        return ["()"]
    else:
        ls.append("()")
        while n-1 > 0:
            for item in ls:
                one_item_combination = insert(item)
                lt.extend(one_item_combination.copy())
            ls = lt.copy()
            lt.clear()
            n -= 1
        ls = list(set(ls))
        return ls


# combination for one item(string)
'using base string "()" to insert into the left or right of each character of one string'
def insert(string):
    basestr = "()"
    lt = []
    for idx in range(len(list(string)) + 1):        # total locations which can be inserted into
        temp_ls = list(string)
        temp_ls.insert(idx, basestr)
        lt.append("".join(temp_ls))                 # re-convert list to string
    lt = list(set(lt))                              # remove repetitive items
    return lt


def main():
    n = eval(input())
    result = brackets(n)
    print(result)
    print(len(result))


main()
