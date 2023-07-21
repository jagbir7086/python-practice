heads = int(input("Enter the total number of heads: "))
legs = int(input("Enter the total number of legs: "))
dogs = (legs - (2 * heads)) / 2
print(dogs)
chickens = heads - dogs
print(chickens)
