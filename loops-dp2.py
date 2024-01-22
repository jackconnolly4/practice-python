# Start with an array of numbers and create a new array with each number times 3.
# For example, [1, 2, 3] becomes [3, 6, 9].

numbers = [1, 2, 3]
index = 0 

while index < 3:
  numbers[index] = numbers[index] * 3
  index += 1

print(numbers)

numbers = [1, 2, 3]
index = 0 
new_numbers = []

while index < 3:
  new_numbers.append(numbers[index] * 3)
  index += 1

print(new_numbers)