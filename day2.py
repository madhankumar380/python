# # fees calculator
# stype = input("Enter Student Type (MSDS, MSH, MGSD): ").strip().lower()
# if stype not in ["msds", "msh", "mgsd"]:
#     print("Invalid student type entered. Please enter MSDS, MSH, or MGSD.")
#     exit()
# while True:
#     try:
#         tuition = float(input("Enter Tuition Fee: "))
#         break
#     except:
#         print("Invalid input! Please enter a numeric value.")
# if stype == "msds":
#     while True:
#         try:
#             college = float(input("Enter College Fee: "))
#             break
#         except:
#             print("Invalid input! Please enter a numeric value.")
#     hostel = 0
# elif stype in ["msh", "mgsd"]:
#     while True:
#         try:
#             hostel = float(input("Enter Hostel Fee: "))
#             break
#         except:
#             print("Invalid input! Please enter a numeric value.")
#     college = 0
# if stype == "msds":
#     total = tuition + college
# elif stype == "msh":
#     total = tuition + hostel
# else: 
#     total = 1.5 * tuition + hostel
# print(f"Total Fee for {stype.upper()}: {total}")
# # result:Enter Student Type (MSDS, MSH, MGSD): msds
# #        Enter Tuition Fee: 6000
# #        Enter College Fee: 7000
# #        Total Fee for MSDS: 13000.0


# # account balance
# account_balance=50000
# withdrawl_amount=int(input('enter the withdrawl amount='))
# if (withdrawl_amount>account_balance):
#     print('insufficiant fund')
# elif (withdrawl_amount>10000):
#     print('limit exceeded')
# else :
#     print('allow withdrawl')
# # result
# # enter the account balance=5000
# # enter the withdrawl amount=5500
# # insufficiant fund

# # atm withdrawl
# account_pin=9486
# x=int(input('enter the pin='))
# if(x==account_pin):
#     print('pin is correct')
#     withdrawl_amount=int(input('enter the withdrawl amount='))
#     if (withdrawl_amount>account_balance):
#         print('insufficiant fund')
#     elif (withdrawl_amount>10000):
#         print('limit exceeded')
#     elif (withdrawl_amount<=0):
#         print('invalid amount')
#     else :
#         print('allow withdrawl')
#         balance_amount=account_balance-withdrawl_amount
#         print('the balance amount is=',balance_amount)
# else:
#     print('wrong pin')
# # result
# # enter the pin=9486
# # pin is correct
# # enter the withdrawl amount=4000
# # allow withdrawl
# # the balance amount is=46000

# # booking tickets
# age=int(input('enter your age='))
# show=input('enter the show time(mng,eve)=')
# child=150
# adult=250
# senior=200
# if (age<=4):
#     print('free entry')
# elif (age>=5) or (age<=16):
#     if (show == "mng"):
#         child_mng=0.5*child
#         print('the ticket price is=',child_mng)
#     else:
#         print('the ticket price is=',child)

# elif (age>=17) or (age<=59):
#     if (show == "mng"):
#         adult_mng=0.5*adult
#         print('the ticket price is=',adult_mng)
#     else:
#         print('the ticket price is=',adult)
# else:
#     if (show == "mng"):
#         senior_mng=0.5*senior
#         print('the ticket price is=',senior_mng)
#     else:
#         print('the ticket price is=',senior)
# # result
# # enter your age=20
# # enter the show time(mng,eve)=eve
# # the ticket price is= 250

# # loop functions

# # qus-1 (odd numbers)
# odd_sum=0
# print("odd numbers upto 100:")
# for i in range(1,100,2):
#     print(i)
#     odd_sum=odd_sum+i
# print('the sum of odd numbers upto 100 is=',odd_sum)
# # o/p: the sum of odd numbers upto 100 is= 2500


# # qus-2 (even numbers)
# even_sum=0
# print("even numbers upto 100:")
# for i in range(0,100,2):
#     print(i)
#     even_sum=even_sum+i
# print('the sum of even numbers upto 100 is=',even_sum)
# # o/p: the sum of even numbers upto 100 is= 2450


# # qus-3 (multiples of 5)
# for i in range(5,55,5):
#     print(i)
# # o/p: 5 10 15 20 25 30 35 40 45 50


# # qus-4 (mark calculator)
# tamil=int(input('enter the tamil mark:'))
# english=int(input('enter the english mark:'))
# maths=int(input('enter the maths mark:'))
# science=int(input('enter the science mark:'))
# social=int(input('enter the social mark:'))
# total_marks=tamil+english+maths+science+social
# print('the total marks is=',total_marks)
# average_marks=total_marks/5
# print('the average marks is=',average_marks)
# # o/p: the total marks is= 450
#     #  the average marks is= 90


# # qus-5 (star pattern)
# for i in range(1,6):
#     print('*'*i)

# # qus-6 (reverse star pattern)
# for i in range(5,0,-1):
#     print('*'*i)


# # while loop functions

# # qus-1 (odd numbers)
# odd_sum=0
# i=1
# print("odd numbers upto 100:")
# while i<100:
#     print(i)
#     odd_sum=odd_sum+i
#     i=i+2

# # qus-2 (even numbers)
# even_sum=0
# i=2
# print("even numbers upto 100:")
# while i<=100:
#     print(i)
#     even_sum=even_sum+i
#     i=i+2


# #qus-3 (star pattern)
# i=1
# while i<=6:
#     print("*"*i)
#     i=i+1


# #qus-4 (reverse star pattern)
# i=5
# while i>0:
#     print("*"*i)
#     i=i-1


# # qus-5 (multiples of 5)
# i=5
# while i<55:
#     print(i)
#     i=i+5

# real time bus seat booking using while loop and in the finish all saets are booked and also chcek if the seat is avilable or not and also put the name of the person who booked the seat
total_seats=10
booked_seats=[]
while total_seats>0:
    seat_number=int(input('enter the seat number you want to book(1-10):'))
    if seat_number>total_seats or seat_number<=0:
        print('seat not available')
    else:
        name=input("enter your name: ")
        booked_seats.append((seat_number,name))
        print(f"seat {seat_number} booked for {name}")
        total_seats=total_seats-1

if total_seats==0:
    print("all seats are booked")