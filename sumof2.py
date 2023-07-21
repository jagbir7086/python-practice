def SUM(x, n):
    total = 1
    for i in range(1, n + 1):
        total = total + ((x**i)/i)
    return total
 
# Driver Code
x = 2
n = 5
s = SUM(x, n)
print(round(s, 2))