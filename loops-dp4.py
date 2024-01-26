# Start with an array of numbers and compute the sum of all the numbers.
# For example, [5, 10, 8, 3] becomes 26.

numbers = [5, 10, 8, 3]
sum = 0
index = 0

while index < len(numbers):
  sum = sum + numbers[index]
  index += 1

print(sum)