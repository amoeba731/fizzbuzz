# add your code here

range(101)
for i in range(101):
    if i %3==0 and i %5==0:
        print("FIZZBUZZ")
    elif i %5==0:
        print("BUZZ")
    elif i %3==0:
        print ("FIZZ")
    else: print(i)
