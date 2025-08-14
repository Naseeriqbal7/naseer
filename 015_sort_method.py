# list with Indian city names
cities = ['delhi', 'mumbai', 
          'bangalore', 'chennai', 'Kolkata',
          'hyderabad', 'pune', 'jaipur',
            'ahmedabad', 'surat', 'lucknow']

cities.sort()
print("Sorted cities:\n", cities)

print()
cities.sort(key=str.lower)
print("Sorted cities in lower case:\n", cities)

print()
cities.sort(key=str.upper, reverse=True)
print("Sorted cities in upper case in reverse order:\n", cities)

