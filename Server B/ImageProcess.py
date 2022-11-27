import requests
import json
def main(url):
    api_key = 'acc_be97141480daf2c'
    api_secret = 'bbf0005f7e71d67297ec86dd111a802c'
    image_url = url
    response = requests.get(
    'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
    auth=(api_key, api_secret))
    resp = response.json()
    #print(resp)
    category = ""
    i = 0
    while i < 10:
        T = False
        if (resp['result']['tags'][i]['tag']['en'] == 'car'
            or resp['result']['tags'][i]['tag']['en'] == 'sports car') \
                and resp['result']['tags'][0]['confidence'] > 50:
            category = "car"
            T = True
            return category

        if (resp['result']['tags'][i]['tag']['en'] == 'motorcycle '
            or resp['result']['tags'][i]['tag']['en'] == 'motor') \
                and resp['result']['tags'][0]['confidence'] > 50:
            category = "motorcycle"
            T = True
            return category

        if resp['result']['tags'][i]['tag']['en'] == 'bicycle' \
                and resp['result']['tags'][0]['confidence'] > 50:
            category = "bicycle"
            T = True
            return category

        if i == 9 and T == False:
            return False
        i += 1
