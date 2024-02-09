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

items = [{ "id": 1, "color": "blue", "price": 32 }, { "id": 2, "color": "red", "price": 12 }]
items_hash = {}
index = 0
while index < len(items):
  items_hash[items[index]["id"]] = items[index]
  index += 1

print(items_hash)