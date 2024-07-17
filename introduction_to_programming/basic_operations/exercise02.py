n = 4096
while n > 0:
    print(n % 10)
    n = (n - (n % 10)) // 10
