import requests
import json

res_list = []

for i in range(100000000, 200000000, 20)[:10]:
    list_ = ','.join([str(x) for x in range(i, i + 20)])
    URL = f'https://kaspi.kz/yml/product-view/product/?code={list_}&ipf=true'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Referer': 'https://kaspi.kz/shop/c/categories/?page=',
    }

    # cookies = {
    #     '__tld__': "null",
    #     '_fbp': "fb.1.1676868349100.1350009416",
    #     '_ga': "GA1.2.690759166.1676868348",
    #     '_gid':"GA1.2.1714004449.1676868348",
    #     '_hjAbsoluteSessionInProgress': "1",
    #     '_hjFirstSeen': "1",
    #     '_hjIncludedInSessionSample': "1",
    #     '_hjSession_283363': "eyJpZCI6IjJmYjIyNDYzLWIxNjMtNDM0Mi1iMjExLWYyYmM4ZTlmODdjNiIsImNyZWF0ZWQiOjE2NzY4NjgzNDg2NDEsImluU2FtcGxlIjp0cnVlfQ==",
    #     '_hjSessionUser_283363': "eyJpZCI6ImNkYjg1NmUwLThlMjAtNWJiYy1iYjdlLTBmOGVmMzllZTA3ZiIsImNyZWF0ZWQiOjE2NzY4NjgzNDg0MTMsImV4aXN0aW5nIjp0cnVlfQ==",
    #     '_ym_d': "1676868348",
    #     '_ym_isad': "2",
    #     '_ym_uid': "1676868348880903040",
    #     '_ym_visorc': "b",
    #     '.AspNetCore.Culture': "c=ru|uic=ru",
    #     'current-action-name': "Index",
    #     'k_stat': "4921235c-e8e8-45ad-ba0e-878e01c8adf2",
    #     'kaspi.storefront.cookie.city': "750000000",
    #     'ks.cc': "-1",
    #     'ks.ngs.s': "b290027649a2aa1b30fcb3b48322cfd9",
    #     'ks.tg': "96",
    #     'ssaid': "71a146a0-b0d9-11ed-84bd-43f7ae7284b0"
    #     }

    r = requests.get(URL, verify=False, headers=headers)

    res = json.loads(r.text)

    for product in res['data']:
        try:
            name = product['title']
            price = product['unitPrice']
            brand = product['brand']
            category = product['category']
            code = product['id']
            link = product['shopLink']

            # add logic if categry..
            print(name, price, brand, category, code, link)
            res_list.append({
                'name': name,
                'price': price, 
                'brand': brand,
                'category': category, 
                'code': code,
                'link': link})
        except:
            pass
    print()



