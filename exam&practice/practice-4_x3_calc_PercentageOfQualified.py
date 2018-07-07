total, ok = 0, 0
standard = input()
data = input()
while data != "":
    total += 1
    if data >= standard:
        ok += 1
    data = input()
if total == 0:                 # when there is one input num("standard"),should be judged by variable "total" not "ok"
    print("合格率为100.00%")
else:
    print("合格率为{:.2%}".format(ok/total))
