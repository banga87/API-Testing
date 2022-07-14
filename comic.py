import requests

image = requests.get("https://imgs.xkcd.com/comics/python.png")

with open('comic.png', 'wb') as f:
    f.write(image.content)

