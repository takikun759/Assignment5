result = " Count of number(that is odd and divisible by 3) is "

n = 0

for i in range(1,31):

    if i%3 == 0 and not(i%2 == 0):
        n += 1
        
print(result,n)