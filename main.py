import requests

with open('valid-proxies.txt','r') as f:
    proxies = f.read().split('\n')

site_to_check = [] 

counter = 0

for site in site_to_check:
    try:
        print(f'using proxy: {proxies[counter]}')
        res = requests.get(site, 
            proxies={'http': proxies[counter],
                     'https': proxies[counter]})
        print(res.status_code)
    except:
        print('Failed')
    finally:
        counter += 1