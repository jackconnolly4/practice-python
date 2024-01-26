# Start with an array of numbers and create a new array with only the numbers less than 20.
# For example, [2, 32, 80, 18, 12, 3] becomes [2, 18, 12, 3].

# numbers = [2, 3, 4, 66, 78, 9, 12, 44]
# small_numbers = []
# index = 0

# while index < len(numbers):
#   number = numbers[index]
#   if number < 20:
#     small_numbers.append(number)
#   index += 1

# print(small_numbers)

# Start with an array of strings and create a new array with only the strings that start with the letter "w".
# For example, ["winner", "winner", "chicken", "dinner"] becomes ["winner", "winner"].

# words = ["ween", "ween", "primus", "weezer"]
# w_words = []
# index = 0

# while index < len(words):
#   letter = words[index][0]
#   if letter == "w":
#     w_words.append(words[index])
#   index += 1

# print(w_words)

# Start with an array of hashes and create a new array with only the hashes with prices greater than 5 (from the :price key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}].

# products = [{"name": "The Pod", "price": 10}, {"name": "GWS", "price": 12}, {"name": "White Pepper", "price": 4} ]
# high_prices = []
# index = 0

# while index < len(products):
#   product = products[index]
#   if product["price"] > 5:
#     high_prices.append(product)
#   index += 1


# print(high_prices)

# Start with an array of numbers and create a new array with only the even numbers.
# For example, [2, 4, 5, 1, 8, 9, 7] becomes [2, 4, 8].

# numbers = [2, 4, 5, 1, 8, 9, 7, 6]
# even_numbers = []
# index = 0

# while index < len(numbers):
#   if numbers[index] % 2 == 0:
#     even_numbers.append(numbers[index])
#   index += 1

# print(even_numbers)


# Start with an array of strings and create a new array with only the strings shorter than 4 letters.
# For example, ["a", "man", "a", "plan", "a", "canal", "panama"] becomes ["a", "man", "a", "a"].

# words = ["a", "man", "a", "plan", "a", "canal", "panama", "hi", "ok"]
# short_words = []
# index = 0

# while index < len(words):
#   word = words[index]
#   if len(word) < 4:
#     short_words.append(word)
#   index += 1

# print(short_words)

# Start with an array of hashes and create a new array with only the hashes with names shorter than 6 letters (from the :name key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}, {name: "book", price: 4}].

# things = [{ "name": "chair", "price": 100 }, { "name": "pencil", "price": 1 }, { "name": "book", "price": 4 }]
# short_name_things = []
# index = 0

# while index < len(things):
#   thing = things[index]
#   if len(thing["name"]) < 6:
#     short_name_things.append(thing)
#   index += 1

# print(short_name_things)

# Start with an array of numbers and create a new array with only the numbers less than 10.
# For example, [8, 23, 0, 44, 1980, 3] becomes [8, 0, 3].

# numbers = [100, 4, 5, 6000, 100000, 1, 2]
# new_numbers = []
# index = 0

# while index < len(numbers):
#   number = numbers[index]
#   if number < 10:
#     new_numbers.append(number)
#   index += 1

# print(new_numbers)

# Start with an array of strings and create a new array with only the strings that don't start with the letter "b".
# For example, ["big", "little", "good", "bad"] becomes ["little", "good"].

# words = ["big", "little", "good", "bad"]
# words2 = []
# index = 0

# while index < len(words):
#   word = words[index]
#   if word[0] != "b":
#     words2.append(word)
#   index += 1

# print(words2)

# Start with an array of hashes and create a new array with only the hashes with prices less than 10 (from the :price key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "pencil", price: 1}, {name: "book", price: 4}].

# items = [{ "name": "chair", "price": 100 }, { "name": "pencil", "price": 1 }, { "name": "book", "price": 4 }, {"name": "ween", "price": 6}, {"name": "primus", "price": 12}]
# cheap_items = []
# index = 0

# while index < len(items):
#   if items[index]["price"] < 10:
#     cheap_items.append(items[index])
#   index += 1

# print(cheap_items)

# Start with an array of numbers and create a new array with only the odd numbers.
# For example, [2, 4, 5, 1, 8, 9, 7] becomes [5, 1, 9, 7].

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = []
index = 0

while index < len(numbers):
  if numbers[index] % 2 != 0:
    odd_numbers.append(numbers[index])
  index += 1

print(odd_numbers)