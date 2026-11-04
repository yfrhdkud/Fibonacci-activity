def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

n = int(input("Enter a number to find its fibonacci: "))
guess = int(input("Enter your guess on the answer: "))
print(f"The fibinacci sequence of {n} is {fib(n)}, your guess: {guess}")

if guess == fib(n):
    print("Your guess was correct")
else:
    print("Your guess was wrong")