query = '''SELECT
regionID, name as regionNAME
from Region
WHERE regionID=?
'''
print(query)
