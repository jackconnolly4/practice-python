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

letters1 = ["a", "b", "c"]
letters2 = ["d", "e", "f", "g"]
combined_letters = []
index1 = 0

while index1 < len(letters1):
  index2 = 0
  while index2 < len(letters2):
    combined_letters.append(letters1[index1] + letters2[index2])
    index2 += 1
  index1 += 1

print(combined_letters)