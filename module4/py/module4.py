#!/usr/bin/env python3

import json

SRC = "/home/scottdavis/eclipse-workspace/module1/cars.json"

with open(SRC) as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)
