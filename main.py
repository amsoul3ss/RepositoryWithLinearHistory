def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print("Hello, World!")

n = int(input("Input n: "))
print(f"Result fib({n}) = {fib(n)}")