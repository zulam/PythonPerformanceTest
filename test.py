#performance test

import cbpro   
import time
import requests
import time

orig_prod = {}
run = True
ctr = 0
lim = 10000
message = ''

try:
    client = cbpro.PublicClient()
    orig_prod = client.get_products()
except Exception as e:
    print(e)

start = time.time()
while ctr < lim:
    orig_ids = []
    new_ids_dashless = []
    for product in orig_prod:
        try:
            if product['quote_currency'] == 'USD':
                orig_ids.append(product['id'])
        except Exception as e:
            print(e)

    for item in orig_ids:
        try:
            message += item + '\n'
            new_ids_dashless.append(item.replace('-', ''))
        except Exception as e:
            print(e)
    ctr += 1

end = time.time()
elapsed = (end - start)
print(elapsed)