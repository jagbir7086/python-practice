
start =int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
 
# iterating each number in list
for num in range(start, end + 1):
     
    # checking condition
    if num % 2 != 0:
        print(num, end = " ")