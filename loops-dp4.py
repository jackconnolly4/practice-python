# Start with an array of numbers and compute the sum of all the numbers.
# For example, [5, 10, 8, 3] becomes 26.

# numbers = [5, 10, 8, 3]
# sum = 0
# index = 0

# while index < len(numbers):
#   sum = sum + numbers[index]
#   index += 1

# print(sum)

# Start with an array of strings and combine them all into a single string.
# For example, ["volleyball", "basketball", "badminton"] becomes "volleyballbasketballbadminton".

# words = ["ween", "boognish","brown", "stallion"]
# string = ""
# index = 0

# while index < len(words):
#   string = string + words[index]
#   index += 1

# print(string)

# Start with an array of hashes and compute the sum of the prices (from the :price key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes 105.

# items = [{ "name": "chair", "price": 100 }, { "name": "pencil", "price": 1 }, { "name": "book", "price": 4 }]
# total_price = 0
# index = 0

# while index < len(items):
#   total_price = total_price + items[index]["price"]
#   index += 1

# print(total_price)

# Start with an array of numbers and compute the the minumum number.
# For example, [5, 10, 8, 3, 9] becomes 3.

# numbers = [10, 4, 5, 6, 3, 8, 1]
# minimum = numbers[0]
# index = 0

# while index < len(numbers):
#   if numbers[index] < minimum:
#     minimum = numbers[index]
#   index += 1 

# print(minimum)

# Start with an array of strings and compute the total length of all the strings.
# For example, ["volleyball", "basketball", "badminton"] becomes 29.

words = ["ween", "boognish","brown", "stallion"]
string = ""
index = 0

while index < len(words):
  string = string + words[index]
  index += 1

print(len(string))