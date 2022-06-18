import requests
import json
from bs4 import BeautifulSoup

def findProfit():
	#Queries WhatToMine to get current difficulty for DGB
	url = "https://whattomine.com/coins/115.json"
	response = requests.get(url)
	cont = json.loads(response.content)
	difficulty = cont['difficulty']

	#Queries WhatToMine using difficulty params to get profit
	#Includes fees to ensure profit margin
	url = "https://whattomine.com/coins/115-dgb-qubit?utf8=%E2%9C%93&hr=1000000.0&d_enabled=true&d=" + str(difficulty) + "&p=1700.0&fee=8.0&cost=0.1&hcost=0.0&commit=Calculate"
	response = requests.get(url)
	cont = BeautifulSoup(response.content, "html.parser")
	table = cont.findAll("td", attrs={"class" : "text-right text-monospace"})
	rows = []
	for row in table:
		rows.append(row)

	#Current difficulty
	print(difficulty)

	#Row 8 contains profit
	revenue = rows[8].text
	return revenue

def findProfitZEN():
	#Queries WhatToMine to get current difficulty for ZenCash
	url = "https://whattomine.com/coins/185.json"
	response = requests.get(url)
	cont = json.loads(response.content)
	difficulty = cont['difficulty']

	#Queries WhatToMine using difficulty params to get profit
	#Includes fees to ensure profit margin
	url = "https://whattomine.com/coins/185-zen-equihash?utf8=%E2%9C%93&hr=1000000&d_enabled=true&d=" + str(difficulty) + "&p=2330.0&fee=8.0&cost=0.1&hcost=0.0&commit=Calculate"
	response = requests.get(url)
	cont = BeautifulSoup(response.content, "html.parser")
	table = cont.findAll("td", attrs={"class" : "text-right text-monospace"})
	rows = []

	for row in table:
		rows.append(row)

	#Current difficulty
	print(difficulty)
	
	revenue = rows[8].text
	return revenue