# Use a nested loop to convert an array of number pairs into a single flattened array.
# For example, [[1, 3], [8, 9], [2, 16]] becomes [1, 3, 8, 9, 2, 16].

# number_pairs = [[1, 3], [8, 9], [2, 16]]
# flattened_numbers = []
# index = 0

# while index < len(number_pairs):
#   index2 = 0
#   numbers = number_pairs[index]
#   while index2 < len(numbers):
#     number = numbers[index2]
#     flattened_numbers.append(number)
#     index2 += 1
#   index += 1

# print(flattened_numbers)

# Use a nested loop with two arrays of strings to create a new array of strings with each string combined.
# For example, ["a", "b", "c"] and ["d", "e", "f", "g"] becomes ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"].

# letters1 = ["a", "b", "c"]
# letters2 = ["d", "e", "f", "g"]
# combined_letters = []
# index1 = 0

# while index1 < len(letters1):
#   index2 = 0
#   while index2 < len(letters2):
#     combined_letters.append(letters1[index1] + letters2[index2])
#     index2 += 1
#   index1 += 1

# print(combined_letters)

# Use a nested loop with one array of strings to create a new array that contains every combination of each string with every other string in the array.
# For example, ["a", "b", "c", "d"] becomes ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"].

# letters = ["a", "b", "c", "d"]
# combined_letters = []
# index = 0

# while index < len(letters):
#   letter = letters[index]
#   index2 = 0
#   while index2 < len(letters):
#     if index2 != index:
#       combined_letters.append(letter + letters[index2])
#     index2 += 1
#   index += 1

# print(combined_letters)


# Use a nested loop to find the largest product of any two different numbers within a given array.
# For example, [5, -2, 1, -9, -7, 2, 6] becomes 63.

numbers = [5, -2, 1, -9, -7, 2, 6]
max_product = numbers[0] * numbers[1]
index1 = 0
while index1 < len(numbers):
  current_number = numbers[index1]
  index2 = 0
  while index2 < len(numbers):
    if index1 != index2:
      other_number = numbers[index2]
      product = current_number * other_number
      if product > max_product:
        max_product = product
    index2 += 1
  index1 += 1

print(max_product)