minimum = 1000000000
maximum = 9999999999
printed = 0
print ("The first 25 10-digit prime numbers are:")
for num in range (minimum, maximum + 1):
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                break
    else:
        print(num)
        printed+= 1

    if printed >= 25:
        break