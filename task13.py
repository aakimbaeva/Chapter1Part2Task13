num = int(input('Write a number: '))
print([i ** 2 for i in range(1, num) if i ** 2 <= num])