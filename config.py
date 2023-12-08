
import json

with open('set.json', 'r') as file:
    content = json.load(file)

print(content['mail']['url'])
