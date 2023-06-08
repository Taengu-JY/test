import base64


f = open ("news/image", "rb")
image = f.readlines()
print(image)

file_base64 = image[0]
path = "news/image.jpg"
with open(path, 'wb') as f :
    decoded_data = base64.decodebytes((file_base64))
    f.write(decoded_data)

f = open("news/article", 'rb')
article = f.readlines()


file_base64 = article[0]
decoded_data = base64.decodebytes((file_base64))
article =decoded_data.decode('utf-8')
print(article)


f.close()