import requests
import m3u8
url = 'https://d2y36twrtb17ty.cloudfront.net/sessions/7fa35bb7-fb5d-43f3-8296-ac44010e0f95/c99627c4-abb5-4619-a080-ac44010e0fad-3433a924-ef64-4d65-9cd7-ac44011d4808.hls/553954/index.m3u8'
r = requests.get(url)
m3u8_master = m3u8.loads(r.text)
print(m3u8_master.data['segments'][0]['uri'])
for d in m3u8_master.data['segments']:
    print(d['uri'])

