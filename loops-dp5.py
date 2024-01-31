# Use a nested loop to convert an array of number pairs into a single flattened array.
# For example, [[1, 3], [8, 9], [2, 16]] becomes [1, 3, 8, 9, 2, 16].

number_pairs = [[1, 3], [8, 9], [2, 16]]
flattened_numbers = []
index = 0

while index < len(number_pairs):
  index2 = 0
  numbers = number_pairs[index]
  while index2 < len(numbers):
    number = numbers[index2]
    flattened_numbers.append(number)
    index2 += 1
  index += 1

print(flattened_numbers)