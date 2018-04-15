import time
scale = 50
print("------执行开始------")
start = time.clock()
for i in range(scale + 1):
    a = "*" * i
    b = "." * (scale - i)
    c = (i /scale)*100
    t = time.clock() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}".format(c,a,b,t),end = "")
    time.sleep(0.05)
print("\n------执行结束------")