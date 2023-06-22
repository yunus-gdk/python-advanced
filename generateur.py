def custom_range(n):
    for i in range(1, n + 1):
        yield i

generateur = custom_range(10)
for i in generateur:
    print(i)

