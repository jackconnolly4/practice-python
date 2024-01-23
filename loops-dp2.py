# # Start with an array of numbers and create a new array with each number times 3.
# # For example, [1, 2, 3] becomes [3, 6, 9].

# numbers = [1, 2, 3]
# index = 0 

# while index < 3:
#   numbers[index] = numbers[index] * 3
#   index += 1

# print(numbers)

######## or

# numbers = [1, 2, 3]
# index = 0 
# new_numbers = []

# while index < 3:
#   new_numbers.append(numbers[index] * 3)
#   index += 1

# print(new_numbers)

# Start with an array of strings and create a new array with each string upcased.
# For example, ["hello", "goodbye"] becomes ["HELLO", "GOODBYE"].

# words = ["ween", "primus"]
# index = 0
# new_words = []

# while index < 2:
#   new_words.append(words[index].upper())
#   index += 1

# print(new_words)

# Start with an array of hashes and create a new array of string values from each hash's :name key.
# For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes ["Alice", "Blane"].

# hashes = [{"name": "Jack", "age": 27}, {"name": "Harold", "age": 42}]
# strings = []
# index = 0

# while index < 2:
#   strings.append(hashes[index]["name"])
#   index += 1

# print(strings)

# Start with an array of numbers and create a new array with each number plus 7.
# For example, [1, 2, 3] becomes [8, 9, 10].

numbers = [1, 2, 3]
new_numbers = []
index = 0

while index < len(numbers):
  new_numbers += [numbers[index] + 7]
  index += 1

print(new_numbers)