def fib(n):
    if n < 1:
        print("Uncorrect number:1 n > 1"); return ValueError
    
    counts = [0, 1]

    while len(counts) < n and n > 1:
        counts += [counts[-1] + counts[-2]]
    for i, count in enumerate(counts):
        if i >= n:
            break
        print(count)


print("Hello, World!")

n = int(input("Input n: ")); fib(n)