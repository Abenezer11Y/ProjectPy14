min = int(input("Enter an lower range."))
max = int(input("Enter an upper range."))

print("Prime numbers between",min,"and",max,"are:")

for num in range(min,max + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)