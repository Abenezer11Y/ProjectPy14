num = int(input("Enter a number"))
t=num
numL=0

while t>0:
    numL += 1
    t=int(t/10)
    
if numL>=4:
    numL = int(numL/2)
    chk = 0
    while num>0:
        rem = num%10
        if chk == numL:
            midone = rem
        elif chk==(numL-1):
            midtwo = rem
            num = int(num/10)
            chk += 1
    prod = midone*midtwo
    print("Products of Mid digits (" +str(midone) + " * " + str(midtwo) +") =", prod)
else:
    print("The number is not a 4 or more digit number!")