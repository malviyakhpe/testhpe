import pytest
import request
import http.client

conn = http.client.HTTPSConnection("run.mocky.io")
payload = ''
headers = {}
conn.request("GET", "/v3/7379a303-f4d1-41ff-adf2-fb85efe640e0", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

