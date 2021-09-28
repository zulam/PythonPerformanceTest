#comparison test

import cbpro   
import time

#original iterations
orig_ids = []
orig_prod = {}
ctr = 0
lim = 10000

while len(orig_prod) == 0: 
    try:
        client = cbpro.PublicClient()
        orig_prod = client.get_products()
    except Exception as e:
        print(e)

    for product in orig_prod:
        try:
            if product['quote_currency'] == 'USD':
                orig_ids.append(product['id'])
        except Exception as e:
            print(e)
try:
    client = cbpro.PublicClient()
    products = client.get_products()
except Exception as e:
    print(e)

start = time.time()
while ctr < lim:
    new_ids = []
    new_ids_dashless = []
    for product in products:
        try:
            if product['id'] not in orig_ids:
                if product['quote_currency'] == 'USD':
                    new_ids.append(product['id'])
        except Exception as e:
            print(e)

    message = ""
    for item in new_ids:
        message += item + '\n'
        new_ids_dashless.append(item.replace('-', ''))
    #print(ctr)
    ctr += 1

end = time.time()
print ('original iterations time: ')
print(end - start)

#set difference
orig_ids = []
ctr = 0
try:
    client = cbpro.PublicClient()
    orig_prod = client.get_products()
except Exception as e:
    print(e)

for product in orig_prod:
    try:
        if product['quote_currency'] == 'USD':
            orig_ids.append(product['id'])
    except Exception as e:
        print(e)

orig_id_set = set(orig_ids)
ctr = 0
try:
    client = cbpro.PublicClient()
    products = client.get_products()
except Exception as e:
    print(e)

start = time.time()
while ctr < lim:
    new_prods = []
    new_ids = {}
    new_ids_dashless = []
    new_prod_set = set([a['id'] for a in products if a['quote_currency'] == 'USD'])
    try:
        new_ids = new_prod_set - orig_id_set
    except Exception as e:
        print(e)

    message = ""
    for item in new_ids:
        message += item + '\n'
        new_ids_dashless.append(item.replace('-', ''))
    #print(ctr)
    ctr += 1

end = time.time()
print ('set difference time: ')
print(end - start)