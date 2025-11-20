string = input("Please enter a word.")
charater = input("Please enter a character.")

i=0
count=0
while (i<len(string)):
    if(string[i] == charater):
        count += 1
    i += 1
print("The number of times",charater,"has occured is", count)