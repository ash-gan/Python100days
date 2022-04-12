#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager

fs = FlightSearch()
dm = DataManager()

for item in dm.sheet_data:
    iata_code = fs.return_iata_code(item['city'])
    dm.update_iata_code(id=item['id'], iata_code=iata_code)

print("**********")
print(dm.sheet_data)
print("**********")

#

