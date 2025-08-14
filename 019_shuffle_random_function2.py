import random

# list with Indian city names
cities = ['delhi', 'mumbai', 
          'bangalore', 'chennai', 'Kolkata',
          'hyderabad', 'pune', 'jaipur',
            'ahmedabad', 'surat', 'lucknow']

random.shuffle(cities)
print("First shuffle:", cities)
print()

random.shuffle(cities)
print("Second shuffle:", cities)
