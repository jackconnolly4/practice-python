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

numbers = [2, 4, 5, 1, 8, 9, 7, 6]
even_numbers = []
index = 0

while index < len(numbers):
  if numbers[index] % 2 == 0:
    even_numbers.append(numbers[index])
  index += 1

print(even_numbers)
