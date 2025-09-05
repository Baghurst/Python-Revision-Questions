username = input("What's your name?: ")
surname = input("What's your surname?: ")
print(f"Hello {username} {surname}!")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
total = num1 + num2
print(total)

num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))
num_3 = int(input("Enter number 3: "))
num_result = num_1 + num_2 * num_3
print("Calculated result:", num_result)

pizza_slices = int(input("How many pizza slices have you started with?: "))
pizza_slices_remaining = int(input("How many do you have left?: "))
pizza_slices_eaten = pizza_slices - pizza_slices_remaining
print("There are", pizza_slices_eaten, "pizza slices were eaten.")

bill_total_ = int(input("What's the total price of the bill?: "))
total_diners_amount = int(input("How many diners were there?: "))
individual_pay_amount = bill_total_ / total_diners_amount
print("Each person must pay", individual_pay_amount, "Euros.")

day_hours = 24
day_minutes = 1440
day_seconds = 86400
random_days = int(input("Enter a random amount of days: "))
total_days_hours = day_hours * random_days
total_days_minutes = day_minutes * random_days
total_days_seconds = day_seconds * random_days
print(f"In {random_days} days there are {total_days_hours} hours, {total_days_minutes} minutes and {total_days_seconds} seconds.")

kilo = 2.204
kilo_weight = int(input("Enter a weight in Kilograms: "))
total_pounds_amount = kilo * kilo_weight
print(f"There are {total_pounds_amount} pounds in {kilo_weight} kilograms ")




