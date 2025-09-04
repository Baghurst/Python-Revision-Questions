numbers = []
while True:
    value = input("Enter a number (or 'q' to quit): ")
    if value.lower() == 'q':
        break
    else:
        numbers.append(float(value))
if len(numbers) == 0:
    print("No numbers were entered.")
mean = sum(numbers) / len(numbers)
numbers.sort()
n = len(numbers)
if n % 2 == 0:  
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
else:           
    median = numbers[n//2]

#I'm a bit stuck, not sure how to get frequency

print("Numbers entered:", numbers)
print("Mean:", mean)
print("Median:", median)
print("Frequency:", )

print("Mode:", )
