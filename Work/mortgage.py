# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

# extra_start = 1
# extra_end = 12
# extra_pay = 1000

# month = 1

# 1.8, 1.9
# while principal > 0:
#     if extra_start < extra_end + 1:
#         principal = principal * (1+rate/12) - payment - extra_pay
#         extra_start = extra_start + 1
#         total_paid = total_paid + payment + extra_pay
#     else:    
#         principal = principal * (1+rate/12) - payment
#         total_paid = total_paid + payment

# print('Total paid', total_paid)

# 1.10

# extra_start = 61
# extra_end = 108
# extra_pay = 1000


# while principal > 0:
#     if extra_start < extra_end + 1:
#         principal = principal * (1+rate/12) - payment - extra_pay
#         extra_start = extra_start + 1
#         total_paid = total_paid + payment + extra_pay
#     else:    
#         principal = principal * (1+rate/12) - payment
#         total_paid = total_paid + payment

# print('Total paid', total_paid)


# 1.17

extra_start = 61
extra_end = 108
extra_pay = 1000


while principal > 0:
    if extra_start < extra_end + 1:
        principal = principal * (1+rate/12) - payment - extra_pay
        extra_start = extra_start + 1
        total_paid = total_paid + payment + extra_pay
    else:    
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

print(f'Total paid {total_paid}')