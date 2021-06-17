from datetime import datetime

current_date_and_time = datetime.now()

weekday = current_date_and_time.isoweekday()

# weekday = 1

if weekday == 2 or weekday == 4:
    discount_day = True
else:
    discount_day = False

initial_total = float(input('Enter your subtotal.\n'))

if initial_total >= 50:
    if discount_day == True:
        pre_tax = initial_total * 0.9
        print(f'There is a discount today, and you meet the criteria.  Your total has been reduced by 10% to {round(pre_tax, 2)}.')
    else:
        pre_tax = initial_total
else:
    pre_tax = initial_total

tax = pre_tax * 0.06

tax = round(tax, 2)

print(f'Your sales tax at 6% is {tax}.')

post_tax = round(pre_tax + tax, 2)
print(f'Your new total is {post_tax}')