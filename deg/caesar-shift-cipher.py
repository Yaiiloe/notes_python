import os


# shift key = 3 in lowercase transformation
def encrypt():
    tempstr = input()
    for c in tempstr:
        if c == " ":
            print(c, end="")
        else:
            c = (ord(c)-97+3) % 26 + 97
            print(chr(c), end="")


# get_name() and get_filename() share the same function
def get_name(fname):
    fullname_ls = fname.split("\\")
    name_ls = fullname_ls[-1].split('.')
    return name_ls[0]


def get_filename(fname):
    filefullname = os.path.basename(fname)
    filename = filefullname.split(".")
    return filename[0]


def get_path(fname):
    parent_path = os.path.dirname(fname)
    return parent_path


def caesar_de():
    fname = input("Please input the file path:")
    key = input("Please set the key for decryption:")
    text = open(fname, "r").read()
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr((i + eval(key)) % 26 + c)] = chr(c+i)
#    print(d)
    fo = open(get_path(fname) + '\\' + get_name(fname) + '_de' + '.txt', 'w')
    for c in text:
        fo.writelines(d.get(c, c))
    print("".join([d.get(c, c) for c in text]))


def caesar_en():
    fname = input("Please input the file path:")
    key = input("Please set the key for encryption:")
    text = open(fname, "r").read()
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(c + i)] = chr((i + eval(key)) % 26 + c)
#    print(d)
    fo = open(get_path(fname) + '\\' + get_name(fname) + '_en' + '.txt', 'w')
    for c in text:
        fo.writelines(d.get(c, c))
    print("".join([d.get(c, c) for c in text]))


caesar_de()
# a = 'D:\\temp\\test.txt'
# print(get_filename(a), get_path(a))
# print(get_path(a) + '\\' + get_name(a) + '_de' + '.txt')
