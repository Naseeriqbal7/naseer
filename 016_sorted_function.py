# list with Indian city names
cities = ['delhi', 'mumbai', 
          'bangalore', 'chennai', 'Kolkata',
          'hyderabad', 'pune', 'jaipur',
            'ahmedabad', 'surat', 'lucknow']

new_cities = sorted(cities, key=str.lower)
print(new_cities)
