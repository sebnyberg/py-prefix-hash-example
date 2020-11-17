import struct

import mmh3

# Apple is a two-way hash
# The goal is to be able to derive the apple ID from the fruit ID
APPLE_TYPE = 1
APPLE_TYPE_PREFIX = struct.pack(">B", APPLE_TYPE)

# Orange is a one-way hash
ORANGE_TYPE = 2
ORANGE_TYPE_PREFIX = struct.pack(">B", ORANGE_TYPE)

## Create a fruit ID from an apple
apple_id = "golden yellow"
apple_fruit_id = APPLE_TYPE_PREFIX + apple_id.encode("utf-8")

## Create a fruit ID from an orange
orange_size = "10"
orange_age = "55 days"
orange_hash = mmh3.hash_bytes(orange_size+orange_age)
orange_fruit_id = ORANGE_TYPE_PREFIX + orange_hash

## Read ID
def parse_fruit_id(fruit_id):
    prefix = struct.unpack(">B", fruit_id[:1])[0]
    if prefix == APPLE_TYPE:
        return prefix, fruit_id[1:].decode("utf-8")
    
    return prefix, fruit_id[1:].hex()

def print_fruit_id(fruit_id):
  fruit_type, id = parse_fruit_id(fruit_id)
  if fruit_type == APPLE_TYPE:
    print("The fruit is an apple!")
  else:
    print("The fruit is an orange!")
  print(f"It's id is.... {id}")

print_fruit_id(apple_fruit_id)
print_fruit_id(orange_fruit_id)