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

# numbers = [5, -2, 1, -9, -7, 2, 6]
# max_product = numbers[0] * numbers[1]
# index1 = 0
# while index1 < len(numbers):
#   current_number = numbers[index1]
#   index2 = 0
#   while index2 < len(numbers):
#     if index1 != index2:
#       other_number = numbers[index2]
#       product = current_number * other_number
#       if product > max_product:
#         max_product = product
#     index2 += 1
#   index1 += 1

# print(max_product)

# Use a nested loop to compute the sum of all the numbers in an array of number pairs.
# For example, [[1, 3], [8, 9], [2, 16]] becomes 39.

# number_pairs = [[1, 3], [8, 9], [2, 16]]
# sum = 0
# index = 0

# while index < len(number_pairs):
#   numbers = number_pairs[index]
#   index2 = 0
#   while index2 < len(numbers):
#     sum += numbers[index2]
#     index2 += 1
#   index += 1

# print(sum)

# Use a nested loop with two arrays of numbers to create a new array of the sums of each combination of numbers.
# For example, [1, 2] and [6, 7, 8] becomes [7, 8, 9, 8, 9, 10].


# numbers1 = [1, 2]
# numbers2 = [6, 7, 8]
# number_sums = []
# index1 = 0

# while index1 < len(numbers1):
#   index2 = 0
#   number = numbers1[index1]
#   while index2 < len(numbers2):
#     number_sums.append(number + numbers2[index2])
#     index2 += 1
#   index1 += 1

# print(number_sums)

# Use a nested loop with an array of numbers to compute an array with every combination of products from each number.
# For example, [2, 8, 3] becomes [4, 16, 6, 16, 64, 24, 6, 24, 9].

# numbers = [2, 8, 3]
# product_combinations = []
# index1 = 0

# while index1 < len(numbers):
#   number = numbers[index1]
#   index2 = 0
#   while index2 < len(numbers):
#     product_combinations.append(number * numbers[index2])
#     index2 += 1
#   index1 += 1

# print(product_combinations)

# Use a nested loop to find the largest sum of any two different numbers within an array.
# For example, [1, 8, 3, 10] becomes 18.

# numbers = [1, 8, 3, 10]
# max_sum = numbers[0] + numbers[1]
# index1 = 0

# while index1 < len(numbers):
#   number = numbers[index1]
#   index2 = 0
#   while index2 < len(numbers):
#     if number != numbers[index2]:
#       sum = number + numbers[index2]
#       if sum > max_sum:
#         max_sum = sum
#     index2 += 1
#   index1 += 1

# print(max_sum)

# Use nested loops with an array of numbers to compute a new array containing the first two numbers (from the original array) that add up to the number 10. If there are no two numbers that add up to 10, return false.
# For example, [2, 5, 3, 1, 0, 7, 11] becomes [3, 7].

# numbers = [2, 5, 3, 1, 0, 7, 11]
# result = "false"
# index1 = 0

# while index1 < len(numbers):
#   number = numbers[index1]
#   index2 = 0
#   while index2 < len(numbers):
#     other_number = numbers[index2]
#     if number != other_number:
#       if number + other_number == 10 and result == "false":
#         result = [number, other_number]
#     index2 += 1
#   index1 += 1

# print(result)

# Use a nested loop to convert an array of string arrays into a single string.
# For example, [["a", "man"], ["a", "plan"], ["a", "canal"], ["panama"]] becomes "amanaplanacanalpanama".

# nested_words = [["a", "man"], ["a", "plan"], ["a", "canal"], ["panama"]]
# combined_word = ""
# index1 = 0

# while index1 < len(nested_words):
#   index2 = 0
#   while index2 < len(nested_words):
#     combined_word += nested_words[index1][index2]
#     index2 += 1
#   index1 += 1

# print(combined_word)
  

nested_words = [["a", "man"], ["a", "plan"], ["a", "canal"], ["panama"]]
combined_word = ""
index1 = 0
while index1 < len(nested_words):
    index2 = 0
    while index2 < len(nested_words[index1]):
        combined_word = combined_word + nested_words[index1][index2]
        index2 = index2 + 1
    index1 = index1 + 1

print(combined_word)