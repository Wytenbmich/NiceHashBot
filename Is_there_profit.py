import nicehash
import ProfitCal
import time

# Production - https://www.nicehash.com
host = 'https://api2.nicehash.com'
organisation_id = 'Removed'
key = 'Removed'
secret = 'Removed'

cur_time = 0
# Create private api object
private_api = nicehash.private_api(host, organisation_id, key, secret, True)


# Create public api object
public_api = nicehash.public_api(host, True)

# Get all algorithms
algorithms = public_api.get_algorithms()

# Get my active hashpower orders

#num_Orders = len(my_top_active_qubit_eu_orders["list"])

#Finds active orders
def get_my_QUBIT_active_orders_not_complete():
	active_orders = []	
	my_top_active_qubit_eu_orders = private_api.get_my_active_orders('QUBIT', 'EU', 10)
	my_top_active_qubit_us_orders = private_api.get_my_active_orders('QUBIT', 'USA', 10)

	for i in my_top_active_qubit_eu_orders["list"]:
		if i["status"]["code"] == "ACTIVE":
			active_orders.append(i)
	for i in my_top_active_qubit_us_orders["list"]:
		if i["status"]["code"] == "ACTIVE":
			active_orders.append(i)
	return active_orders

def get_my_EQUIHASH_active_orders_not_complete():
	active_orders = []	
	my_top_active_equihash_us_orders = private_api.get_my_active_orders('EQUIHASH', 'EU', 10)
	for i in my_top_active_equihash_us_orders["list"]:
		if i["status"]["code"] == "ACTIVE":
			active_orders.append(i)
	return active_orders

#Gets active orders in a list
eq_orders = get_my_EQUIHASH_active_orders_not_complete()

#Checks the profit of the Qubit/Zen algorithm
Qubit_profit = float(ProfitCal.findProfit())
zen_Profit = float(ProfitCal.findProfitZEN())

print("Current Qubbit profit:" + str(Qubit_profit))
print("Current ZenCash:" + str(zen_Profit))

#Checks orders profitability and changes the order limit
def lets_profit(request_orders):
	Qubit_profit = float(ProfitCal.findProfit())
	print("Current Qubbit profit:" + str(Qubit_profit))
	order_id = 0
	for i in request_orders:
		order_id = order_id + 1
		Working_profit = (Qubit_profit - float(i['price']))		
		print("----------------------")
		print("----------------------")
		print("----------------------")
		print(str(order_id) + ":" + i["price"] + " Limit: " + i['limit'] + " Speed: " + i['acceptedCurrentSpeed'] + " Profit: " + str(Working_profit))
		print("----------------------")
		print("----------------------")
		print("----------------------")

		if i["price"] == '0.0037':
			if Qubit_profit < 0.0037:
				set_limit_order = private_api.set_limit_hashpower_order(i['id'], 0.1, 'QUBIT', algorithms)
			else:
				set_limit_order = private_api.set_limit_hashpower_order(i['id'], 1, 'QUBIT', algorithms)

		if i["price"] == '0.0049':
			if Qubit_profit < 0.0052:
				set_limit_order = private_api.set_limit_hashpower_order(i['id'], 0.1, 'QUBIT', algorithms)
			else:
				set_limit_order = private_api.set_limit_hashpower_order(i['id'], 1, 'QUBIT', algorithms)
		
		if i["price"] == '0.0042':
			if Qubit_profit < 0.0044:
				set_limit_order = private_api.set_limit_hashpower_order(i['id'], 0.1, 'QUBIT', algorithms)
			else:
				set_limit_order = private_api.set_limit_hashpower_order(i['id'], 1, 'QUBIT', algorithms)

		if i["price"] == '0.0041':
			if Qubit_profit < 0.0043:
				set_limit_order = private_api.set_limit_hashpower_order(i['id'], 0.1, 'QUBIT', algorithms)
			else:
				set_limit_order = private_api.set_limit_hashpower_order(i['id'], 1, 'QUBIT', algorithms)

def lets_profit_EQUIHASH(request_orders):
	zen_Profit = float(ProfitCal.findProfitZEN())
	print("Current ZenCash profit:" + str(zen_Profit))
	order_id = 0 
	for i in request_orders:
		order_id = order_id + 1
		Working_profit = (zen_Profit - float(i['price']))
		print("----------------------")
		print("----------------------")
		print(str(order_id) + ":" + i["price"] + " Limit: " + i['limit'] + " Speed: " + i['acceptedCurrentSpeed'] + " Profit: " + str(Working_profit))
		print("----------------------")
		print("----------------------")

		#When orders are profitable raises order limit otherwise minimum
		if float(i["price"]) > zen_Profit:
			set_limit_order = private_api.set_limit_hashpower_order(i['id'], 0.1, 'EQUIHASH', algorithms)
		else:
			set_limit_order = private_api.set_limit_hashpower_order(i['id'], 7.9, 'EQUIHASH', algorithms)


#Repeats until stopped

while True:
	try:
		#orders = get_my_QUBIT_active_orders_not_complete()
		eq_orders = get_my_EQUIHASH_active_orders_not_complete()
		#lets_profit(orders)
		lets_profit_EQUIHASH(eq_orders)
		print("Waiting 10 seconds.......")
		time.sleep(10)
		continue
		#cur_time = cur_time + 30
	except:
		print("Connection refused by the server..")
		print("Let me sleep for 30 seconds")
		print("ZZzzzz...")
		time.sleep(30)
		print("Was a nice sleep, now let me continue...")
		#cur_time = cur_time + 30
		continue
