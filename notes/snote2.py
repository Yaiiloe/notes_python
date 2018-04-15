def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

count = 0
def hanoi(n,src,dst,mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(n,src,dst))
        count += 1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hanoi(n-1,mid,dst,src)


#print(factorial(50))
print(fibonacci(11))
hanoi(3,'A','C','B')
print(count)