import  os
import requests
from  requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


load_dotenv()


class DataManager:

    def __init__(self):
        self.user = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.authorization = HTTPBasicAuth(self.user, self.password)
        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self.authorization = HTTPBasicAuth(self.user, self.password)

        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.prices_endpoint, auth=self.authorization)
        print(response.request.headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data




    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data,
                auth=self.authorization
            )
            print(response.text)

    def get_customer_emails(self):
            response = requests.get(url=self.users_endpoint, auth=self.authorization)
            response.raise_for_status()
            data = response.json()

            self.customer_data = data["users"]
            return self.customer_data





