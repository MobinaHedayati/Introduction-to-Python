num = int(input("Enter a number: "))
prime = True
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            prime = False
            break

if prime:
    print("True")
else:
    print(prime)
