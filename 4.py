def check_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def all_prime():
    for n in range(1, 201):
        if check_prime(n):
            print(f"{n} is a prime number.")
        else:
            print(f"{n} is not a prime number.")

all_prime()
