import json

with open('./data.json', 'r') as animals_json:
  animals = json.load(animals_json)

animal_values = []

# for animal in animals['animals']:
#     x = animal['weight']
#     y = animal['speed']
#     key = x + ';' + y
#     value = animal['name']
#     animal_values.append(key, value)

input_weight = 1000
input_speed = 20
output = 'not found'

for animal in animals['animals']:
    if animal['weight'] < input_weight + 5 and animal['weight'] > input_weight - 5:
        if animal['speed'] < input_speed + 5 and animal['speed'] > input_speed - 5:
            output = animal['name']

print(output)