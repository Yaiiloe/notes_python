from jieba import lcut


def get_text():
    txt = open("D:\\analysis\\threekingdoms.txt", "r", encoding='utf-8').read()
    words = lcut(txt)
    return words


def analyse_optimz():
    words = get_text()
    excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如此", "商议", "如何", "主公", "军士", "左右", "军马",
                "引兵", "次日", "大喜", "天下", "东吴", "于是", "今日", "不敢", "魏兵", "陛下", "一人", "都督", "人马",
                "不知", "汉中", "只见", "众将", "后主", "蜀兵", "上马", "大叫", "太守", "此人", "夫人", "先主", "后人",
                "背后", "城中", "天子", "一面", "何不", "大军", "忽报", "先生", "百姓", "何故", "然后", "先锋", "不如",
                "赶来", "原来", "令人", "江东", "下马", "喊声", "正是", "徐州", "忽然", "因此", "成都", "不见", "未知",
                "大败", "大事", "之后", "一军", "引军", "起兵", "军中", "接应", "进兵", "大惊", "可以", "以为", "大怒",
                "不得", "心中", "下文", "一声", "追赶"}
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        elif word == "诸葛亮" or word == "孔明曰":
            sword = "孔明"
        elif word == "关公" or word == "云长":
            sword = "关羽"
        elif word == "玄德" or word == "玄德曰":
            sword = "刘备"
        elif word == "孟德" or word == "丞相":
            sword = "曹操"
        else:
            sword = word
        counts[sword] = counts.get(sword, 0) + 1
    for word in excludes:
        del counts[word]
    return counts


def analyse_simple():
    words = get_text()
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    return counts


def main():
    schema = input("Please choose a pattern to analyse(1 -> general, 2 -> accurate):")
    if schema == '1':
        counts = analyse_simple()
    elif schema == '2':
        counts = analyse_optimz()
    else:
        counts = analyse_simple()
        print("Default pattern chosen:general")

    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(20):
        key, count = items[i]
        print("{:<10}{:>10}".format(key, count))


if __name__ == '__main__':
    main()
