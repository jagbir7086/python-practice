salary = float(input("Enter your salary: "))
HRA = salary*10/100
DA = salary*5/100
PF = salary*3/100
if salary < 100000:
   In_hand = salary - (HRA+DA+PF)
    print(In_hand)
elif 500000 < salary < 1000000:
    In_hand = float(salary - (HRA+DA+PF+salary*10/100))
    print(In_hand)
elif 1100000 <= salary < 2000000:
    In_hand = float(salary - (HRA+DA+PF+salary*20/100))
    print(In_hand)
else:
    In_hand = float(salary - (HRA+DA+PF+salary*30/100))
    print(In_hand)