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
apple_fruit_id = (APPLE_TYPE_PREFIX + apple_id.encode("utf-8")).hex()

## Create a fruit ID from an orange
orange_size = "10"
orange_age = "55 days"
orange_hash = mmh3.hash_bytes(orange_size+orange_age)
orange_fruit_id = (ORANGE_TYPE_PREFIX + orange_hash).hex()

## Read ID
def parse_fruit_id(fruit_id):
    id_bytes = bytearray.fromhex(fruit_id)
    prefix = struct.unpack(">B", id_bytes[:1])[0]
    if prefix == APPLE_TYPE:
        return prefix, id_bytes[1:].decode("utf-8")
    
    return prefix, id_bytes[1:].hex()

def print_fruit_id(fruit_id):
  fruit_type, id = parse_fruit_id(fruit_id)
  if fruit_type == APPLE_TYPE:
    print("The fruit is an apple!")
  else:
    print("The fruit is an orange!")
  print(f"Its id is.... {id}")

# Prints:
# The fruit is an apple!
# Its id is.... golden yellow
print_fruit_id(apple_fruit_id)

# Prints:
# The fruit is an orange!
# Its id is.... 5dc6384c18150b6d2ab5cf2b854d074c
print_fruit_id(orange_fruit_id)