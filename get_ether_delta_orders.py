import requests

ether_delta_orders_api = "https://api.etherdelta.com/orders"
def get_ether_delta_order_for(contract_address,page):
  r = requests.get("{}/{}/{}".format(ether_delta_orders_api,contract_address,page))
  r_json = r.json()
  buys = r_json["buys"]
  buys_results = []
  for buy in buys:
    buys_results.append(buy)
  
  sells = r_json["sells"]
  sells_results = []
  for sell in sells:
    sells_results.append(sell)
  return buys_results,sells_results
