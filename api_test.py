import requests

data = {
  "acousticness": 0.33,
  "danceability": 0.75,
  "energy": 0.32,
  "instrumentalness": 0.0166,
  "liveness": 0.08,
  "speechiness": 0.03,
  "tempo": 101.93,
  "valence": 0.44
}

response = requests.request("POST", "http://127.0.0.1:4000/prediction/", json=data)

print(response.json())