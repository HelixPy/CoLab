print("Hello, type in a number and i will show you the prime factors")
num = int(input("please enter a number: "))
div = 1
while num > div:
    if num % div == 0:
        num = num / div
        print(num)
        div += 1
        continue
    if num % div > 0:
        print(f"the entry {num} is a prime number and has itself and 1 as prime factors")
        break
print ("finished")
