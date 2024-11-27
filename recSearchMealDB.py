import http.client

conn = http.client.HTTPSConnection("themealdb.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "1c1c1c59bdmshf84ad70f171c112p1619e7jsnb4194834861d",
    'x-rapidapi-host': "themealdb.p.rapidapi.com"
}

conn.request("GET", "/filter.php?i=chicken", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))