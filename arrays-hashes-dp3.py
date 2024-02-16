# Convert an array of arrays into a hash.
# For example, [[1, 3], [8, 9], [2, 16]] becomes {1 => 3, 8 => 9, 2 => 16}.

# pairs = [[1, 3], [8, 9], [2, 16]]
# pairs_hash = {}
# index = 0
# while index < len(pairs):
#   key = pairs[index][0]
#   value = pairs[index][1]
#   pairs_hash[key] = value
#   index += 1


# print(pairs_hash)

# Convert an array of hashes into a hash using the :id key from the array's hashes as the keys in the new hash.
# For example, [{id: 1, color: "blue", price: 32}, {id: 2, color: "red", price: 12}] becomes {1 => {id: 1, color: "blue", price: 32}, 2 => {id: 2, color: "red", price: 12}}.

# items = [{ "id": 1, "color": "blue", "price": 32 }, { "id": 2, "color": "red", "price": 12 }]
# items_hash = {}
# index = 0
# while index < len(items):
#   items_hash[items[index]["id"]] = items[index]
#   index += 1

# print(items_hash)

# Convert a string into a hash with keys for each letter in the string and values for the number of times the letter appears in the string.

# word = "bookkeeper"
# letter_frequencies = {}
# index = 0
# while index < len(word):
#     letter = word[index]
#     if letter not in letter_frequencies:
#         letter_frequencies[letter] = 0
#     letter_frequencies[letter] += 1
#     index += 1

# print(letter_frequencies)

# Convert a hash into an array of arrays.
# For example, {"chair" => 100, "book" => 14} becomes [["chair", 100], ["book", 14]].

# things = {"chair": 100, "book": 14}
# name_price_pairs = []

# for name, price in things.items():
#     name_price_pairs.append([name, price])

# print(name_price_pairs)


# Convert a hash into an array of hashes using the keys from each hash as the :id key in each of the array's hashes.
# For example, {321 => {name: "Alice", age: 31}, 322 => {name: "Maria", age: 27}} becomes [{id: 321, name: "Alice", age: 31}, {id: 322, name: "Maria", age: 27}].

people = {321: {"name": "Alice", "age": 31}, 322: {"name": "Maria", "age": 27}}
people_array = []

for id, person in people.items():
    person["id"] = id
    people_array.append(person)

print(people_array)
