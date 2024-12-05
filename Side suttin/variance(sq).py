import math

user_input = input("Enter a list of numbers to fnd their variance(separated by spaces): ")
numbers = [int(num) for num in user_input.split()]

mean_of_numbers = sum(numbers) / (len(numbers) - 1)

difference_of_numbers = [num - mean_of_numbers for num in numbers]

squared_difference_of_numbers = [num ** 2 for num in numbers]

variance = sum(squared_difference_of_numbers) / (len(numbers) - 1)

standard_deviation = math.sqrt(variance)

print(f"The variance of {numbers} is {variance} and its standard deviation is {standard_deviation}")
