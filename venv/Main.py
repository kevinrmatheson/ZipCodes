import pgeocode
import pandas as pd
import numpy as np
import uszipcode
import csv
from uszipcode import SearchEngine
###
ogcodes = pd.read_csv(r"C:\Users\Kevin\Downloads\ZipCodeList2020.csv")###I just grabbed the zipcodes from the wrestlers and output as a list, then paste to the same excel file.
#ogcodes = ogcodes[0:171]
### CHange it so that zip codes which dont exist spit out 99999 or something###
codes = ogcodes.iloc[:,1]###Make sure to make list of all numbers, no blanks (blanks replaced with 00000)
codes = [row.replace("'","")[0:5] for row in codes]
ogcodes = ogcodes.iloc[:,0:3]

dist = pgeocode.GeoDistance('us')
zipcodes = pd.DataFrame(columns = ['Dist'])
temp = []
for code in codes:
  temp.append(dist.query_postal_code("52001", code))

zipcodes.Dist = temp
zipcodes = 0.621371 * zipcodes.fillna(16091.835)###Makes it so that NA's give max dist 9999
zipcodes = zipcodes.round(0)
distances = zipcodes.values.tolist()
distance = sum(distances, [])


ogcodes['Distance'] = distance

###Next we find median income per zipcode
search = SearchEngine(simple_zipcode=True)
temp1 = []
for code in codes:
  zipcode = search.by_zipcode(code)
  zipcode.median_household_income
  temp1.append(zipcode.median_household_income)
temp2 = [(0 if item is None else item) for item in temp1]
ogcodes['Income'] = temp2
path = 'C:\\Users\\Kevin\\Downloads'

ogcodes.to_csv(path+'\\Updated_Zip_Codes6-22-20.csv',index = False)

