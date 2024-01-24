# Start with an array of numbers and create a new array with only the numbers less than 20.
# For example, [2, 32, 80, 18, 12, 3] becomes [2, 18, 12, 3].

numbers = [2, 3, 4, 66, 78, 9, 12, 44]
small_numbers = []
index = 0

while index < len(numbers):
  number = numbers[index]
  if number < 20:
    small_numbers.append(number)
  index += 1

print(small_numbers)