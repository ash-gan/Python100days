import requests

class DataManager:
    sheety_endpoint = "https://api.sheety.co"
    sheety_url = '/4166d676b55b21c519cd0267e9889bf2/flightDealsProject/prices'
    sheety_headers = {
        "Authorization": "Basic YWJoZTp3b3JraGFyZEAxMzUyNDY="
    }

    def __init__(self):
        self.sheet_new = "This is not working"
        self.sheet_data = self.get_sheety_rows_data()

    def get_sheety_rows_data(self):
        sheety_get_url = f"{self.sheety_endpoint}{self.sheety_url}"
        sheet_resp = requests.get(url=sheety_get_url)
        sheet_resp.raise_for_status()
        sheet_data = sheet_resp.json()["prices"]
        return sheet_data

    def update_iata_code(self, id, iata_code):
        sheet_put_url = f"{self.sheety_endpoint}{self.sheety_url}/{id}"
        put_body = {
                    "price": {
                        'iataCode': iata_code
                    }
                }
        sheet_put_resp = requests.put(url=sheet_put_url, json=put_body, headers=self.sheety_headers)
        sheet_put_resp.raise_for_status()
        return sheet_put_resp.text
