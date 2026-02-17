# variables are used to store data in a program

apple=10
print(apple)
# o/p: 10

# data types (4 types)
# int, float, string, boolean 

#########################################################################

# operators
# arithmetic operators (+, -, *, /, %)

# qus-1 (age calculator)
birth_year=2005
current_year=2026
age=current_year-birth_year
print("age=",age)
# o/p: 21

# qus-2 (total amount calculator)
current_age=21
max_age=74
amount_per_day=10
remaining_years=max_age-current_age
total_amount=remaining_years*365*amount_per_day
print("total_amount=",total_amount,"at the year of=",remaining_years)
# o/p: 193450

# qus-3 (total water calculator)
current_age=21
max_age=74
water_per_day=5
remaining_years=max_age-current_age
total_water=remaining_years*365*water_per_day
print("total_water=",total_water,"at the year of=",remaining_years)
#o/p:96725

# qus-4 (total cost calculator)
total_km=500
car_mileage=20
cast_per_litre=102
total_litre=total_km/car_mileage
total_cost=total_litre*cast_per_litre
print("total_cost=",total_cost)
# o/p: 2550.0

# qus-5 (monthly usage calculator)
daily_usage=2
no_of_days=30
monthly_usage=daily_usage*no_of_days
print("monthly_usage=",monthly_usage)
# o/p: 60

# qus-6 (total days calculator)
age=21
days=age*365
print("how many days=",days)
# o/p: 7665

# qus-7 (discount calculator)
og_price=1000
discount=10
decimal=discount/100
discount_amount=og_price*decimal
final_price=og_price-discount_amount
print("final_price=",final_price)
# o/p: 900.0 

#################################################################

# ifelse statements
# qus-1 (greater than, less than, equal to)
x=int(input("enter a number: "))
y=int(input("enter a number: "))
if(x==y):
    print("x and y are equal")
elif(x>y):
    print("x is greater than y")
else:
    print("x is less than y")
# o/p: (depends on user input)


# qus-2 (vowel or consonant)
x=(input("enter a word: "))
if(x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):
    print("x is a vowel")
else:
    print("x is a consonant")
# o/p: (depends on user input) 


# qus-3 (grade calculator) 
x=int(input("enter a mark: "))
if(x==100):
    print("grade O")
elif(x>=90 and x<=99):
    print("grade A") 
elif(x>=80 and x<90):
    print("grade B")
elif(x>=70 and x<80):
    print("grade C")
elif(x>=60 and x<70):
    print("grade D")
elif(x>=50 and x<60):
    print("grade E")
else:
    print("Fail")
# o/p: (depends on user input) 

x=int(input("enter the total cost=:"))
y=int(input("enter the sold cost=:"))
profit=y-x
loss=x-y
if(x>y):
    print("loss=",loss)
elif(x<y):
    print("profit=",profit)
else:
    print("no profit, no loss") 


