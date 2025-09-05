
# Mean = average value.
# Median = middle value (after sorting).
# Frequency = how many times each number appears.
# Mode = most common number(s).
numbers = []
while True:
    value = input("Enter a number (or 'q' to quit): ")
    if value.lower() == 'q':
        break
    else:
        numbers.append(float(value)) #Adding the user input to the list "numbers"
if len(numbers) == 0:
    print("No numbers were entered.")
mean = sum(numbers) / len(numbers) #Diving the sum of "numbers" by the lenght of "numbers" to get the average
numbers.sort() #Sorting the numbers in order from smallest to largest
n = len(numbers)
    
#I'm a bit stuck, not sure how to get frequency



print("Numbers entered:", numbers)
print("Mean:", mean)
print("Median:", )
print("Frequency:", )
print("Mode:", )


