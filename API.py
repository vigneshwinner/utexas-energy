import pandas as pd
import requests

api_key = 'LwF29MF1GD8L4837wS5xijv4DhLQjm2tRMnuvd7o'
url = 'https://api.eia.gov/v2/co2-emissions/co2-emissions-aggregates/data/?api_key=LwF29MF1GD8L4837wS5xijv4DhLQjm2tRMnuvd7o'

response = requests.get(url)
data = response.json()

print(data)