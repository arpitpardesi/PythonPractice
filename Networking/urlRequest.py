from urllib.request import urlopen

obj = urlopen("https://www.tutorialspoint.com/images/logo.png")
data = obj.read()
img = open("img.jpg", "wb")
img.write(data)
img.close()
