import requests

url = "https://www.example.com/image.jpg"
response = requests.get(url)

with open("downloaded.jpg", "wb") as f:
    f.write(response.content)

print("Image downloaded successfully.")
