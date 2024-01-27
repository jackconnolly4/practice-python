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

# words = ["ween", "boognish","brown", "stallion"]
# string = ""
# index = 0

# while index < len(words):
#   string = string + words[index]
#   index += 1

# print(len(string))

# Start with an array of hashes and find the hash with the lowest price (from the :price key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "pencil", price: 1}.

# items = [{ "name": "chair", "price": 100 }, { "name": "pencil", "price": 1 }, { "name": "book", "price": 4 }]
# cheapest_item = items[0]
# index = 0

# while index < len(items):
#   if items[index]["price"] < cheapest_item["price"]:
#     cheapest_item = items[index]
#   index += 1

# print(cheapest_item)

# Start with an array of numbers and compute product of all the numbers.
# For example, [5, 10, 8, 3] becomes 1200.

# numbers = [5, 10, 8, 23]
# product = 1
# index = 0

# while index < len(numbers):
#   product = product * numbers[index]
#   index += 1

# print(product)

# Start with an array of strings and combine them all into a single string, separated by dashes.
# For example, ["volleyball", "basketball", "badminton"] becomes "-volleyball-basketball-badminton-".

# strings = ["volleyball", "basketball", "badminton"]
# single_string = "-"
# index = 0

# while index < len(strings):
#   single_string = single_string + strings[index] + "-"
#   index += 1

# print(single_string)

#  or: 

# strings = ["volleyball", "basketball", "badminton"]
# single_string = "-"
# index = 0

# while index < len(strings):
#   string = strings[index]
#   single_string += f"{string}-"
#   index += 1

# print(single_string)

# Start with an array of hashes and find the hash with the shortest name (from the :name key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "book", price: 4}.

# items = [{ "name": "chair", "price": 100 }, { "name": "pencil", "price": 1 }, { "name": "book", "price": 4 }, {"name": "ween", "price": 6}, {"name": "primus", "price": 12}]
# shortest_name = items[0]
# index = 0

# while index < len(items):
#   name = items[index]["name"]
#   if len(name) < len(shortest_name["name"]):
#     shortest_name = items[index]
#   index += 1

# print(shortest_name)

# Start with an array of numbers and compute the maximum number.
# For example, [5, 10, 8, 3] becomes 10.

numbers = [-1, 0, 1, 4, 2, 3]
maximum = numbers[0]
index = 0

while index < len(numbers):
  if numbers[index] > maximum:
    maximum = numbers[index]
  index += 1

print(maximum)