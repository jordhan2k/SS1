# Part 1 - MCQ
# Problem 1
# 1.a  2.a  3.b  4.b,d  5.b
# Problem 2
# 1.a 2.a 3.a 4.d 5.a
#

# Problem 4
def calculate_profit():
    while True:
        try:
            total_sale = float(input('total sales (): '))
            if total_sale < 0:
                print('Invalid input! Re-input')
                continue
            else:
                break
        except ValueError:
            print('Invalid input! Re-input')
            continue
    profit = (total_sale * 23) / 100
    print('Profit: $', profit)


# Problem 5
def calculate_acre():
    while True:
        try:
            total_square_feet = float(input('Input the total square feet: '))
            if total_square_feet < 0:
                print('Invalid input! Re-input')
                continue
            else:
                break
        except ValueError:
            print('Invalid input! Re-input')
            continue
    total_acre = total_square_feet / 43560
    print('The number of acres: ', total_acre)


# Problem 6
def calculate_distance():
    speed = 70
    print('The distance the car travel in: ')
    print('+ 6 hours: ', (speed * 6), ' miles')
    print('+ 10 hours: ', (speed * 10), ' miles')
    print('+ 15 hours: ', (speed * 15), ' miles')


# Problem 7
def calculate_purchase_info():
    purchase_amount = float(input('Input the amount of purchase: '))
    state_sales_tax = purchase_amount * 0.025
    country_sales_tax = purchase_amount * 0.05
    total_sale_tax = state_sales_tax + country_sales_tax
    total_sale = purchase_amount + total_sale_tax
    print('The amount of purchase: ', purchase_amount)
    print('State sales tax: ', state_sales_tax)
    print('Country sales tax: ', country_sales_tax)
    print('Total sales tax: ', total_sale_tax)
    print('Total of the sale: ', total_sale)


# Problem 8
def calculate_mpg():
    miles_driven = float(input('Enter the number of miles driven: '))
    gallon_gas = float(input('Enter the number of gallons of gas used: '))
    mpg = miles_driven / gallon_gas
    print('MPG: ', mpg)


# problem 9
def convert_celsius_to_fahrenheit():
    celsius = float(input('Enter the number of Celsius degrees: '))
    fahrenheit = (9 / 5) * celsius + 32
    print(celsius, 'C degree is ', fahrenheit, 'F degree')



