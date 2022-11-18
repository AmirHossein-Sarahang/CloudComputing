import requests
import json
api_key = 'acc_be97141480daf2c'
api_secret = 'bbf0005f7e71d67297ec86dd111a802c'
image_url = 'https://powersports.honda.com/-/media/products/segment/street/street-assets/2022-cruiser-rebel-1100-tile-750x750.jpg'

response = requests.get(
    'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
    auth=(api_key, api_secret))
resp = response.json()