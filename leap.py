years = int(input("Enter a year: "))
if years % 2 == 0 and years  %400 == 0:
    print("Leap year")
else:
   print("Not leap year")